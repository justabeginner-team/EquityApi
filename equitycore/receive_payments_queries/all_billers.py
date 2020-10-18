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

    Example{
        "billers": [
            {
                "name": "INCULSIVITY",
                "code": "642292"
            },
            {
                "name": "I PAY",
                "code": "266300"
            },
            {
                "name": "MDUKA ONLINE",
                "code": "123456"
            },
            {
                "name": "ECITIZEN",
                "code": "967600"
            },
            {
                "name": "KPLC",
                "code": "6800001"
            },
            {
                "name": "test biller",
                "code": "400000"
            },
            {
                "name": "JAMBO PAY TRUSTEE ACCOUNT",
                "code": "147147"
            },
            {
                "name": "I PAY",
                "code": "300014"
            },
            {
                "name": "ZUKU",
                "code": "320320"
            },
            {
                "name": "WINGS TO FLY",
                "code": "344344"
            },
            {
                "name": "VIRTUAL MOBILE LIMITED",
                "code": "111111"
            },
            {
                "name": "A.C.K ST JAMES CHURCH BURUBURU",
                "code": "303030"
            },
            {
                "name": "MARY WAMBUI KAMANDE",
                "code": "389443"
            },
            {
                "name": "SAMUEL THURI GACHO",
                "code": "800589"
            },
            {
                "name": "JOHN MUHUNGI THURI",
                "code": "017019"
            },
            {
                "name": "BENCHMARK DISTRIBUTORS LIMITED",
                "code": "644443"
            },
            {
                "name": "EAZZY PAY ONLINE",
                "code": "900900"
            },
            {
                "name": "AZURI TECHNOLOGIES KENYA LIMITED",
                "code": "821055"
            }
        ]
    }

    """

    headers = {
        'Authorization': token,
    }

    payload = {}

    url = f"{settings.UAT_URL}/transaction/v2/billers?per_page={billers_per_page}&page={number_of_billers}"
    response = get(url, payload=payload, headers=headers)
    data = json.loads(response.text)

    return data
