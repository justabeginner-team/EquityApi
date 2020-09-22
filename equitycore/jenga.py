import requests
import json
from django.conf import settings
from .http import post

def get_token():
    """
    fetch a new token
    :param: type:
    :return: JSON
    """

    url = f"{settings.SANDBOX_URL}/identity/v2/token"
    payload = dict(username=settings.MERCHANT_CODE, password=settings.PASSWORD)
    
    headers = {
        "authorization": f"{settings.API_KEY}",
         }

    response = post(url, payload=payload, headers=headers)
    token=json.loads(response.text)
    return token
