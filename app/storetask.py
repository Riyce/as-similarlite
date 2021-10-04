from lightparser import LightParser
from models import ExtractResponse


class StoreTask:
    def similar(self, request):
        apps = LightParser().extract(
            request.similar_clp, 'en_US', request.country
        )
        return ExtractResponse(request.id, apps)
