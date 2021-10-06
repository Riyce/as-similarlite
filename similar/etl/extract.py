from similar.etl.models import ExtractRequest, ExtractResponse
from similar.etl.parser.lightparser import LightParser
from similar.etl.transports.urllibtransport import UrllibTransport


class PlaySimilarEtl:
    def similar(self, request: ExtractRequest) -> ExtractResponse:
        transport = UrllibTransport()
        apps = LightParser(transport).extract(
            request.similar_clp, 'en_US', request.country
        )
        return ExtractResponse(request.id, apps)
