from celery import shared_task

from similar.etl.models import ExtractResponse, ExtractRequest
from similar.etl.extract import PlaySimilarEtl


@shared_task(
    bind=True,
    name='ps.similar',
)
def get_similars(self, request: ExtractRequest) -> ExtractResponse:
    result = PlaySimilarEtl().similar(request)
    return result