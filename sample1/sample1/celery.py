import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sample1.settings')

app = Celery("sample1")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()