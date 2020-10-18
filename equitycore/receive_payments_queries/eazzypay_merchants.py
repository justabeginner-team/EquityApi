from django.conf import settings
import json

from ..http import get


def get_merchants(
        token,
        number_of_pages,
        merchants_per_page
):
    """
    This webservice returns all EazzyPay merchants .

    :param token: the bearer token used to access the API
    :param number_of_pages: specify the number of pages to return
    :param merchants_per_page: the number of merchants to return per page
    :return: 200 Success Response
    Field Name	                    Field Type	    Field Description
    merchant	                    array	        merchants list
    merchant.name	                string	        merchant name
    merchant.tillnumber	            string	        merchant till number
    merchant.outlets	            array	        outlets list
    merchants.outlets.name	        string	        merchant outlet name
    merchants.outlets.tillnumber	string	        merchant outlet till number
    """

    headers = {
        'Authorization': token,
    }

    payload = {}

    url = f"{settings.UAT_URL}/transaction/v2/merchants?per_page={merchants_per_page}&page={number_of_pages}"
    response = get(url, payload=payload, headers=headers)
    data = json.loads(response.text)

    return data
