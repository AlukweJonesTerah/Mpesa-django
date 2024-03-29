from django.db import models

# Create your models here.

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


class LNMOnline(models.Model):
    CheckoutRequestID = models.CharField(max_length=50, blank=True, null=True)
    MerchantRequestID = models.CharField(max_length=20, blank=True, null=True)
    ResultCode = models.IntegerField(blank=True, null=True)
    ResultDesc = models.CharField(max_length=120, blank=True, null=True)
    Amount = models.FloatField(blank=True, null=True)
    MpesaReceiptNumber = models.CharField(max_length=20, blank=True, null=True)
    Balance = models.CharField(max_length=12, blank=True, null=True)
    TransactionDate = models.DateTimeField(blank=True, null=True)
    PhoneNumber = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.PhoneNumber} has sent {self.Amount} on {self.TransactionDate} , RefNo: {self.MpesaReceiptNumber}'


class C2BPayments(models.Model):
    TransactionType = models.CharField(max_length=15, blank=True, null=True)
    TransID = models.CharField(max_length=12, blank=True, null=True)
    TransTime = models.CharField(max_length=14, blank=True, null=True)
    TransAmount = models.CharField(max_length=12, blank=True, null=True)
    BusinessShortCode = models.CharField(max_length=10, blank=True, null=True)
    BillRefNumber = models.CharField(max_length=20, blank=True, null=True)
    InvoiceNumber = models.CharField(max_length=20, blank=True, null=True)
    OrgAccountBalance = models.CharField(max_length=12, blank=True, null=True)
    ThirdPartyTransID = models.CharField(max_length=12, blank=True, null=True)
    MSISDN = models.CharField(max_length=12, blank=True, null=True)
    FirstName = models.CharField(max_length=30, blank=True, null=True)
    MiddleName = models.CharField(max_length=30, blank=True, null=True)
    LastName = models.CharField(max_length=30, blank=True, null=True)
