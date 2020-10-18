from django.conf import settings
import json
from ..http import post
from ..utils.jengautils import signature

merchant_code = settings.MERCHANT_CODE


def merchant_payments(
        token,
        merchant_till,
        payment_reference,
        payment_amount,
        payment_currency,
        partner_id,
        partner_reference,
):
    """
    This API Provides Partners the Capability To Make Payments For Goods And Services

    :param: token: the bearer token used to access the API
    :param: merchant_till: EazzyPay merchant till identifier of the merchant to be paid. e.g 0766000000
    :param: payment_reference: A unique 12 digit string and is the payment reference
    :param: payment_amount: amount to be paid e.g 1000.00
    :param: payment_currency: currency code of the payment amount in ISO 4217 e.g KES
    :param: partner_id: it is a partner identifier. This will always be the bank account maintained in jengaHQ
            for TILL PAYMENT APIs e.g 0011547896523
    :param: partner_reference: reference of the person making the payment e.g the payers mobile number e.g 987654321
    :return: 200 Success Response Schema
    Field Name	    Field Type	Field Description
    status	        string	    SUCCESS or FAILURE
    merchantName	string	    name of merchant receiving the payment
    transactionId	string	    payment transaction id
    
    
    sample of payload::

        {
            "merchant":{
            "till":"0766000000" 
            },
            "payment":{
            "ref":"539440628712", 
            "amount":"10", 
            "currency":"KES", 
            },
            "partner":{
            "id":"1100161816677", 
            "ref":"0711521508" 
            } 
        }
    
    """

    transaction_data = (
        str(merchant_till), 
        str(partner_id), 
        str(payment_amount),
        str(payment_currency), 
        str(payment_reference)
        )
    
    signed_data = signature(transaction_data)
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'signature': signed_data
    }
    payload = "{{\r\n" \
              "\"merchant\":{{\r\n \"till\":\"{0}\" \r\n}}," \
              "\"payment\":{{\r\n \"ref\":\"{1}\", \r\n \"amount\":\"{2}\", \r\n \"currency\":\"{3}\", \r\n}}," \
              "\"partner\":{{\r\n \"id\":\"{4}\", \r\n \"ref\":\"{5}\" \r\n}}" \
              " \r\n}}".format(
                                merchant_till,
                                payment_reference, 
                                payment_amount, 
                                payment_currency,
                                partner_id, 
                                partner_reference
                                )


    url = f"{settings.UAT_URL}/transaction/v2/tills/pay"
    response = post(url, payload=payload, headers=headers)
    data = json.loads(response.text)
    print(payment_reference)
    response_data = dict(
        token=token,
        ref=payment_reference,
        data=data
    )
    return response_data
