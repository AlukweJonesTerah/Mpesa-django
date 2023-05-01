from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from pesa.models import LNMOnline, C2BPayments
from pesa.api.serializers import LNMOnlineSerializer, C2BPaymentsSerializer
from rest_framework.response import Response
import pytz


# import os
# from django.conf import settings
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mpesa.settings')
# settings.configure()
# setDJANGO_SETTINGS_MODULE= Mpesa.settings

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(self.request.data, "This request.data")

        '''
            {'Body':
                {'stkCallback':
                    {
                        'MerchantRequestID':'70216-39201466-2',
                        'CheckoutRequestID':'ws_CO_DMZ_202302271_0945745983042',
                        'ResultCode':'0',
                        'ResultDesc':'The service request is processed successfully',
                        'CallbackMetadata':{
                                                'Item':[
                                                    {'Name':'Amount', 'Value':1.0},
                                                    {'Name':'MpesaReceiptNumber', 'Value':'NCB1FW1DFZ'},
                                                    {"Name":"Balance"},
                                                    {"Name":"TransactionDate", "Value":"20190311190244"},
                                                    {"Name":"PhoneNumber", "Value":"25467899087656"}
                                                
                                                ]
                        
                        
                                            }
                    
                    }
                
                }
            }
        #          this is the request.data json format
        '''
        # extracting the data

        merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        print(merchant_request_id, "this should be MerchantRequestID")
        checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        print(checkout_request_id, "this should be CheckoutRequestID")
        result_code = request.data['Body']['stkCallback']['ResultCode']
        print(result_code, "this should be ResultCode")
        result_description = request.data['Body']['stkCallback']['ResultDesc']
        print(result_description, "this should be ResultDesc")
        amount = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
        print(amount, "this should be amount")
        mpesa_receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
        print(mpesa_receipt_number, "this should be mpesa_receipt_number")
        balance = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][2]
        print(balance, "this should be balance")
        # or
        balance = ''
        transaction_date = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']
        print(transaction_date, "this should be transaction_date")
        phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']
        print(phone_number, "this should be phone_number")

        #         Converting transaction_date from int to string then to date field

        from datetime import datetime
        #  converting int to string
        str_transaction_date = str(transaction_date)
        print(str_transaction_date, "this should be str_transaction_date")
        # converting string to date
        transaction_datetime = datetime.strptime(str_transaction_date, '%Y%m%d%H%M%S')
        print(transaction_datetime)
        # converting  time
        aware_transaction_datetime = pytz.utc.localize(transaction_datetime)
        print(aware_transaction_datetime)

        # saving data  database
        our_model = LNMOnline.objects.create(
            CheckoutRequestID=checkout_request_id,
            MerchantRequestID=merchant_request_id,
            ResultCode=result_code,
            ResultDesc=result_description,
            Amount=amount,
            MpesaReceiptNumber=mpesa_receipt_number,
            Balance=balance,
            TransactionDate=aware_transaction_datetime,
            PhoneNumber=phone_number,
        )
        our_model.save()
        # Response(data, status=None, template_name=None, headers=None, content_type=None)
        return Response({"OurResultDesc", "Successfully worked"})


class C2BValidationAPIView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentsSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(self.request.data, "This request.data.in Validation")

        my_headers = self.get_success_headers(request.data)

        return Response({
            "ResultCode":1,
            "ResponseDesc":"Failed!",
        },
        headers=my_headers)


class C2BConfirmationAPIView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentsSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(self.request.data, "This request.data in Confirmation")

        '''
            {'Body':
               'TransactionType':'PayBill',
               'TransID':'NCQ61M88K4',
               'TransTime':'20190326210441',
               'TransAmount':'2.00',
               'BusinessShortCode':'608761', this is the paybill
               'BillRefNumber':'12345678',
               'InvoiceNumber':'',
               'OrgAccountBalance':'18.00',
               'ThirdPartyTransID':'',
               'MSISDN':'254708927262',
               'FirstName':'Jonh',
               'MiddleName':'J.',
               'LastName':'Doe',
        #          this is the request.data in Confirmation
        '''

        # Response(data, status=None, template_name=None, headers=None, content_type=None)
        return Response({"ResultDesc", 0})
