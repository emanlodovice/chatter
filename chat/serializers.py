from django.db.models import fields
from django.contrib.auth import get_user, get_user_model
from rest_framework import serializers

from .models import ChatRoom, Message


User = get_user_model()


class MessageUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'id')
        read_only_fields = ('last_name', 'first_name')


class ChatRoomSerializer(serializers.ModelSerializer):
    members = MessageUserSerializer(many=True)
    class Meta:
        model = ChatRoom
        fields = ('name', 'last_message_date', 'is_group', 'members')


class MessageSerializer(serializers.ModelSerializer):
    user = MessageUserSerializer(required=True)

    class Meta:
        model = Message
        fields = ('content', 'creation_date', 'user')
