from chat import serializers
from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework import permissions

from typing import Any, Dict

from . import config
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer

class Home(TemplateView):
    template_name = 'chat/index.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['config'] = config
        return context


class ChatRoomViewset(viewsets.ModelViewSet):
    serializer_class = ChatRoomSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.chat_rooms.order_by('-last_message_date')
    
