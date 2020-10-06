import base64

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

import requests
import json
from django.conf import settings

from ..http import post
from ..helpers import pk_path as pkey_path


def get_token():
    """
    fetch a new token
    :param: type:
    :return: JSON
    """

    url = f"{settings.UAT_URL}/identity/v2/token"
    payload = dict(
        username=settings.MERCHANT_CODE,
        password=settings.PASSWORD,
    )

    headers = {
        "authorization": f"{settings.API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = post(url, payload=payload, headers=headers)

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

    private_key = False
    with open(pkey_path(), "r") as pk:
        private_key = RSA.importKey(pk.read())

    signer = PKCS1_v1_5.new(private_key)
    return base64.b64encode(signer.sign(digest))
