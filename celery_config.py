from celery.schedules import crontab
from datetime import timedelta

BROKER_URL = 'amqp://guest@localhost'

CELERYBEAT_SCHEDULE = {
    'every_minute': {
        'task': 'worker.expose_data',
        'schedule': timedelta(seconds=1)
    }
}
