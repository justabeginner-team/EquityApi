from django.conf import settings
import json

from ..http import get


def eazzypaypush_status(
        token,
        transaction_reference
):
    """
    The webservice enables an application track the status of a payment that is linked to
    the Receive Payments - Eazzypay Push web service especially in failure states

    :param: token: the bearer token used to access the API
    :param: transaction_reference: this is the reference returned by create payment API - eazzypaypush
    :return: 200 Success Response
    Field Name	        Field Type	    Field Description
    transactionRef	    string	        The transaction reference of the payment

    status	            string	        The status of the transaction
                                        0: Transaction approved successfully.
                                        1: Transaction pending approval.
                                        3: Failed. Customer pin validation error.
                                        4: Pin Validation Time Out
                                        5: Failed. Insufficient funds in customer account.
                                        6: Failed. Transaction rejected by customer.
                                        7: Failed. Maximum or Minimum threshold amount exceeded.

    message	            string	        status message
    """

    headers = {
        'Authorization': token,
    }

    payload = {}

    url = f"{settings.UAT_URL}/transaction/v2/payments/details/{transaction_reference}"
    response = get(url, payload=payload, headers=headers)
    data = json.loads(response.text)

    return data
