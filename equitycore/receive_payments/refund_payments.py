from django.conf import settings
import json
from ..http import post
from ..utils.jengautils import signature

merchant_code = settings.MERCHANT_CODE


def eazzy_refund_payments(
        token,
        transaction_reference,
        transaction_amount,
        transaction_description,
        customer_mobi_number,
        country_code
):
    """
    This web service allows a payment to be voided completely or partially.

    :param token: the bearer token used to access the API
    :param transaction_reference: the transaction reference created after the `receive payment - eazzypush' service e.g 921215770060
    :param transaction_amount: amount to be refunded
    :param transaction_description: the description of the transaction reversal please work
    :param customer_mobi_number: the mobile number of the customer that initiated the transaction 0763000000
    :param country_code: country code
    :return:
    Field Name	    Field Type	Field Description
    reference	    string	    the transaction reference
    status	        string	    the status of the request
    resultCode	    string	    code identifying the status of the transaction

    Example Response
        {
        "reference": "692194625798",
        "status": "SUCCESS",
        "resultCode": "000"
        }
    """

    service = 'EazzyPayOnline'  # application or system from which the payment originated from / system requesting a
    # reversal. Valid Values are : EazzyPayOnline
    channel = 'EAZ'  # the payment channel that was used to make the payment. Valid values are EAZ
    transaction_type = 'refund'  # type of transaction. valid values are reversal refund. In this particular case use
    # refund
    transaction_data = (str(transaction_amount), str(transaction_reference))
    signed_data = signature(transaction_data)

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'signature': signed_data
    }

    payload = "{{\r\n " \
              "\"transaction\":{{\r\n" \
              "\"reference\":\"{0}\", \r\n \"amount\":\"{1}\", \r\n \"service\":\"{2}\", \r\n \"channel\":\"{3}\", " \
              "\r\n \"description\":\"{4}\", \r\n \"type\":\"{5}\", \r\n}}," \
              "\"customer\":{{\r\n" \
              "\"mobileNumber\":\"{6}\", \r\n \"countryCode\":\"{7}\", \r\n}}" \
              "\r\n}} ".format(transaction_reference, transaction_amount, service, channel, transaction_description,
                               transaction_type, customer_mobi_number, country_code)

    url = f"{settings.UAT_URL}/transaction/v2/payments/refund"

    response = post(url, headers=headers, payload=payload)
    data = json.loads(response.text)
    return data
