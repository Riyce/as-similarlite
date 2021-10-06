from similar.etl.models import ExtractRequest, ExtractResponse
from similar.etl.parser.lightparser import LightParser


class PlaySimilarEtl:
    def similar(self, request: ExtractRequest) -> ExtractResponse:
        apps = LightParser().extract(
            request.similar_clp, 'en_US', request.country
        )
        return ExtractResponse(request.id, apps)
