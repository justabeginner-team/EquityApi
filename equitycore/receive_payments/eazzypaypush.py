from django.conf import settings
import json
from ..http import post
from ..utils.jengautils import signature

merchant_code = settings.MERCHANT_CODE


def eazzypay_push(
        token: str,
        mssid: int,
        countryCode: str,
        trans_amount: int,
        trans_desc: str,
):
    """
    fetch a new token
    :param: type:
    :return: JSON
    """

    trans_type = 'EazzyPayOnline'
    trans_ref = 692194625798
    
    trans_data = (str(trans_ref), str(trans_amount), merchant_code, countryCode)
    signed_signature = signature(trans_data)
    payload = "{{\r\n   \"customer\": {{\r\n      \"mobileNumber\": \"{0}\",\r\n   \"countryCode\": \"{1}\"\r\n  }},\r\n   \"transaction\": {{\r\n      \"amount\": \"{2}\",\r\n      \"description\": \"{3}\",\r\n    \"type\": \"{4}\",\r\n      \"reference\": \"{5}\"\r\n   }}\r\n}}".format(
                 str(mssid),countryCode,str(trans_amount),trans_desc,trans_type,trans_ref)
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'signature': signed_signature
    }
    
    url = f"{settings.UAT_URL}/transaction/v2/payments"
    response = post(url, payload=payload, headers=headers)
    data=json.loads(response.text)

    return payload,data
