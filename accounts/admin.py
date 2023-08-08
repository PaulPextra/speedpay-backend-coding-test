from django.contrib import admin
from accounts.models import CustomUser, Account, Transaction


admin.site.register(CustomUser)
admin.site.register(Account)
admin.site.register(Transaction)
