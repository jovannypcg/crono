from celery import Celery

CELERY_TASK_QUEUE = 'celery_mongo_sample'

app = Celery(CELERY_TASK_QUEUE)
app.config_from_object('celery_config')


@app.task
def expose_data():
    return 1
