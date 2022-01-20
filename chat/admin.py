from django.contrib import admin

from .models import ChatRoom, Message


class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'creation_date', 'last_message_date', 'is_group')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'sender', 'creation_date')


admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Message, MessageAdmin)
