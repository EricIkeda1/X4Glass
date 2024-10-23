from django.urls import re_path
from GlassHubApp.consumers import EventConsumer

websocket_urlpatterns = [
    re_path(r'ws/eventos/$', EventConsumer.as_asgi()),
]