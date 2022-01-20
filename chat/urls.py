from django.urls import path
from rest_framework import routers

from .views import Home, ChatRoomViewset, MessageViewset

router = routers.SimpleRouter()
router.register(r'rooms', ChatRoomViewset, basename='chatroom')
router.register(r'rooms/(?P<room_uuid>[-\w]+)/messages', MessageViewset, basename='chat-messages')


urlpatterns = [
    path('', Home.as_view(), name='chat.Home'),
] + router.urls