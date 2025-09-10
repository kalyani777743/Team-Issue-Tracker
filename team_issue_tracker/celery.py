import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'team_issue_tracker.settings')

app = Celery('team_issue_tracker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
