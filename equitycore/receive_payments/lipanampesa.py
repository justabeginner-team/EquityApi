import json
from django.conf import settings
from ..http import post
from ..utils.jengautils import signature
from ..models import LipanampesaRequest
from ..helpers import reference_id_generator


def lipanampesa(
        token: str,
        mssid: int,
        countryCode: str,
        trans_amount: int,
        trans_desc: str,
):
    """
      Initiates a Lipa na Mpesa stkpush request

      :param: token:
      :param: mssid:
      :param: CountryCode:
      :param: trans_amount:
      :param: trans_desc:
      :return: response that gets transaction reference from the api if successful
      """

    business_number = "174379"
    trans_ref = reference_id_generator()

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    payload = "{{\r\n   \"customer\": {{\r\n      \"mobileNumber\": \"{0}\",\r\n      \"countryCode\": \"{1}\"\r\n   " \
              "}},\r\n   \"transaction\": {{\r\n      \"amount\": \"{2}\",\r\n      \"description\": \"{3}\"," \
              "\r\n      \"businessNumber\": \"{4}\",\r\n      \"reference\": \"{5}\"\r\n   }}\r\n}}".format(
        str(mssid), countryCode, str(trans_amount), trans_desc, business_number, trans_ref)

    url = f"{settings.UAT_URL}/transaction/v2/payment/mpesastkpush"

    response = post(url, headers=headers, payload=payload)
    data = json.loads(response.text)

    LipanampesaRequest.objects.update(api_transaction_reference=data.get("transactionRef"),
                                      transaction_reference=trans_ref, transaction_status=data.get("status"))
    return data.get("transactionRef")
