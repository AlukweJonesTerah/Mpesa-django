import requests
from requests.auth import HTTPBasicAuth
import json

requests = ""

def getAccessToken(request):
    consumer_key = ''
    consumer_secret = ''
    api_URL = ''
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    print(validated_mpesa_access_token)

getAccessToken()