# cartme-shipping-fastapi

## Instalar todos os pacotes
```
poetry install
```
## Iniciar o servidor

```
poetry run uvicorn app.main:app --reload
```

## Executar testes

```
poetry run pytest tests/ -v -x
```
## Contract Example
```json
{
  "zipcode": "05448000",
  "products": [
    {
      "sku": "SKU1",
      "quantity": 1,
      "price": 11,
      "weight": 11,
      "width": 10,
      "height": 11,
      "lenght": 12
    }
  ]
}
```

## Curl Example
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/v1/shipping/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "tipo": "sedex",
  "GOCEP": "44001535",
  "HERECEP": "03971010",
  "peso": "1",
  "formato": "0",
  "largura": "18",
  "comprimento": "9",
  "altura": "13.5",
  "diametro": "0"
}'
```

## Response

```json
{
  "MsgErro": "",
  "Erro": "0",
  "Codigo": "40010",
  "Valor": "75,00",
  "PrazoEntrega": "2",
  "ValorMaoPropria": "0,00",
  "ValorValorDeclarado": "0,00",
  "EntregaDomiciliar": "S",
  "EntregaSabado": "N"
}
```