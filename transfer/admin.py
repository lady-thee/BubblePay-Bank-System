from django.contrib import admin
from transfer.models import Transfer 



class TransferAdmin(admin.ModelAdmin):
    list_display = ('id', 'transferee', 'transfered_amt')


admin.site.register(Transfer, TransferAdmin)
