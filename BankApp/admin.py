from django.contrib import admin
from BankApp.models import Customer
# Register your models here.

class customerAdmin(admin.ModelAdmin):
    list_display=('id','mail_id','amount')
    
admin.site.register(Customer,customerAdmin)