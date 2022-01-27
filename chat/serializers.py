from typing import List
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import ChatRoom, Message
from .config import get_recipients, UserDetail


User = get_user_model()


def get_users(user):
    """ Default method for getting users that the current user can message. By default it will return
    all active users
    """
    return User.objects.filter(is_active=True)



class MessageUserSerializer(serializers.ModelSerializer):
    avatar = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('username', 'name', 'id', 'avatar')
        read_only_fields = ('last_name', 'first_name')

    def to_representation(self, instance):
        instance = UserDetail(instance)
        return super().to_representation(instance)


class ChatRoomSerializer(serializers.ModelSerializer):
    members = MessageUserSerializer(many=True, read_only=True)
    member_usernames = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = ChatRoom
        fields = ('name', 'last_message_date', 'is_group', 'members', 'member_usernames', 'uuid')
        read_only_fields = ('last_message_date', 'members')

    def validate_member_usernames(self, attrs):
        # todo: validate that the list of members are users that the current user can message
        members = list(get_recipients(self.context['user']).filter(username__in=attrs).exclude(id=self.context['user'].id))
        if len(members) == 0:
            raise serializers.ValidationError(_('Members are required.'))
        members.append(self.context['user'])
        return members

    def validate(self, attrs):
        if not attrs['is_group']:
            members = attrs['member_usernames']
            if len(members) > 2:
                raise serializers.ValidationError({'member_usernames': _('Person message can only have 1 member.')})
            key_identifier = ChatRoom.generate_key_identifier(members, attrs['name'])
            if ChatRoom.objects.filter(key_identifier=key_identifier).exists():
                raise serializers.ValidationError({'member_usernames': _('Person room with this user exists.')})
            attrs['key_identifier'] = key_identifier
        return super().validate(attrs)

    def create(self, validated_data):
        members: List = validated_data.pop('member_usernames')
        members.append(self.context['user'])
        chat_room = ChatRoom.objects.create(**validated_data)
        chat_room.members.add(*members)
        return chat_room


class MessageSerializer(serializers.ModelSerializer):
    sender = MessageUserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('sender', 'content', 'creation_date', 'uuid')

    def create(self, validated_data):
        validated_data['sender'] = self.context['user']
        validated_data['room'] = self.context['room']
        return super().create(validated_data)
