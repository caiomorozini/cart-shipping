import logging
from .const import SHIPMENTS
import fastapi
from app.config import settings
from pycorreios import Correios
import asyncio
import pandas as pd

def parser(payload: dict):
    shipping = {}
    shipping['zipcode'] = payload.get('zipcode', 'zipcode not found')
    df = pd.DataFrame(payload['products'])
    
    # set total items
    shipping['items_total'] = len(payload['products'])
    
    # calculating total price
    price_total = df['price'].mul(df['quantity']).sum()
    
    # formatting total price in 2 digits
    shipping['price_total'] = float(f'{price_total:.2f}')
    
    # set weight of all items
    shipping['weight_total'] = df['weight'].sum()
    
    # set volume of all items
    df.loc[:,'volume'] = df['quantity']*df['height']*df['width']*df['lenght']
    shipping['volume_total'] = df['volume'].sum()
    
    # set cubage of all items
    df.loc[:,'cubage'] = df['width']*df['height']*df['lenght']*df['weight']
    
    # recalculate WxHxL of package based on total volume
    biggest_size = df['height'].max()
    other_sizes = pow(base=df['volume'].sum(), exp=1/2)
    shipping['adjusted_total_boxsize'] = (
        [biggest_size, other_sizes, other_sizes]
    )
    
    # if biggest_size is less than a half of other_sizes
    if biggest_size < other_sizes/2:
        sizes = pow(base=df['volume'].sum(), exp=1/3)
        shipping['adjusted_total_boxsize'] = (
        [sizes, sizes, sizes]
    )
    logging.info('[+] processed payload: ', shipping)
    return shipping
    
    
def select_shipment(shipment: str) -> int:
    return SHIPMENTS.get(
        shipment.upper().replace(" ", ""), "Shipping not Found"
    )

def fixed(shipping_cost: str = settings.fretefixo_valor,
    name: str = 'Frete Fixo',) -> dict:
    return {
        'id': '0001',
        'name': name,
        'value': shipping_cost,
        'prazo': settings.fretefixo_prazo,
        'erro': '',
    }
                                                                                      
def free() -> dict:
    return fixed('0', 'Frete Grátis')


def correios_raw(data: dict) -> dict:
    corr = Correios()
    return corr.frete(**data)


async def correios(shipping: dict, service, name):
    payload = {
        'HERECEP': settings.correios_sceporigem,
        'GOCEP': shipping.get('shipping', 'Shipping not found'),
        'peso': shipping.get('weight_total', 'weight_total not found'),
        'formato': '1',
        'comprimento': shipping['adjusted_total_boxsize'][0],
        'altura': shipping['adjusted_total_boxsize'][1],
        'largura': shipping['adjusted_total_boxsize'][2],
        'cod': service,
        'diametro': '0',
        
    }
    correios_quote = correios_raw(payload)
    return {
        'id': service,
        'name': name,
        'value': correios_quote.get('Valor'),
        'prazo': correios_quote.get('PrazoEntrega'),
        'erro': correios_quote.get('MsgErro'),
    }