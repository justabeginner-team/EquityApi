from .models import EazzyPushRequest, LipanampesaRequest,MerchantRequest
import equitycore.exceptions  as exceptions


class Jenga:

    @staticmethod
    def eazzypaypush(
        phone, 
        country_code, 
        amount, 
        trans_desc
        ):
        """
        Initiates Eazzy Push transaction
        :param phone: user phone to start the Eazzy push e.g. 0765******
        :param amount: amount to be deducted from the users account wallet
        :param country_code:country code from which the initiator has registered their account
        :param trans_desc: the message that get shown to the user on the checkout USSD message
        :return: EazzyPushRequest object
        """

        try:
            EazzyPushRequest.objects.create(
                customer_phone_number=phone,
                customer_country_code=country_code,
                transaction_amount=amount,
                transaction_description=trans_desc,
                # transaction_reference=trans_ref
            )
        except Exception as ex:
            raise exceptions.EazzyPayPushError(str(ex))

    @staticmethod
    def lipanampesapush(
        phone, 
        country_code, 
        amount, 
        trans_desc
        ):
        """
        Initiates Eazzy Push transaction
        :param phone: user phone to start the Eazzy push e.g. 0765******
        :param amount: amount to be deducted from the users account wallet
        :param country_code:country code from which the initiator has registered their account
        :param trans_desc: the message that get shown to the user on the checkout USSD message
        :return: EazzyPushRequest object
        """

        try:
            LipanampesaRequest.objects.create(
                customer_phone_number=phone,
                customer_country_code=country_code,
                transaction_amount=amount,
                transaction_description=trans_desc,
            )
        except Exception as ex:
            raise exceptions.MpesaStkPushError(str(ex))

    @staticmethod
    def merchant(
        cust_phone,
        merchant_till,
        currency, 
        amount,
        account_number="0011547896523",
        ):
        """
        
        """

        try:
            MerchantRequest.objects.create(
                    partner_id=str(account_number),
                    partner_reference=cust_phone,
                    transaction_amount=amount,
                    currency=currency,
                    merchant_till=merchant_till,
                )
        except Exception as ex:
            raise exceptions.MpesaStkPushError(str(ex))
