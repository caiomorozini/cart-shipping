from pydantic import BaseModel, constr, confloat, conint
from typing import List
from pycorreios import Correios

class Fields(BaseModel):
    tipo: str = "sedex"
    GOCEP: constr(
        strip_whitespace=True, 
        regex='[0-9]{8}',
        min_length=8,
        max_length=8,
        )
    HERECEP: constr(
        strip_whitespace=True, 
        regex='[0-9]{8}',
        min_length=8,
        max_length=8,
        )
    peso: constr(
        strip_whitespace=True
        ) 
    formato: str = "0"
    largura: str = "0"
    comprimento: str = "0"
    altura: str = "0"
    diametro: str = "0"

class Products(BaseModel):
    sku: str = 'SKU1'
    quantity: conint(gt=0) = 10
    price: confloat(gt=0) = 101.12
    weight: confloat(gt=0) = 11.0
    width: confloat(gt=0) =  10.0
    height: confloat(gt=0) = 11.0
    lenght: confloat(gt=0) = 12.0
    
class Payload(BaseModel):
    zipcode: str = '05448000'
    products: List[Products]
        

class FreteResponse(BaseModel):
    id: int
    name: str
    value: str
    prazo: str
    erro: str
