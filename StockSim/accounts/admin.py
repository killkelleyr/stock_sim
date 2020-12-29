from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    fields = ['user', 'rhoodID', 'rhoodPWD', 'rhQ']
    #list_display = []

admin.site.register(Account, AccountAdmin)