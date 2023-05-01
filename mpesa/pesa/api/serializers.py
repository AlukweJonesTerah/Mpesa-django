from rest_framework import serializers
from pesa.models import LNMOnline, C2BPayments


class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMOnline
        fields = 'id'


class C2BPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BPayments
        fields = ('id',
                  'TransactionType',
                  'TransID',
                  'TransTime',
                  'TransAmount',
                  'BusinessShortCode',
                  'BillRefNumber',
                  'InvoiceNumber',
                  'OrgAccountBalance',
                  'ThirdPartyTransID',
                  'MSISDN',
                  'FirstName',
                  'MiddleName',
                  'LastName'
                  )

        '''
            {
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
