import requests
import keys
from access_token import generate_access_token
from requests.auth import HTTPBasicAuth


def register_url():
    my_access_token = generate_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {'Authorization': "Bearer %s" % my_access_token}
    request = {
               "ShortCode": keys.shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://mydomain.com/api/payments/c2b-confirmation/",
               "ValidationURL": "https://mydomain.com/api/payments/c2b-validation",
               }

    try:
        response = requests.post(api_url, json=request, headers=headers)

    except:
        response = requests.post(api_url, json=request, headers=headers, verify=False)

    print(response.text)


register_url()


def simulate_c2b_transaction():
    my_access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {'Authorization': "Bearer %s" % my_access_token}
    request = {
        "ShortCode": keys.shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "1",
        "Msisdn": keys.test_msisdn,
        "BillRefNumber": "123456789",
    }
    try:
        response = requests.post(api_url, json=request, headers=headers)
    except:
        response = requests.post(api_url, json=request, headers=headers, verify=True)
    print(response.text)


simulate_c2b_transaction()
