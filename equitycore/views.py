from django.http import HttpResponse
from .jenga import Jenga
from .receive_payments_queries.query_transaction_details import query_transaction
from .models import AuthToken
from .helpers import reference_id_generator
from .receive_payments.bill_validation import bill_validation
import equitycore.exceptions as exceptions


def accesstoken(request):
    # token = get_token()
    # print(token.get("access_token"))

    # url = "https://uat.jengahq.io/transaction/v2/payment/mpesastkpush"

    countryCode = "KE"
    mssid = "0764555372"
    amount = "10"
    desc = "eazzy pay push"
    # query = query_transaction(AuthToken.objects.getaccesstoken(), "797969035827")
    # query=reference_id_generator()
    # print(query)
    # print(query)

    # raise exceptions.EazzyPayPushError(str(mssid))
    Jenga.eazzypaypush(mssid, countryCode, amount, desc)
    # Jenga.lipanampesapush(mssid,countryCode,amount,desc)
    access = "hallo nigga"
    # bill_validation()
    return HttpResponse(access)
