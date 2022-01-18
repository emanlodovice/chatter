from typing import List

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


def blank_json():
    return {}


class ChatRoom(models.Model):
    is_group = models.BooleanField(default=False)
    name = models.CharField(blank=True, max_length=100, verbose_name=_('Room name'))
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_message_date = models.DateTimeField(default=timezone.now, verbose_name=_('Last message date'))
    members = models.ManyToManyField(User, related_name='chat_rooms', blank=True, verbose_name=_('Members'))
    key_identifier = models.TextField(db_index=True)

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def generate_key_identifier(members: List[User], name: str):
        ids = sorted([member.pk for member in members])
        key = ''
        for id in ids:
            key += f'-{id}-'
        return key + name


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE, verbose_name=_('Chat room'))
    sender = models.ForeignKey(User, related_name='chat_messages', on_delete=models.CASCADE, verbose_name=_('Sender'))
    content = models.TextField(verbose_name=_('Content'))
    meta = models.JSONField(verbose_name=_('meta'), default=blank_json, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))

    def __str__(self) -> str:
        return f'{self.room.name} - {self.id}'

    def save(self, *args, **kwargs):
        is_new = self.id is None
        result = super().save(*args, **kwargs)
        if is_new:
            # make sure to sync room's last_message_date field
            self.room.last_message_date = self.creation_date
            self.room.save(update_fields=('last_message_date',))
        return result
