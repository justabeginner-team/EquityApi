from django.conf import settings
from django.db import transaction
import json
from ..http import post
from ..utils.jengautils import signature
from ..models import EazzyPushRequest

merchant_code = settings.MERCHANT_CODE


def eazzypay_push(
        pk :int ,
        token: str,
        mssid: int,
        countryCode: str,
        trans_amount: int,
        trans_desc: str,
        trans_ref: str,
):
    """
    Initiate an Eazzypay push request

    :param: token:
    :param: mssid:
    :param: CountryCode:
    :param: trans_amount:
    :param: trans_desc:
    :return: response
    """
    print(trans_ref)
    trans_type = 'EazzyPayOnline'

    trans_data = (str(trans_ref), str(trans_amount), merchant_code, countryCode)
    signed_data = signature(trans_data)

    payload = "{{\r\n   \"customer\": {{\r\n      \"mobileNumber\": \"{0}\",\r\n   \"countryCode\": \"{1}\"\r\n  }}," \
              "\r\n   \"transaction\": {{\r\n      \"amount\": \"{2}\",\r\n      \"description\": \"{3}\"," \
              "\r\n    \"type\": \"{4}\",\r\n      \"reference\": \"{5}\"\r\n   }}\r\n}}".format(
        str(mssid), countryCode, str(trans_amount), trans_desc, trans_type, trans_ref)

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'signature': signed_data
    }

    url = f"{settings.UAT_URL}/transaction/v2/payments"
    
    with transaction.atomic():
        response = post(url, payload=payload, headers=headers)
        data = json.loads(response.text)
        user = EazzyPushRequest.objects.select_for_update().get(id=pk)
        
        if not user.is_posted:
            #pass
                user.transaction_type=trans_type,
                user.api_transaction_reference=data.get("referenceNumber"),
                user.transaction_reference=trans_ref,
                user.transaction_status=data.get("status"),
                user.is_posted=True
                user.save()

    responseData = dict(
        token=token,
        ref=trans_ref,
        data=data
    )
    return responseData
