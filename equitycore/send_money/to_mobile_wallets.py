import json
from django.conf import settings

from ..http import post
from ..utils.jengautils import signature


def sign_data(wallet_name, transfer_amount, transfer_currency_code, transfer_reference, source_account_number):
    """
    Generates a signature depending on the wallet name
    :param wallet_name:
    :param transfer_amount:
    :param transfer_currency_code:
    :param transfer_reference:
    :param source_account_number:
    :return:
    """
    if wallet_name == 'Airtel' or wallet_name == 'Mpesa':
        transaction_data = (str(transfer_amount), str(transfer_currency_code), str(transfer_reference),
                            str(source_account_number))

    elif wallet_name == 'Equitel':
        # Handle signature for transfer to Equitel
        transaction_data = (str(source_account_number), str(transfer_amount),
                            str(transfer_currency_code), str(transfer_reference))

    signed_data = signature(transaction_data)

    return signed_data


def to_mobile_wallets(
        token,
        source_country_code,
        source_name,
        source_account_number,
        destination_type,
        destination_country_code,
        destination_name,
        destination_mobile_number,
        destination_wallet_name,
        transfer_type,
        transfer_amount,
        transfer_currency_code,
        transfer_reference,
        transfer_date,
        transfer_description
):
    """

    :param token:
    :param source_country_code:
    :param source_name:
    :param source_account_number:
    :param destination_type:
    :param destination_country_code:
    :param destination_name:
    :param destination_mobile_number:
    :param destination_wallet_name:
    :param transfer_type:
    :param transfer_amount:
    :param transfer_currency_code:
    :param transfer_reference:
    :param transfer_date:
    :param transfer_description:
    :return: Success Response
    Field Name	    Field Type	Field Description
    transactionId	string	    unique transaction id
    status	        string	    transaction status

    Example
    {
        "transactionId": "45865",
        "status": "SUCCESS"
    }
    """

    signed_data = sign_data(wallet_name=destination_wallet_name, transfer_amount=transfer_amount,
                            transfer_currency_code=transfer_currency_code, transfer_reference=transfer_reference,
                            source_account_number=source_account_number)

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
              "\"type\":\"{3}\", \r\n \"countryCode\":\"{4}\", \r\n \"name\":\"{5}\", \r\n \"mobileNumber\":\"{6}\"," \
              " \r\n \"walletName\":\"{7}\", \r\n}}," \
              "\"transfer\":{{\r\n " \
              "\"type\":\"{8}\", \r\n \"amount\":\"{9}\", \r\n \"currencyCode\":\"{10}\", \r\n \"reference\":\"{11}\"," \
              "\r\n \"date\":\"{12}\" , \r\n \"description\":\"{13}\"" \
              "\r\n}}" \
              "\r\n}}".format(source_country_code, source_name, source_account_number, destination_type,
                              destination_country_code, destination_name, destination_mobile_number,
                              destination_wallet_name, transfer_type, transfer_amount, transfer_currency_code,
                              transfer_reference, transfer_date, transfer_description)

    url = f"{settings.UAT_URL}/transaction/v2/identity/remittance"
    response = post(url, payload=payload, headers=headers)
    data = json.loads(response.text)

    return data
