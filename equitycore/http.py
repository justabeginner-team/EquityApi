import requests


def post(url, headers, payload):
    """
    Post a request to a given url
    :param url:
    :param headers:
    :param payload:
    :return:
    
    """
    response = requests.request("POST", url=url, data=payload, headers=headers)

    return response



