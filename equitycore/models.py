from django.db import models
from .managers import AuthTokenManager


class AuthToken(models.Model):
    access_token = models.CharField(max_length=40)
    expires_in = models.BigIntegerField()
    objects = AuthTokenManager()

    def __str__(self):
        return "access token"


class EazzyPushRequest(models.Model):
    """
        Handles EazzyPay push Requests
    """
    id = models.BigAutoField(primary_key=True)
    customer_country_code = models.CharField(max_length=2)
    customer_phone_number = models.BigIntegerField(blank=True, null=True)
    transaction_type = models.CharField(max_length=20, blank=True, null=True)
    transaction_reference = models.CharField(max_length=20, unique=True)
    transaction_date = models.DateTimeField( null=True)
    transaction_amount = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    transaction_description = models.CharField(
        max_length=50, blank=True, null=True )
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer_phone_number)

    class Meta:
        db_table = "tbl_eazzypay_push"
        verbose_name_plural = "Eazzypaypush Requests"
