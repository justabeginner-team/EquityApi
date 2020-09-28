from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .receive_payments.eazzypaypush import eazzypay_push


@shared_task(name="eazzypaypush_task")
def call_eazzypaaypush_task(
    mssid,
    country_code,
    amount,
    trans_desc
    ):
    """
    Handle eazzypaypush request
    :param mssid:
    :param country code:
    :param amount:
    :param transaction_description:
    :return:
    """
    return eazzypay_push(mssid,country_code,amount,trans_desc)