from .models import EazzyPushRequest, LipanampesaRequest, MerchantRequest, BillPaymentRequest
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
    def merchant_payment(
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
            raise exceptions.MerchantError(str(ex))
    
    @staticmethod
    def billpayment(
        biller_code,
        country_code,
        bill_ref,
        bill_amount,
        bill_currency,
        payer_name,
        payer_account,
        payer_mobile_number,
        remarks,
        partner_id="0011547896523",
        
    ):
        """
        Provides Partners the Capability To Initiate Utility Bill Payments For Goods And Services
        
        :param: biller_code: the business number. e.g for ZUKU 32030 is the business number
        :param: country_code: country of the biller account
        :param: bill_reference: invoice/ref number against which the bill will be paid 111222
        :param: bill_amount: amount of bill to be paid
        :param: bill_currency: currency code of the payment amount in ISO 4217 e.g KES
        :param: payer_name: name of the person making the payment e.g A N.Other
        :param: payer_account: invoice/ref number against which the bill will be paid. same as bill reference e.g 111222
        :param: payer_reference: A unique 12 digit string and it is the payer's reference
        :param: payer_mobile_number: payer mobile number e.g 0763000000
        :param: partner_id: partner identifier. This will always be the bank account maintained in jengaHQ
        for BILL PAYMENT APIs e.g 0011547896523
        :param: remarks: remarks of the bill payment
        """
        try:
            BillPaymentRequest.objects.create(
                biller_code=biller_code,
                country_code=country_code,
                bill_reference=bill_ref,
                bill_amount=bill_amount,
                bill_currency=bill_currency,
                payer_account=bill_ref,
                payer_name=payer_name,
                remarks=remarks,
                partner_id=partner_id,
                payer_mobile_number=payer_mobile_number
            )
        except Exception as e:
            raise exceptions.BillError(str(e))    
