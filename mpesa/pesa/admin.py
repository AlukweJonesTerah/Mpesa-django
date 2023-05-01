from django.contrib import admin
from .models import LNMOnline, C2BPayments


# Register your models here.


class LNMOnlineAdmin(admin.ModelAdmin):
    list_display = ['PhoneNumber', 'Amount', 'MpesaReceiptNumber', 'TransactionDate']


admin.site.register(LNMOnline, LNMOnlineAdmin)


class C2BPaymentAdmin(admin.ModelAdmin):
    list_display = ['MSISDN', 'TransAmount ', 'TransID', 'TransTime']


admin.site.register(C2BPayments, C2BPaymentAdmin)
