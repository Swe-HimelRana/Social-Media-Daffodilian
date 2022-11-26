from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('app/chat/', consumers.ChatConsumer.as_asgi()),
]