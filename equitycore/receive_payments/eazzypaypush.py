from django.conf import settings

from ..http import post
from ..utils.jengautils import signature
from ..models import AuthToken


merchant_code = settings.MERCHANT_CODE


def eazzypay_push(
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
    url = "https://sandbox.jengahq.io/transaction-test/v2/payments"

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

    headers = {
        "authorization": AuthToken.objects.getaccesstoken(),
        "signature": f'{signed_signature}',
        "content-type": 'application/json',
    }

    response = post(url, payload=payload, headers=headers)

    return response.text
