from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from .views import Home, ChatRoomViewset, MessageViewset, RecipientsViewset, ClientView

router = routers.SimpleRouter()
router.register(r'rooms', ChatRoomViewset, basename='chatroom')
router.register(r'rooms/(?P<room_uuid>[-\w]+)/messages', MessageViewset, basename='chat-messages')
router.register(r'recipients', RecipientsViewset, basename='chat-recipients')


urlpatterns = [
    path('', ClientView.as_view(), name='chat.ClientView'),
    path('refresh-token', TokenRefreshView.as_view(), name='chat.TokenRefreshView'),
    path('testing', Home.as_view(), name='chat.Home'),
] + router.urls