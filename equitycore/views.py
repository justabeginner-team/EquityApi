from django.conf import settings
from django.http import HttpResponse

# in app imports
from .models import AuthToken
from .utils.jengautils import get_token,signature
from equitycore.receive_payments.eazzypaypush import eazzypay_push
from .jenga import Jenga



def accesstoken(request):
    
    #access = AuthToken.objects.getaccesstoken()
    #access=get_token()
    #access=signature(("0765521578","KE","100","HALLO"))
    access = Jenga.eazzypaypush(765521578, "KE", 100, "HALLO")
    
    return HttpResponse(access)
