
from django.contrib import admin
from .models import AuthToken,EazzyPushRequest,LipanampesaRequest
from rangefilter.filter import DateRangeFilter

class AuthTokenAdmin(admin.ModelAdmin):
    readonly_fields=('access_token','expires_in')


admin.site.register(AuthToken,AuthTokenAdmin)

@admin.register(EazzyPushRequest)
class EazzyPushRequestAdmin(admin.ModelAdmin):
    list_display = ("customer_phone_number",
                    "transaction_amount", "date_added", "transaction_date")
    readonly_fields = (
        "customer_phone_number",
        "transaction_amount",
        "customer_country_code",
        "transaction_type",
        "transaction_reference",
        "transaction_description",
        "transaction_date",
        "date_added",
    )
    search_fields = ("customer_phone_number",
                     "transaction_amount", "date_added", "transaction_date","customer_country_code")
    list_filter = (("date_added", DateRangeFilter),
                   ("transaction_date", DateRangeFilter),)


@admin.register(LipanampesaRequest)
class LipaNaMpesaRequestAdmin(admin.ModelAdmin):
    list_display = ("customer_phone_number",
                    "transaction_amount", "date_added", "transaction_date")
    readonly_fields = (
        "customer_phone_number",
        "transaction_amount",
        "customer_country_code",
        
        "transaction_reference",
        "transaction_description",
        "transaction_date",
        "date_added",
        "transaction_status",
    )
    search_fields = ("customer_phone_number",
                     "transaction_amount", "date_added", "transaction_date", "customer_country_code")
    list_filter = (("date_added", DateRangeFilter),
                   ("transaction_date", DateRangeFilter),)
