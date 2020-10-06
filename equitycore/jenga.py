from .models import EazzyPushRequest,LipanampesaRequest

class Jenga:

    @staticmethod
    def eazzypaypush(phone,country_code,amount,trans_ref):
        """
        Initiates Eazzy Push transaction
        :param phone: user phone to start the Eazzy push e.g. 0765******
        :param amount: amount to be deducted from the users account wallet
        :param country_code:country code from which the initiator has registered their account
        :param trans_desc: the message that get shown to the user on the checkout USSD message
        :return: EazzyPushRequest object
        """
       
        return EazzyPushRequest.objects.create(
            customer_phone_number= phone,
            customer_country_code= country_code,
            transaction_amount=amount,
            transaction_description= trans_ref,
        )

    @staticmethod
    def lipanampesapush(phone, country_code, amount, trans_desc):
        """
        Initiates Eazzy Push transaction
        :param phone: user phone to start the Eazzy push e.g. 0765******
        :param amount: amount to be deducted from the users account wallet
        :param country_code:country code from which the initiator has registered their account
        :param trans_desc: the message that get shown to the user on the checkout USSD message
        :return: EazzyPushRequest object
        """

        return LipanampesaRequest.objects.create(
            customer_phone_number=phone,
            customer_country_code=country_code,
            transaction_amount=amount,
            transaction_description=trans_desc,
        )
