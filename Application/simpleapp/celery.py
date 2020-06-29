import os
from celery import Celery
from django.core.cache import cache

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simpleapp.settings')

app = Celery('simpleapp')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
