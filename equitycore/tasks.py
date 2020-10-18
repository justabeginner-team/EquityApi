from __future__ import absolute_import, unicode_literals
import celery.signals
import random
from celery import shared_task

from .receive_payments.eazzypaypush import eazzypay_push
from .receive_payments.lipanampesa import lipanampesa
from .receive_payments.merchant_payments import merchant_payments
from .receive_payments_queries.query_transaction_details import query_transaction
from .models import AuthToken


@celery.signals.worker_process_init.connect()
def seed_rng(**_):
    """
    Seeds the  random number generator.
    """
    random.seed()


@shared_task(name="reference_id")
def reference_id_generator(response):
    """
    generates a 12 digit random number with leading zeros 
    
    :returns: a string of 12 random unique digits from 000000000001 to 999999999999 with leading zeros i.e 000005678967
    """
    data=dict(
        ref_id="%0.12d" % random.randint(1, 999999999999),
        token=response
        )
    return data


@shared_task(name="bearer token")
def bearer_token_task():
    """
    Handle generation of accesstoken
    :return bearer token
    """
    return AuthToken.objects.getaccesstoken()


@shared_task(name="eazzypaypush_task", max_retries=10, acks_late=True)
def call_eazzypaaypush_task(
        response,
        pk,
        mssid,
        country_code,
        amount,
        trans_desc,
        
):
    """
    Handle eazzypaypush request
    :param response:
    :param trans_desc:
    :param country_code:
    :param mssid:
    :param amount:
    :return:
    """
    print(pk)
    print(response["ref_id"])
    return eazzypay_push(pk,response["token"], mssid, country_code, amount, trans_desc, response["ref_id"])


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
    :param trans_desc:
    :param country_code:
    :param response:
        > returned response content
          1. token

    :param mssid:
    :param amount:
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

@shared_task(name="merchant_payment")
def merchant_payment_task(
    response,
    partner_id,
    merchant_till,
    currency,
    amount,
    partner_reference,

):
    """
    Handle merchant request
    :param response from previous task in a sequence:
    :param partner_id:
    :param merchant_till:
    :param currency:
    :param amount:
    :param partner_reference:
    :return:
    """
    print(response["ref_id"])
    return merchant_payments(
        response["token"],
        merchant_till,
        response["ref_id"],
        amount,
        currency,
        partner_id,
        partner_reference,
        )
