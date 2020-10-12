import json
from django.conf import settings

from ..http import post
from ..utils.jengautils import signature


def to_rtgs(
        token,
        source_country_code,
        source_name,
        source_account_number,
        destination_type,
        destination_country_code,
        destination_name,
        destination_bank_code,
        destination_account_number,
        transfer_type,
        transfer_amount,
        transfer_currency_code,
        transfer_reference,
        transfer_date,
        transfer_description
):
    """
    This API Can Move Funds Within Equity Bank Across Kenya, Uganda, Tanzania, Rwanda & South Sudan

    :param token: the bearer token used to access the API
    :param source_country_code: the sender's ISO country code
    :param source_name: sender's full name
    :param source_account_number: the sender's account number
    :param destination_type: the recipient's store of value. In this case its bank
    :param destination_country_code: the recipient's country code
    :param destination_name: the recipient's full name
    :param destination_bank_code: recipient's bank code e.g 09
    :param destination_account_number: the recipient's bank account number.
    :param transfer_type: the transfer type. In this case its RTGS
    :param transfer_amount: the amount to transfer.  Maximum is USD 10,000 or its currency equivalent per transaction
    :param transfer_currency_code: the amount's ISO currency
    :param transfer_reference: A unique 12 digit string and it is the transaction reference
    :param transfer_date: the transfer date ISO 8601 date format 'YYYY-MM-DD'
    :param transfer_description: any additional information the sender would like to add
    :return: Response schema
    Field Name	    Field Type	Field Description
    transactionId	string	    unique transaction id
    status	        string	    transaction status

    Example
    {
        "transactionId": "000000403777",
        "status": "SUCCESS"
    }
    """

    transaction_data = (str(transfer_reference), str(transfer_date),
                        str(source_account_number), str(destination_account_number), str(transfer_amount))
    signed_data = signature(transaction_data)

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'signature': signed_data
    }

    payload = "{{\r\n" \
              "\"source\":{{\r\n " \
              "\"countryCode\":\"{0}\", \r\n \"name\":\"{1}\", \r\n \"accountNumber\":\"{2}\", " \
              "\r\n}}," \
              "\"destination\":{{\r\n " \
              "\"type\":\"{3}\", \r\n \"countryCode\":\"{4}\", \r\n \"name\":\"{5}\", \r\n \"bankCode\":\"{6}\"," \
              " \r\n \"accountNumber\":\"{7}\" \r\n}}," \
              "\"transfer\":{{\r\n " \
              "\"type\":\"{8}\", \r\n \"amount\":\"{9}\", \r\n \"currencyCode\":\"{10}\", \r\n \"reference\":\"{11}\"," \
              "\r\n \"date\":\"{12}\" , \r\n \"description\":\"{13}\"" \
              "\r\n}}" \
              "\r\n}}".format(source_country_code, source_name, source_account_number, destination_type,
                              destination_country_code, destination_name, destination_bank_code,
                              destination_account_number, transfer_type,
                              transfer_amount, transfer_currency_code, transfer_reference,
                              transfer_date, transfer_description)

    url = f"{settings.UAT_URL}/transaction/v2/identity/remittance"
    response = post(url, payload=payload, headers=headers)
    data = json.loads(response.text)

    return data
