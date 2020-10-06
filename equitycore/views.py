from django.http import HttpResponse
from .jenga import Jenga


def accesstoken(request):
<<<<<<< HEAD
    #token = get_token()
    #print(token.get("access_token"))
    
    #url = "https://uat.jengahq.io/transaction/v2/payment/mpesastkpush"
    
    countryCode= "KE"
    mssid = "0765521578"
    amount="1"
    desc="eazzy pay push"
    
    Jenga.eazzypaypush(mssid,countryCode,amount,desc)
    #Jenga.lipanampesapush(mssid,countryCode,amount,desc)
    access="hallo nigga"
    
=======
    # token = get_token()
    # print(token.get("access_token"))

    # url = "https://uat.jengahq.io/transaction/v2/payment/mpesastkpush"

    countryCode = "KE"
    mssid = "0763181872"
    amount = "1"
    desc = "eazzy pay push"

    Jenga.eazzypaypush(mssid, countryCode, amount, desc)
    # Jenga.lipanampesapush(mssid,countryCode,amount,desc)
    access = "hallo nigga"

>>>>>>> d0d1fad84997e203f6e3ed1f050223544b4ae757
    return HttpResponse(access)
