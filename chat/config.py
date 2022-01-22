import importlib
from django.conf import settings


PAGE_HEADING = getattr(settings, 'CHAT_PAGE_HEADING', 'Chat')
RECIPIENTS_METHOD_PATH = getattr(settings, 'CHAT_RECIPIENTS_METHOD', 'chat.serializers.get_users')
module_name, get_recipients_method_name = RECIPIENTS_METHOD_PATH.rsplit('.',1)


def get_recipients(user):
    recipients_method_module = importlib.import_module(module_name)
    recipients_method = getattr(recipients_method_module, get_recipients_method_name)
    return recipients_method(user)
