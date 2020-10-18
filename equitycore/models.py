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
    id = models.BigAutoField(
        primary_key=True)
    customer_country_code = models.CharField(
        max_length=3)
    customer_phone_number = models.BigIntegerField(
        blank=True, null=True)
    transaction_type = models.CharField(
        max_length=20, blank=True, null=True)
    api_transaction_reference = models.CharField(
        max_length=20, unique=False, null=True)
    transaction_reference = models.CharField(
        max_length=12, unique=False, null=False)

    transaction_amount = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    transaction_description = models.CharField(
        max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(
        auto_now_add=True)
    transaction_date = models.DateTimeField(null=True)
    paid = models.BooleanField(
        default=False)
    is_posted = models.BooleanField(default=False)
    transaction_status = models.CharField(
        blank=False, null=True, max_length=100)

    def __str__(self):
        return str(self.customer_phone_number)

    class Meta:
        db_table = "tbl_eazzypay_push"
        verbose_name_plural = "Eazzypaypush Requests"


class LipanampesaRequest(models.Model):
    """
        Handles LipaNaMpesaOnline push Requests
    """
    id = models.BigAutoField(primary_key=True)

    customer_phone_number = models.BigIntegerField(
        blank=True, null=True)
    customer_country_code = models.CharField(
        max_length=3)
    api_transaction_reference = models.CharField(
        max_length=20, unique=False, null=True)
    transaction_reference = models.CharField(
        max_length=12, unique=True, null=False)
    transaction_amount = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    transaction_description = models.CharField(
        max_length=50, blank=True, null=True)
    transaction_date = models.DateTimeField(
        null=True)
    transaction_status = models.CharField(
        blank=False, max_length=100)
    date_added = models.DateTimeField(
        auto_now_add=True)
    paid = models.BooleanField(
        default=False)

    def __str__(self):
        return str(self.customer_phone_number)

    class Meta:
        db_table = "tbl_lipanampesaonline_push"
        verbose_name_plural = "LipaNaMpesaOnline Requests"


class MerchantRequest(models.Model):
    """
        Handles Merchants Requests
    """
    id = models.BigAutoField(primary_key=True)

    partner_id = models.BigIntegerField(
        blank=True, null=True)
    merchant_till = models.CharField(
        max_length=12, null=False)
    currency = models.CharField(
        max_length=4)
    partner_reference = models.CharField(max_length=15)
    api_transaction_reference = models.CharField(
        max_length=20, unique=False, null=True)
    transaction_reference = models.CharField(
        max_length=12, unique=False, null=False)
    transaction_amount = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    transaction_date = models.DateTimeField(
        null=True)
    transaction_status = models.CharField(
        blank=False, max_length=100)
    date_added = models.DateTimeField(
        auto_now_add=True)
    is_posted = models.BooleanField(default=False)
    paid = models.BooleanField(
        default=False)

    def __str__(self):
        return str(self.partner_id)

    class Meta:
        db_table = "tbl_merchant_payment"
        verbose_name_plural = "Merchant Requests"


class BillPaymentRequest(models.Model):
    """Handles Bill Payments"""
    id = models.BigAutoField(primary_key=True)
    biller_code = models.CharField(
        max_length=12, null=False)
    country_code = models.CharField(
        max_length=3)
    bill_reference = models.CharField(
        max_length=12, null=False)  # same as payer_account
    bill_amount = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    bill_currency = models.CharField(
        max_length=4)
    payer_name = models.CharField(max_length=60)
    payer_reference = models.CharField(
        max_length=12, unique=False, null=False)
    payer_mobile_number = models.CharField(
        max_length=12, null=False)
    partner_id = models.BigIntegerField(
        blank=True, null=True)
    remarks = models.TextField()
    transaction_date = models.DateTimeField(
        null=True)
    transaction_status = models.CharField(
        blank=False, max_length=100)
    date_added = models.DateTimeField(
        auto_now_add=True)
    api_transaction_reference = models.CharField(
        max_length=20, unique=False, null=True)
    is_posted = models.BooleanField(default=False)
    paid = models.BooleanField(
        default=False)

    def __str__(self):
        return str(self.partner_id)

    class Meta:
        db_table = "tbl_bill_payments"
        verbose_name_plural = "Bill Payment Requests"


class BillValidationRequest(models.Model):
    """Handles Bill Validation Request"""
    id = models.BigAutoField(primary_key=True)
    biller_code = models.CharField(
        max_length=12, null=False)
    customer_reference_number = models.CharField(
        max_length=12, null=False)
    bill_amount = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    bill_currency = models.CharField(
        max_length=4)
    date_added = models.DateTimeField(
        auto_now_add=True)
    transaction_date = models.DateTimeField(
        null=True)
    is_posted = models.BooleanField(default=False)
    validated = models.BooleanField(
        default=False)

    def __str__(self):
        return str(self.customer_reference_number)

    class Meta:
        db_table = "tbl_bill_validation"
        verbose_name_plural = "Bill Validation Requests"
