from django.conf import settings
import json
from ..http import get


def query_transaction(
        token: str,
        transaction_id: str,
):
    """
    This webservice enables an application or service to query a transactions details and status
    :param: token: the bearer token used to access the API
    :param: transaction_id: the payments unique reference/ transaction id
    :return: JSON response
    """
    payload = {}
    headers = {
        'Authorization': token,
    }

    url = f"{settings.UAT_URL}/transaction/v2/payments/details/{transaction_id}"
    response = get(url, payload=payload, headers=headers)
    data = json.loads(response.text)

    return data
