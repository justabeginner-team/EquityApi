from django.dispatch import receiver
from celery import chain
from django.db.models.signals import post_save
from .models import EazzyPushRequest
from .tasks import call_eazzypaaypush_task


@receiver(post_save,sender=EazzyPushRequest)
def handle_eazzypaypush_post_save(sender,instance,**Kwargs):
    chain(
        call_eazzypaaypush_task.s(
            str(instance.customer_phone_number),
            instance.customer_country_code,
            str(instance.transaction_amount),
            instance.transaction_reference,
        ),
    ).apply_async(queue="eazzypaypush_request")
