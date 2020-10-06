import json
from django.conf import settings
from ..http import post
from ..utils.jengautils import signature
from ..models import LipanampesaRequest

def lipanampesa(
    token: str,
    mssid: int,
    countryCode: str,
    trans_amount: int,
    trans_desc: str,
):


    businessnumber = "174379"
    trans_ref = "ref"
    
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'  
    }
    payload = "{{\r\n   \"customer\": {{\r\n      \"mobileNumber\": \"{0}\",\r\n      \"countryCode\": \"{1}\"\r\n   }},\r\n   \"transaction\": {{\r\n      \"amount\": \"{2}\",\r\n      \"description\": \"{3}\",\r\n      \"businessNumber\": \"{4}\",\r\n      \"reference\": \"{5}\"\r\n   }}\r\n}}".format(
        str(mssid), countryCode, str(trans_amount), trans_desc, businessnumber, trans_ref )
    
    url = f"{settings.UAT_URL}/transaction/v2/payment/mpesastkpush"

    response = post(url, headers=headers, payload=payload)
    data=json.loads(response.text)
    
    LipanampesaRequest.objects.update(transaction_reference=data.get("transactionRef"),transaction_status=data.get("status"))
    return payload
