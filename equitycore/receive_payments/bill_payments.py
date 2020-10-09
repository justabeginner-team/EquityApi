from django.conf import settings
import json
from ..http import post
from ..utils.jengautils import signature

merchant_code = settings.MERCHANT_CODE


def bill_payments(
        token,
        biller_code,
        country_code,
        bill_reference,
        bill_amount,
        bill_currency,
        payer_name,
        payer_account,
        payer_reference,
        payer_mobile_number,
        partner_id,
        remarks
):
    """
    This API Provides Partners the Capability To Initiate Utility Bill Payments For Goods And Services

    :param: token: the bearer token used to access the API
    :param: biller_code: the business number. e.g for ZUKU 32030 is the business number
    :param: country_code: country of the biller account
    :param: bill_reference: invoice/ref number against which the bill will be paid 111222
    :param: bill_amount: amount of bill to be paid
    :param: bill_currency: currency code of the payment amount in ISO 4217 e.g KES
    :param: payer_name: name of the person making the payment e.g A N.Other
    :param: payer_account: invoice/ref number against which the bill will be paid. same as bill reference e.g 111222
    :param: payer_reference: A unique 12 digit string and it is the payer's reference
    :param: payer_mobile_number: payer mobile number e.g 0763000000
    :param: partner_id: partner identifier. This will always be the bank account maintained in jengaHQ
    for BILL PAYMENT APIs e.g 0011547896523
    :param: remarks: remarks of the bill payment
    :return: 200 Success Response Schema
    Field Name	     Field Type	  Field Description
    status	         string	      bill processing status i.e whether SUCCESS or FAILED
    transactionId	 string	      payment transaction id. returned only if payment is successful
    """

    transaction_data = (str(biller_code), str(bill_amount), str(payer_reference), str(partner_id))
    signed_data = signature(transaction_data)
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'signature': signed_data
    }
    payload = "{{\r\n" \
              "\"biller\":{{\r\n \"billerCode\":\"{0}\", \r\n \"countryCode\":\"{1}\", \r\n}}," \
              "\"bill\":{{\r\n \"reference\":\"{2}\", \r\n \"amount\":\"{3}\", \r\n \"currency\":\"{4}\", \r\n}}," \
              "\"payer\":{{\r\n \"name\":\"{6}\", \r\n \"account\":\"{7}\", \r\n \"reference\":\"{8}\", " \
              "\r\n \"mobileNumber\":\"{9}\", \r\n}}," \
              "\"partnerId\":\"{10}\"," \
              "\"remarks\":\"{11}\" \r\n}}".format(biller_code, country_code, bill_reference, bill_amount,
                                                   bill_currency, payer_name, payer_account, payer_account,
                                                   payer_reference, payer_mobile_number, partner_id, remarks)

    url = f"{settings.UAT_URL}/transaction/v2/bills/pay"
    response = post(url, payload=payload, headers=headers)
    data = json.loads(response.text)

    response_data = dict(
        token=token,
        ref=bill_reference,
        data=data
    )
    return response_data
