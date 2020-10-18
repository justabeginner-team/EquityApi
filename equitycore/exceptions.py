class BaseError(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EazzyPayPushError(BaseError):
    """ exception raised from eazzypaypush request"""
    pass

class MpesaStkPushError(BaseError):
    """ exception raised from mpesastk push request"""
    pass

class MerchantError(BaseError):
    """ exception raised from merchant payment error"""
    pass

class BillError(BaseError):
    """ exception raised from bill payment error"""
    pass
