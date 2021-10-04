from lightparser import LightParser
from models import ExtractResponse


class StoreTask:
    def similar(self, id, country, clp):
        apps = LightParser().extract(
            clp, 'en_US', country
        )
        return apps
