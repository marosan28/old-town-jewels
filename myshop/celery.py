import os
from celery import Celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<your_project_name>.settings')
app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.update(
    BROKER_URL=os.environ.get('CLOUDAMQP_URL'),
    CELERY_RESULT_BACKEND=os.environ.get('CLOUDAMQP_URL')
)
