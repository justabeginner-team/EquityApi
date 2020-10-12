from django.conf import settings
import json
from ..http import post


def get_forex_rates(
        token,
        country_code,
        currency_code
):
    """
    The Foreign Exchange Rates API Provides Easy Access To The Equity Bank Daily Currency Conversion Rate For Major Currencies

    :param token: the bearer token used to access the API
    :param country_code: the country for which rates are being requested. Valid values are KE, TZ, UG, RW.
    :param currency_code: he currency code of the currency that is being converted from in ISO 4217 format
    :return: Response schema
    Field Name	    Field Type	Field Descriptions
    currencyRates	list	    list of conversion rates for major currencies
    fromCurrency	string	    the currency code of the currency that is being converted from
    rate	        double	    the conversion rate
    toCurrency	    string	    the currency code of the currency that is being converted to
    """

    payload = "{{\r\n" \
              " \"countryCode\": \"{0}\"," \
              "\"currencyCode\": \"{1}\"," \
              " \r\n}}".format(country_code, currency_code)

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }

    url = f"{settings.UAT_URL}/transaction/v2/foreignexchangerates"

    response = post(url, headers=headers, payload=payload)
    data = json.loads(response.text)
    return data
