from django.http import HttpResponse
from .jenga import Jenga





def accesstoken(request):
    #token = get_token()
    #print(token.get("access_token"))
    
    #url = "https://uat.jengahq.io/transaction/v2/payment/mpesastkpush"
    
    countryCode= "KE"
    mssid="0715112499"
    amount="100"
    desc="stkpush"
    

    access=Jenga.lipanampesapush(mssid,countryCode,amount,desc)

    
    return HttpResponse(access)
