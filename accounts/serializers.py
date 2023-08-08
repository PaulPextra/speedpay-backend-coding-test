from rest_framework import serializers
from accounts.models import Account, Transaction
from django.contrib.auth import get_user_model


User = get_user_model()

class AccountSerializer(serializers.ModelSerializer):
    """ Accounts Serializer Class """
    
    class Meta:
        model = Account
        fields = ('account_number', 'balance')


class CustomUserSerializer(serializers.ModelSerializer):
    """ CustomUser Serializer Class """

    account = AccountSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = (
            'id',
            'first_name', 
            'last_name', 
            'username',
            'password', 
            'email',
            'phone', 
            'gender',
            'address',
            'account',
            'is_active',
            'date_joined'
        )


class TransactionSerializer(serializers.ModelSerializer):
    """ Transactions Serializer Class """

    class Meta:
        model = Transaction
        fields = ('account', 'amount', 'transaction_type', 'timestamp')


class TransferSerializer(serializers.Serializer):
    """ Transfer Serializer Class """

    to_account_number = serializers.CharField(max_length=6)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
