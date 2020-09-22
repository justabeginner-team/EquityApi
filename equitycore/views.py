from django.conf import settings
from django.http import HttpResponse

# in app imports
from .models import AuthToken


def accesstoken(request):
    access = AuthToken.objects.getaccesstoken()

    return HttpResponse(access)
