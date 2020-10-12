from django.conf import settings
import json
from ..http import post
from ..utils.jengautils import signature

merchant_code = settings.MERCHANT_CODE


def verify_identity(
        token,
        document_type,
        first_name,
        last_name,
        date_of_birth,
        document_number,
        country_code
):
    """
    This web service enables your application to query the various registrar of persons in the various countries
    in East Africa. Currently available for Kenya and Rwanda only.

    :param token: the bearer token used to access the API
    :param document_type: the document type of the customer. for example ID, PASSPORT, ALIENID
    :param first_name: first name as per identity document type
    :param last_name: last name as per identity document type
    :param date_of_birth: date in YYYY-MM-DD format
    :param document_number: the document id number i.e 25632548
    :param country_code: the country in which the document relates to (only KE and RW enabled for now)
    :return: Response Schema
    Field Name	                                Field Type	Field Description
    identity	                                object	    identity object
    identity.customer	                        object	    customer object
    customer.fullName	                        string	    full name
    customer.firstName	                        string	    first name
    customer.lastName	                        string	    last name
    customer.shortName	                        string	    short name
    customer.birthDate	                        string	    birth date
    customer.birthCityName	                    string	    birth city name
    customer.deathDate	                        string	    death date
    customer.gender	                            string	    gender
    customer.faceImage	                        string	    face image
    customer.occupation	                        string	    occupation
    customer.nationality	                    string	    nationality
    documentType	                            string	    identity document type
    documentNumber	                            string	    identity document number
    identity.documentSerialNumber	            string	identity document serial number
    documentExpirationDate	                    string	identity document expiration date
    documentIssuingLocation	                    string	identity document issuing location
    documentIssueDate	                        string	identity document issuing date
    issuedBy	                                string	identity document issuing authorit
    identity.additionalIdentityDetails	        array	additional identity documents array
    additionalIdentityDetails.documentNumber	string	identity document number
    additionalIdentityDetails.documentType	    string	identity document type
    additionalIdentityDetails.issuedBy	        string	identity document issuing authority
    identity.address	                        object	address
    address.provinceName	                    string	province name
    address.districtName	                    string	district name
    address.locationName	                    string	location name
    address.subLocationName	                    string	sub-location name
    address.villageName	                        string	village name

    Example
    {
        "identity": {
            "customer": {
                "fullName": "John Doe ",
                "firstName": "John",
                "middlename": "",
                "lastName": "Doe",
                "ShortName": "John",
                "birthDate": "1900-01-01T00:00:00",
                "birthCityName": "",
                "deathDate": "",
                "gender": "",
                "faceImage": "/9j/4AAQSkZJRgABAAEAYABgA+H8qr6n4e1O71SGFbV/sEOF3O6/N/eb71d/FGkaBVXaq9KfRRRRRUMsKSIdyr0r/9k=",
                "occupation": "",
                "nationality": "Refugee"
            },
            "documentType": "ALIEN ID",
            "documentNumber": "654321",
            "documentSerialNumber": "100500425",
            "documentIssueDate": "2002-11-29T12:00:00",
            "documentExpirationDate": "2004-11-28T12:00:00",
            "IssuedBy": "REPUBLIC OF KENYA",
            "additionalIdentityDetails": [
                {
                    "documentNumber": "",
                    "documentType": "",
                    "issuedBy": ""
                }
            ],
            "address": {
                "provinceName": " ",
                "districtName": "",
                "locationName": "",
                "subLocationName": "",
                "villageName": ""
            }
        }
    }
    """

    transaction_data = (merchant_code, str(document_number), str(country_code))
    signed_data = signature(transaction_data)
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'signature': signed_data
    }

    payload = "{{\r\n" \
              "\"identity\":{{\r\n " \
              "\"documentType\":\"{0}\", \r\n \"firstName\":\"{1}\", \r\n \"lastName\":\"{2}\", " \
              "\r\n \"dateOfBirth\":\"{3}\", \r\n \"documentNumber\":\"{4}\", \r\n \"countryCode\":\"{5}\", \r\n}}" \
              "\r\n}}".format(document_type, first_name, last_name, date_of_birth, document_number, country_code)

    url = f"{settings.UAT_URL}/transaction/v2/identity/verify"
    response = post(url, payload=payload, headers=headers)
    data = json.loads(response.text)

    return data
