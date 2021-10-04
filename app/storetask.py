from lightparser import LightParser
from models import ExtractResponse, ExtractRequest


class StoreTask:
    def similar(self, **kwargs) -> ExtractResponse:
        apps = LightParser().extract(
            kwargs['similar_clp'], 'en_US', kwargs['country']
        )
        return apps
