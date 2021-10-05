import os

from dotenv import load_dotenv

load_dotenv()

RESULT_BACKEND = os.getenv('RESULT_BACKEND')
BROKER_URL = os.getenv('BROKER_URL')

CELERY_CONF = dict(
    task_serializer='pickle',
    result_serializer='pickle',
    accept_content=['json', 'pickle'],
    broker_url=BROKER_URL,
    result_backend=RESULT_BACKEND,
    task_routes={'ps.similar': {'queue': 'ps_similar'}},
    enable_utc=True
)