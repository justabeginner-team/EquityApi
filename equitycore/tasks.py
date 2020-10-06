from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .receive_payments.eazzypaypush import eazzypay_push
from  .receive_payments.lipanampesa import lipanampesa
from .models import AuthToken

@shared_task(name="bearer token")
def bearer_token_task():
    """
    Handle generation of accesstoken
    :return bearer token
    """
    return AuthToken.objects.getaccesstoken()



@shared_task(name="eazzypaypush_task")
def call_eazzypaaypush_task(
    response,
    mssid,
    country_code,
    amount,
    trans_desc,
    ):
    """
    Handle eazzypaypush request
    :param mssid:
    :param country code:
    :param amount:
    :param transaction_description:
    :return:
    """
    return eazzypay_push(response,mssid,country_code,amount,trans_desc)

@shared_task(name="lipa_na_mpesa_push")
def lipa_na_mpesapush_task(
    response,
    mssid,
    country_code,
    amount,
    trans_desc,
    ):
    #mssid="0"+mssid

    return lipanampesa(response,mssid,country_code,amount,trans_desc)

