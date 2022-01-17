from django.urls import path
from rest_framework import routers

from .views import Home, ChatRoomViewset

router = routers.SimpleRouter()
router.register(r'rooms', ChatRoomViewset, basename='chatroom')


urlpatterns = [
    path('', Home.as_view(), name='chat.Home'),
] + router.urls