from django.conf import settings
import json

from ..http import get


def get_all_billers(
        token,
        number_of_billers,
        billers_per_page
):
    """
    This web service returns a paginated list of all billers

    :param token: the bearer token used to access the API
    :param number_of_billers: specify the number of billers to return
    :param billers_per_page: the number of billers to return per page
    :return:
    Field Name	    Field Type	    Field Description
    billers	        array	        biller array
    billers.name	string	        biller name
    billers.code	string	        biller code
    """

    headers = {
        'Authorization': token,
    }

    payload = {}

    url = f"{settings.UAT_URL}/transaction/v2/billers?per_page={billers_per_page}&page={number_of_billers}"
    response = get(url, payload=payload, headers=headers)
    data = json.loads(response.text)

    return data
