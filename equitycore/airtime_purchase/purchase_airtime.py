from django.conf import settings
import json
from ..http import post
from ..utils.jengautils import signature

merchant_code = settings.MERCHANT_CODE


def airtime(
        token,
        country_code,
        mobile_number,
        airtime_amount,
        airtime_reference,
        airtime_telco
):
    """
    This gives an application the ability to purchase airtime from any telco in East and Central Africa.

    :param token: the bearer token used to access the API
    :param country_code: the telco's ISO country code i.e KE
    :param mobile_number: the mobile number you are purchasing airtime for
    :param airtime_amount: the airtime amount
    :param airtime_reference: A unique 12 digit string and it is the transaction reference
    :param airtime_telco: the telco/provider. For example: Equitel, Safaricom , Airtel.
    :return: Response Schema
    Field Name	        Field Type	Field Description
    referenceNumber	    string	    reference number for the transaction
    status	            string	    status of transaction

    Example
    {
        "referenceNumber": "4568899373748",
        "status": "SUCCESS"
    }

    """
    transaction_data = (merchant_code, str(airtime_telco), str(airtime_amount), str(airtime_reference))
    signed_data = signature(transaction_data)
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'signature': signed_data
    }
    payload = "{{\r\n" \
              "\"customer\":{{\r\n \"countryCode\":\"{0}\", \r\n \"mobileNumber\":\"{1}\", \r\n}}," \
              "\"airtime\":{{\r\n \"amount\":\"{2}\", \r\n \"reference\":\"{3}\", \r\n \"telco\":\"{4}\", \r\n}}" \
              "\r\n}}".format(country_code, mobile_number, airtime_amount,
                              airtime_reference, airtime_telco)

    url = f"{settings.UAT_URL}/transaction/v2/airtime"
    response = post(url, payload=payload, headers=headers)
    data = json.loads(response.text)

    return data
