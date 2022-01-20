from django.views.generic import TemplateView
from django.utils.functional import cached_property
from django.shortcuts import get_object_or_404

from rest_framework import (
    viewsets,
    permissions,
    mixins,
)

from typing import Any, Dict

from . import config
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer

class Home(TemplateView):
    template_name = 'chat/index.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['config'] = config
        return context


class ChatRoomViewset(viewsets.ModelViewSet):
    serializer_class = ChatRoomSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'uuid'

    def get_queryset(self):
        return self.request.user.chat_rooms.order_by('-last_message_date')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


class MessageViewset(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'uuid'

    @cached_property
    def room(self) -> ChatRoom:
        if 'room_uuid' not in self.kwargs:
            return None
        return get_object_or_404(self.request.user.chat_rooms.all(), uuid=self.kwargs['room_uuid'])

    def get_queryset(self):
        return self.room.messages.order_by('-creation_date')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['room'] = self.room
        context['user'] = self.request.user
        return context
