from django.contrib.auth import get_user_model
from django.templatetags.static import static


User = get_user_model()


class UserDetail:
    def __init__(self, user: User) -> None:
        self.user = user

    @property
    def username(self):
        return self.user.username

    @property
    def name(self):
        return self.user.get_full_name()

    @property
    def id(self):
        return self.user.id

    @property
    def avatar(self):
        return static('chat/default_avatar.jpeg')
