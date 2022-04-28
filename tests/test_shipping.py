from starlette.testclient import TestClient
from app.main import app
import random
from app.schemas import FreteResponse
router = "/v1/shipping/"

TEST_EXAMPLE = {
    "GOCEP": "27261150",
    "HERECEP": "12223830",
    "weight": "1",
    "format": "1",  # box/package
    "width": "18",
    "length": "15",
    "height": "13",
    "diameter": "0",
}
TEST_RESPONSE = {

}
CEP_EXAMPLE = "12223830"
CEP_FAIL_EXAMPLE = "1222383"
TYPES = (
    'SEDEX', 'PAC', 'SEDEX_10', 'SEDEX_HOJE',
    'E_SEDEX', 'OTE', 'NORMAL', 'SEDEX_A_COBRAR',
)


def test_sucess_shipping_sedex():
    with TestClient(app) as client:
        response = client.post(f"{router}", json={
            "tipo": "sedex",
            "GOCEP": "27261150",
            "HERECEP": "12223830",
            "weight": "1",
            "format": "1",
            "width": "18",
            "length": "15",
            "height": "13",
            "diameter": "0",
        }
                               )
        
        assert response.status_code == 200
        assert response.json()['MsgErro'] == ""
        assert response.json()['Valor'] == "27,70"

def test_sucess_shipping_pac():
    with TestClient(app) as client:
        response = client.post(f"{router}", json={
            "tipo": "pac",
            "GOCEP": "27261150",
            "HERECEP": "12223830",
            "weight": "1",
            "format": "1",
            "width": "18",
            "length": "15",
            "height": "13",
            "diameter": "0",
        }
                               )
        assert response.status_code == 200
        assert response.json()['MsgErro'] == ""
        assert response.json()['Valor'] == "24,30"
        
def test_with_failed_result():
    with TestClient(app) as client:
        response = client.post(f"{router}", json={
            "tipo": "pac",
            "GOCEP": "27261150",
            "HERECEP": "12223830",
            "weight": "1",
            "format": "1",
            "width": "18",
            "length": "15",
            "height": "13",
            "diameter": "0",
        }
                               )
    