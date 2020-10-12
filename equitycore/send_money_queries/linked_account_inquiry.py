from django.conf import settings
import json
from ..http import post


def get_linked_bank(
        token,
        mobile_number,
):
    """
    This webservice returns the recipients’ Linked Banks linked to the provided phone number on PesaLink

    :param token:
    :param mobile_number:
    :return: Response Schema
    Field Name	    Field Type	Field Description
    banks	        object	    banks object
    bankCode	    string	    bank code as registered by the Kenya Bankers Association (KBA)
    bankName	    string	    bank name
    customerName	string	    customer name

    Example:
    {
        "banks": [
            {
                "bankCode": "11",
                "bankName": "CO-OPERATIVE BANK",
                "customerName": "A N Other"
            }
        ]
    }
    """
    payload = "{{\r\n" \
              " \"mobileNumber\": \"{0}\"," \
              " \r\n}}".format(mobile_number)

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }

    url = f"{settings.UAT_URL}/transaction/v2/pesalink/inquire"

    response = post(url, headers=headers, payload=payload)
    data = json.loads(response.text)
    return data
