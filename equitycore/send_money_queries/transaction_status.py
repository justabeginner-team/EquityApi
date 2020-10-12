from django.conf import settings
import json
from ..http import post


def get_status(
        token,
        request_id,
        destination_type,
        transfer_date
):
    """
    This API checks the status of a B2C transaction
    :param token: bearer token used to access the API
    :param request_id: transfer reference sent in original transaction
    :param destination_type: B2C Wallet. Currently only Mpesa has been enabled
    :param transfer_date: date of transfer
    :return: Response Schema
    Field Name	        Field Type	Field Description
    transactionId	    string	    B2C Wallet. Currently only Mpesa has been enabled
    mpesaref	        string	    Unique identifier to identify a transaction on M-Pesa
    transactiondate	    string	    date of transfer
    recipientName	    string	    recipient name
    wallettype	        string	    B2C Wallet. Currently only Mpesa has been enabled
    mpesacode	        string	    transaction result code
    mpesaDesc	        string	    transaction result description
    response_code	    string	    response code
    response_status	    string	    response status
    """

    payload = "{{\r\n" \
              " \"requestId\": \"{0}\"," \
              "\"destination\": {{\r\n  \"type\": \"{1}\" \r\n }}" \
              "\"transfer\": {{\r\n  \"date\": \"{2}\" \r\n }}" \
              " \r\n}}".format(request_id, destination_type, transfer_date)

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }

    url = f"{settings.UAT_URL}/transaction/v2/b2c/status/query"

    response = post(url, headers=headers, payload=payload)
    data = json.loads(response.text)
    return data
