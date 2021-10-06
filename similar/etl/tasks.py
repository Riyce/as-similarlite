from celery import shared_task

from similar.etl.extract import PlaySimilarEtl
from similar.etl.models import ExtractRequest, ExtractResponse


@shared_task(
    bind=True,
    name='ps.similar',
)
def get_similars(self, request: ExtractRequest) -> ExtractResponse:
    result = PlaySimilarEtl().similar(request)
    return result
