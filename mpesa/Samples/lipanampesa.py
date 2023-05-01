import requests
from requests.auth import HTTPBasicAuth
import keys
from access_token import generate_access_token
from mpesa_encode import generate_password
from utils import get_timestamp

formatted_time = get_timestamp()
decoded_password = generate_password(formatted_time)
print(generate_access_token())


def lipa_na_mpesa():
    access_token = generate_access_token(),
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer %s" % access_token
    }

    request = {
        "BusinessShortCode": keys.business_shortCode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_shortCode,
        "PhoneNumber": keys.phone_number,
        # replace with an actual url link(callBackUrl)
        "CallBackURL": "https://mydomain.com/api/payments",
        "AccountReference": "7211222",
        "TransactionDesc": "Test",
    }
    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)
    # response = requests.request("GET",
    # 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization':
    # 'Bearer cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ==' }) print(response.text.encode(
    # 'utf8'))


lipa_na_mpesa()
