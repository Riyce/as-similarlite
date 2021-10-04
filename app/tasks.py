from celery import Celery

from storetask import StoreTask


app = Celery('tasks')
app.config_from_object('celeryconfig')


@app.task
def add(x, y):
    return x + y


@app.task
def test_task(name):
    return f'It`s {name}'


@app.task
def get_similars(id, country, clp):
    result = StoreTask().similar(id, country, clp)
    return result
