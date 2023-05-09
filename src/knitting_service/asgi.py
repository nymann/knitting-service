from knitting_service.api import Api
from knitting_service.core.config import Config
from knitting_service.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api
