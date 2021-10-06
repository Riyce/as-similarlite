from celery import Celery

from app.settings import CELERY_CONF as conf


APPS = ['similar']
app = Celery('app', **conf)
app.autodiscover_tasks(packages=APPS)
