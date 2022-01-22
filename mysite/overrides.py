from django.contrib.auth.models import User


def get_recipients(user):
    return User.objects.filter(is_staff=True)