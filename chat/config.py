import os
import importlib
from django.conf import settings


PAGE_HEADING = getattr(settings, 'CHAT_PAGE_HEADING', 'Chat')
CLIENT_URL = getattr(settings, 'CHAT_CLIENT_URL', os.path.join(settings.STATIC_URL, 'chat/index.html'))

RECIPIENTS_METHOD_PATH = getattr(settings, 'CHAT_RECIPIENTS_METHOD', 'chat.serializers.get_users')


def get_recipients(user):
    module_name, get_recipients_method_name = RECIPIENTS_METHOD_PATH.rsplit('.',1)
    recipients_method_module = importlib.import_module(module_name)
    recipients_method = getattr(recipients_method_module, get_recipients_method_name)
    return recipients_method(user)


USER_CLASS = getattr(settings, 'CHAT_USER_CLASS', 'chat.user.UserDetail')
user_module_name, user_class_name = USER_CLASS.rsplit('.', 1)
user_module = importlib.import_module(user_module_name)
UserDetail = getattr(user_module, user_class_name)