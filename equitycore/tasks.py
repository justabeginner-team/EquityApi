from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .receive_payments.eazzypaypush import eazzypay_push
from .receive_payments.lipanampesa import lipanampesa
from .receive_payments_queries.query_transaction_details import query_transaction
from .models import AuthToken


@shared_task(name="bearer token", max_retries=10)
def bearer_token_task():
    """
    Handle generation of accesstoken
    :return bearer token
    """
    return AuthToken.objects.getaccesstoken()


@shared_task(name="eazzypaypush_task", max_retries=10)
def call_eazzypaaypush_task(
        response,
        mssid,
        country_code,
        amount,
        trans_desc,
        trans_ref
):
    """
    Handle eazzypaypush request
    :param mssid:
    :param country code:
    :param amount:
    :param transaction_description:
    :param transaction_reference:
    :return:
    """
    return eazzypay_push(response, mssid, country_code, amount, trans_desc, trans_ref)


@shared_task(name="lipa_na_mpesa_push")
def lipa_na_mpesapush_task(
        response,
        mssid,
        country_code,
        amount,
        trans_desc,
):
    """
    Handle eazzypaypush request
    :param response:
        > returned response content
          1. token

    :param mssid:
    :param country code:
    :param amount:
    :param transaction_description:
    :return:
        
    """
    return lipanampesa(response, mssid, country_code, amount, trans_desc)


@shared_task(name="query_transaction")
def query_transaction_task(
        response,
):
    """
    Handle transaction queries
    :param:response --- 
     > returned response content
          1. token 
          2. reference id
    """
    return query_transaction(response["token"], response["ref"])
