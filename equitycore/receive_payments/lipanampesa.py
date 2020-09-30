from ..http import post
from ..utils.jengautils import signature


def lipanampesa(
    token: str,
    mssid: int,
    countryCode: str,
    trans_amount: int,
    trans_desc: str,
):

    

    businessnumber = 174379
    trans_ref = "ref"
    
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        
    }
    payload = {
        "customer": {
            "mobileNumber": "0711521508",
            "countryCode": "KE"
        },
        "transaction": {
            "amount": str(trans_amount),
            "description": trans_desc,
            "businessNumber": "174379",
            "reference": "ref"
        }
    }
    url = "https://uat.jengahq.io/transaction-test/v2mk/payment/mpesastkpush"
    response = post(url, headers=headers, payload=payload)
    return response.text
