from pydantic import BaseSettings

class Settings(BaseSettings):
    #producao_prazo: str
    fretefixo_prazo: str
    fretefixo_valor: str
    correios_sceporigem: str
    correios_ncdempresa: str
    correios_sdssenha: str
    class Config:
        env_file = ".env"
        

settings = Settings()
    