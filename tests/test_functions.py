from app.functions import select_shipment, fixed, free
from pycorreios import Correios
from app.config import settings
import logging

def test_select_shipment_sedex():
    response = select_shipment("sedex")
    assert response == Correios.SEDEX

def test_select_shipment_error():
    response = select_shipment("sedx")
    assert response == "Shipping not Found"
    
def test_select_shipment_pac():
    response = select_shipment("pac")
    assert response == Correios.PAC
    
def test_select_shipment_sedex10():
    response = select_shipment("sedex_10 ")
    assert response == Correios.SEDEX_10
    
def test_select_shipment_sedex_hoje():
    response = select_shipment("sedex_hoje")
    assert response == Correios.SEDEX_HOJE
    
def test_select_shipment_esedex():
    response = select_shipment("e_sedex")
    assert response == Correios.E_SEDEX
    
def test_method_fixed():
    data = '100.00'
    data_return = {
        'erro': '',
        'id': '0001',
        'name': 'Frete Fixo',
        'value': '100.00',
        'prazo': settings.fretefixo_prazo,
    }
    response = fixed(data)
    logging.debug(response)
    assert response == data_return

def test_method_fixed_without_params():
    data_return = {
        'erro': '',
        'id': '0001',
        'name': 'Frete Fixo',
        'value': settings.fretefixo_valor,
        'prazo': settings.fretefixo_prazo,
    }
    response = fixed()
    logging.debug(response)
    assert response == data_return
