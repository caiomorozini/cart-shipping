from fastapi import (APIRouter, status)
from pycorreios import Correios
from ..schemas import Payload, FreteResponse
import logging
from ..functions import correios, parser, free, fixed, select_shipment

router = APIRouter(
    prefix="/v1/shipping",
    tags=["shipping"],
)

@router.post(
    "/", 
    status_code=status.HTTP_200_OK, 
    response_model=FreteResponse
    )
async def quote(payload: Payload) -> dict:
    data = parser(payload.dict())
    if data.get('price_total') > 300:
        return free()
    elif data.get('zipcode') == '0544800':
        return fixed()
    
    services = ['sedex', 'pac', 'sedex_10']
    s_codes = {service:select_shipment(service) for service in services}
    response = {} 
    for service in services:
        response[service] = await correios(data, s_codes.get(service), service)
    return response
        