from django.conf import settings

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
    
    
  
    headers = {
        'Content-Type': 'application/json',
        'Authorization':f"{token}",
        'signature': signed_signature,
    }
    payload = {
        "customer": {
            "mobileNumber": str(mssid),
            "countryCode": countryCode,
        },
        "transaction": {
            "amount": str(trans_amount),
            "description": trans_desc,
            "type": trans_type,
            "reference": trans_ref,
        }
    }
    url = "https://sandbox.jengahq.io/transaction-test/v2/payments"
    response = post(url, payload=payload, headers=headers)

    return token,response.text

   
