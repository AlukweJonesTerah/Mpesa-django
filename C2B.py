import requests
import keys
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token

def register_url():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {'Authorization': "Bearer %s" % access_token}
    request = {"ShortCode": keys.shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://mydomain.com/confirmation",
               "ValidationURL": "https://mydomain.com/validation",
               }
    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


register_url()


def simulate_c2b_transaction():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {'Authorization': "Bearer %s" % access_token}
    request = {
        "ShortCode": keys.shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "1",
        "Msisdn": keys.test_msisdn,
        "BillRefNumber": "123456789",
    }
    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

simulate_c2b_transaction()

# payload = {
#     "InitiatorName": "testapi",
#     "SecurityCredential": "L9BzsxG+UatJu0xkNSYfBhtyDguHYgSGh7nsm51jjor3JIdvS43qXSSxsQ34ExH9CEbk118lfPw+5Nr0M7OekGFPyXA1/MbR4OQP8cDcByuat5+mJHRHDM2I7p+NzsmolYKYvRxdGvW86k0ZXbiiL98ZuVecbIkShDm5ihhEWmPPVAL2UMZMVTZKdgjy7A/QEJZa/LvtE773jGNz5uHGXoMcSxgkC5METYg1/C3B1FrIjk7B5eMXvZ0Yq6zE4iXyqPn0mjtJS5jAkem+O1ieyIHdCnqKPK5mgRl75NFHqV0AZl2Em4Y+8SKDCuRRmrZZRILvO2Gg+vOGpOvnFSQOeA==",
#     "CommandID": "BusinessPayment",
#     "Amount": 1,
#     "PartyA": 600978,
#     "PartyB": 254708374149,
#     "Remarks": "Test remarks",
#     "QueueTimeOutURL": "https://mydomain.com/b2c/queue",
#     "ResultURL": "https://mydomain.com/b2c/result",
#     "Occassion": "",
#   }
#
# response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest', headers = headers, data = payload)
# print(response.text.encode('utf8'))
