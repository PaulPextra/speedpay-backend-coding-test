from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUser(AbstractUser):
    """ Extending our user model """

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.username


class Account(models.Model):
    """ Accounts Model Class """

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="account")
    account_number = models.CharField(max_length=6, unique=True, primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.account_number}"


class Transaction(models.Model):
    """ Transactions Model Class """
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10)  # 'deposit', 'withdraw' or 'transfer'
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.transaction_type}"
