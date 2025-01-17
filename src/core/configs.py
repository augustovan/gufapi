from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://geek:university@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    class Config:
        case_sensite = True

settings = Settings()
