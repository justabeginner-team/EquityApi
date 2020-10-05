
import json
import requests
import base64
import os
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from django.conf import settings
from django.http import HttpResponse

# in app imports
from .models import AuthToken
#from .utils.jengautils import get_token, signature
from equitycore.receive_payments.eazzypaypush import eazzypay_push
from .jenga import Jenga
from .http import post


def get_token():
    """
    fetch a new token
    :param: type:
    :return: JSON
    """

    url = "https://uat.jengahq.io/identity/v2/token"
    payload = dict(
        username="#####",
        password="#####",
    )

    headers = {
        "authorization": "@@@@@@@@@",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = post(url, payload=payload, headers=headers)
    print(response.text)
    return json.loads(response.text)
   


def signature(requestfields):
    """
    Build a String of concatenated values of the request fields with
    following order: 
     as specificied by the API endpoints

    ::The resulting text is then signed with Private Key and Base64 encoded  to proof that this request is coming from the merchant.
    ::Takes a tuple of request fields in the order that they should be
    concatenated, hashes them with SHA-256, signs the resulting hash and
    ::returns a Base64 encoded string of the resulting signature
    
    """

    data_concat = "".join(requestfields).encode("utf-8")
    digest = SHA256.new()
    digest.update(data_concat)

    
    with open(os.path.join(os.getcwd(), ".JengaApi", "keys", "privatekey.pem"), "r") as pk:
        private_key = RSA.importKey(pk.read())

    signer = PKCS1_v1_5.new(private_key)
    return base64.b64encode(signer.sign(digest))


def accesstoken(request):
    token = get_token().get("access_token")

    url = "https://uat.jengahq.io/transaction/v2/foreignexchangerates"

    ke = "KE"
    payload = "{{\r\n   \"countryCode\": \"{0}\",\r\n   \"currencyCode\": \"{1}\"\r\n}}".format(ke,"USD")

    print(payload)

    headers = {
        'Authorization': 'Bearer '+token,
        'Content-Type': 'application/json'
    }
   
    response = requests.request("POST", url, headers=headers, data=payload)

    print(json.loads(response.text))

    return HttpResponse(json.loads(response.text))
