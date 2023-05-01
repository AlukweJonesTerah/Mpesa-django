import requests
import keys
from requests.auth import HTTPBasicAuth


def generate_access_token():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    try:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        print(r.json())
    except:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret), verify=True)
        print(r.json())

    print(r.text)
    # extracting the access token from r.json()

    json_response = (r.json())  # {'access_token': 'orfE9Dun2qqCpuXsORjcWGzvrAIY', 'expires_in': '3599'}

    my_access_token = json_response['access_token']
    print(my_access_token)

    return my_access_token


generate_access_token()
