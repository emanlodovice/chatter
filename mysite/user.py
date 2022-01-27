from chat.user import UserDetail


class SiteUserDetail(UserDetail):

    @property
    def avatar(self):
        return 'https://raw.githubusercontent.com/Ashwinvalento/cartoon-avatar/master/lib/images/female/68.png'
