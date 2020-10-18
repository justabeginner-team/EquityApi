from django.dispatch import receiver
from celery import chain, chord
from django.db.models.signals import post_save
from .models import (
    EazzyPushRequest,
    LipanampesaRequest,
    MerchantRequest
)
from .tasks import (
    call_eazzypaaypush_task,
    bearer_token_task,
    lipa_na_mpesapush_task,
    query_transaction_task,
    reference_id_generator,
    merchant_payment_task,
)


@receiver(post_save, sender=EazzyPushRequest)
def handle_eazzypaypush_post_save(sender, instance, **Kwargs):
    chain(
        bearer_token_task.s(),
        reference_id_generator.s(),
        call_eazzypaaypush_task.s(
            instance.id,
            str(instance.customer_phone_number),
            instance.customer_country_code,
            str(instance.transaction_amount),
            instance.transaction_description,
            # instance.transaction_reference
        ),
        query_transaction_task.s(),
    ).apply_async(queue="eazzypaypush_request")


@receiver(post_save, sender=LipanampesaRequest)
def handle_lipa_na_mpesa_post_save(sender, instance, **Kwargs):
    chain(
        bearer_token_task.s(),
        lipa_na_mpesapush_task.s(
            str(instance.customer_phone_number),
            instance.customer_country_code,
            str(instance.transaction_amount),
            instance.transaction_description,
        ),
    ).apply_async(queue="lipanampesa_request")


@receiver(post_save, sender=MerchantRequest)
def handle_merchant_request(sender, instance, **Kwargs):
    chain(
        bearer_token_task.s(),
        reference_id_generator.s(),
        merchant_payment_task.s(
            str(instance.partner_id),
            str(instance.merchant_till),
            str(instance.currency),
            str(instance.transaction_amount),
            str(instance.partner_reference),
        )
    ).apply_async(queue="merchant_request")
