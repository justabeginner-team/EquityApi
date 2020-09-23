
from django.contrib import admin
from .models import AuthToken

class AuthTokenAdmin(admin.ModelAdmin):
    readonly_fields=('access_token','expires_in')


admin.site.register(AuthToken,AuthTokenAdmin)
