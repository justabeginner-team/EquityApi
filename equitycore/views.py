from django.http import HttpResponse
from .jenga import Jenga


def accesstoken(request):
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

    return HttpResponse(access)
