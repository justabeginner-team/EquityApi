import time
from django.conf import settings
from django.db import models
from .jenga import get_token


class AuthTokenManager(models.Manager):
    """
    authorization manager token
    """

    def getaccesstoken(self):
        timenow = int(time.time())

        # checks if the token already exists in the database.
        if self.filter().count() == 0:
            token = get_token()
            access_token = token["access_token"]
            expires_in = timenow + int(token["expires_in"])
            self.create(access_token=access_token, expires_in=expires_in, )
            return access_token

        else:
            ''' checks if token has expired if it is update'''
            obj = self.filter()[0]
            if timenow > (obj.expires_in - int(settings.TOKEN_THRESHOLD)):
                token = get_token()
                access_token = token["access_token"]
                expires_in = timenow + int(token["expires_in"])
                auth = self.filter()[0]
                auth.access_token = access_token
                auth.expires_in = expires_in
                auth.save()
                return access_token
            else:
                return obj.access_token
