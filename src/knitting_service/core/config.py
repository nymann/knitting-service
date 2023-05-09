from pydantic import BaseSettings

from knitting_service.version import __version__


class Config(BaseSettings):
    title: str = "Knitting Service"
    version: str = __version__

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
