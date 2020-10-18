from django.conf import settings
import json
from ..http import post
from ..utils.jengautils import signature

merchant_code = settings.MERCHANT_CODE


def bill_validation(token,
                    biller_code,
                    customer_ref_number,
                    amount,
                    amount_currency
                    ):
    """

    :param token: the bearer token used to access the API
    :param biller_code: The business number. e.g for ZUKU 32030 is the business number
    :param customer_ref_number: the account number at the billers side e.g 111222
    :param amount: the amount to be paid. In some cases this amount will be validated,
    meaning you might not be allowed to overpay or underpay
    :param amount_currency: the amount's ISO currency eg. KES,USD,EUR
    :return: Success Response Schema
    --------------------------------------------------------------------
    Field Name                |  Field Type |	Field Description
    ---------------------------------------------------------------------
    bill	                  |   object    |   bill object
    bill.CustomerRefNumber    |	  string	|   bill identifier
    bill.amount               |	  string	|   bill amount
    bill.amountCurrency	      |   string	|   bill amount currency
    bill.name	              |   string	|   bill name
    bill.status	              |   boolean	|   bill status true or false
    bill.billStatus	          |   string    |
    createdOn	              |   string	|   bill create date on third party system
    message	                  |   string	|  bill query response message

    Example Response
        {
            "bill": {
                "CustomerRefNumber": "28055948",
                "amount": "20000",
                "amountCurrency": "KES",
                "name": "A N Other",
                "status": true,
                "billStatus": "1",
                "createdOn": "2018-05-21T00:00:00+03:00",
                "message": "SUCCESS"
            }
        }
    """

    payload = "{{\r\n" \
              " \"billerCode\": \"{0}\"," \
              "\"customerRefNumber\": \"{1}\"," \
              "\"amount\": \"{2}\"," \
              "\"amountCurrency\": \"{3}\"" \
              " \r\n}}".format(biller_code, customer_ref_number, amount, amount_currency)

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }

    url = f"{settings.UAT_URL}/transaction/v2/bills/validation"

    response = post(url, headers=headers, payload=payload)
    data = json.loads(response.text)
    return data
