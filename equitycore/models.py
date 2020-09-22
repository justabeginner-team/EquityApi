from django.db import models
from .managers import AuthTokenManager


class AuthToken(models.Model):
    access_token = models.CharField(max_length=40)
    expires_in = models.BigIntegerField()
    objects = AuthTokenManager()

    def __str__(self):
        return self.access_token
