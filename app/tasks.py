from celery import Celery, shared_task

from models import ExtractResponse, ExtractRequest
from storetask import StoreTask


app = Celery('tasks')
app.config_from_object('celeryconfig')


@shared_task(
    bind=True,
    name='ps.similar'
)
def get_similars(request: ExtractRequest) -> ExtractResponse:
    result = StoreTask().similar(request)
    return result
