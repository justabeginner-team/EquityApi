import time
from django.conf import settings
from django.db import models
from .utils.jengautils import get_token


class AuthTokenManager(models.Manager):
    """
    authorization manager token
    """

    def getaccesstoken(self):
        timenow = int(time.time())
        token = get_token()
        # check if the token already exists in the database.
        if self.filter().count() == 0:
           
            print(token)
            access_token = "Bearer " + token["access_token"]
            expires_in = timenow + int(token["expires_in"])
            self.create(access_token=access_token, expires_in=expires_in, )
            return access_token

        else:
            # check if it's expired
            # if it update
            obj = self.filter()[0]
            if timenow > (obj.expires_in - int(settings.TOKEN_THRESHOLD)):
                token = get_token()
                access_token = "Bearer  " + token.get("access_token")
                expires_in = timenow + int(token["expires_in"])
                auth = self.filter()[0]
                auth.access_token = access_token
                auth.expires_in = expires_in
                auth.save()
                return access_token
            else:
                return obj.access_token
