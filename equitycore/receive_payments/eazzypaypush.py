from django.conf import settings

from ..http import post
from ..jenga import signature


def eazzypay_push():
    """
    fetch a new token
    :param: type:
    :return: JSON
    """

    transaction_reference = ''
    transaction_amount = ''
    merchant_code = settings.MERCHANT_CODE
    customer_country_code = 'KE'

    url = f"{settings.SANDBOX_URL}/identity/v2/payments"
    payload = {
        "customer": {
            "mobileNumber": "0765555125",
            "countryCode": f"{customer_country_code}"
        },
        "transaction": {
            "amount": f"{transaction_amount}",
            "description": "A short description",
            "type": "exampleType",
            "reference": f"{transaction_reference}"
        }
    }
    signed_signature = signature((transaction_reference, transaction_amount, merchant_code, customer_country_code))

    headers = {
        "authorization": f"{settings.API_KEY}",
        "signature": f'{signed_signature}',
        "content-type": 'application/json',
    }

    response = post(url, payload=payload, headers=headers)

    return response
