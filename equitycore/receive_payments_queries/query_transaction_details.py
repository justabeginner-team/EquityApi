from django.conf import settings
import json
from ..http import post


def query_transaction(
        token: str,
        transaction_id: str,
):
    """
    This webservice enables an application or service to query a transactions details and status
    :param: token: the bearer token used to access the API
    :param: transaction_id: the payments unique reference/ transaction id
    :return: JSON
    """

    headers = {
        'Authorization': f'Bearer {token}',
        }

    url = f"{settings.UAT_URL}/transaction/v2/payments/details/{transaction_id}"
    response = post(url, headers=headers)
    data = json.loads(response.text)

    return data
