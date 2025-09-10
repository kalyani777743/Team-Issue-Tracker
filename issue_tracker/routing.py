from django.urls import re_path
from .consumers import IssueNotificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/project/(?P<project_id>\d+)/$', IssueNotificationConsumer.as_asgi()),
]
