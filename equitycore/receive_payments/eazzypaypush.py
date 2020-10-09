from django.conf import settings
import json
from ..http import post
from ..utils.jengautils import signature
from ..models import EazzyPushRequest

merchant_code = settings.MERCHANT_CODE


def eazzypay_push(
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
    response = post(url, payload=payload, headers=headers)
    data = json.loads(response.text)

    EazzyPushRequest.objects.update(
        transaction_type=trans_type, api_transaction_reference=data.get("referenceNumber"),
        transaction_reference=trans_ref, transaction_status=data.get("status"))

    responseData = dict(
        token=token,
        ref=trans_ref,
        data=data
    )
    return responseData
