from accounts.models import Account, Transaction
from accounts.serializers import AccountSerializer, TransactionSerializer, CustomUserSerializer, TransferSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BaseAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import uuid


User = get_user_model()

@swagger_auto_schema(methods=['POST'], operation_summary="user signup", request_body=CustomUserSerializer())
@api_view(['POST'])
def user_signup(request):
    """ User Sign-up Operation """

    serializer = CustomUserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        user = User.objects.create(**serializer.validated_data)
        serializer_class = CustomUserSerializer(user)
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='POST', operation_summary='create account')
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_account(request):
    """ Create Account Operation. """

    user = request.user
    account_number = generate_account_number()
    account = Account.objects.create(user=user, account_number=account_number)
    serializer = AccountSerializer(account)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(method='GET', operation_summary='fetch all active users')
@authentication_classes([BaseAuthentication])
@api_view(['GET'])
@permission_classes([IsAdminUser])
def active_users(request):
    """ Get All Active Users. """
    
    user = User.objects.filter(is_active=True)
    serializer_class = CustomUserSerializer(user, many=True)
    return Response(serializer_class.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='POST', operation_summary='deposit funds into user account')
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deposit(request):
    """ Fund Deposit Operation. """

    user = request.user
    account = user.account
    amount = request.data.get('amount')

    if amount:
        account.balance += amount
        account.save()
        Transaction.objects.create(account=account, amount=amount, transaction_type='deposit')
        return Response({'message': 'Deposit successful'}, status=status.HTTP_200_OK)
    return Response({'message': 'Amount is required'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='POST', operation_summary='withdraw funds from user account')
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def withdraw(request):
    """ Fund Withdrawal Operation. """

    user = request.user
    account = user.account
    amount = request.data.get('amount')

    if amount:
        if account.balance >= amount:
            account.balance -= amount
            account.save()
            Transaction.objects.create(account=account, amount=amount, transaction_type='withdraw')
            return Response({'message': 'Withdrawal successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Amount is required'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='GET', operation_summary='check user account balance')
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_balance(request):
    """ Check User Account Balance. """

    account = request.user.account
    serializer = AccountSerializer(account)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='POST', operation_summary='transfer funds to a user account')
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def transfer_funds(request):
    """ Funds Transfer Operation. """

    user = request.user
    to_account_number = request.data.get('to_account_number')
    from_account = user.account
    amount = request.data.get('amount')

    serializer_class = TransferSerializer(data=request.data)

    if not to_account_number or not amount:
        return Response({'message': 'To account number and amount are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        to_account = Account.objects.get(account_number=to_account_number)
    except Account.DoesNotExist:
        return Response({'message': 'Invalid recipient account number'}, status=status.HTTP_400_BAD_REQUEST)

    if serializer_class.is_valid():
        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            from_account.save()
            to_account.save()
            Transaction.objects.create(account=from_account, amount=-amount, transaction_type='transfer')
            Transaction.objects.create(account=to_account, amount=amount, transaction_type='transfer')
            return Response({'message': 'Transfer successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='GET', operation_summary='fetch all transactions')
@authentication_classes([BaseAuthentication])
@api_view(['GET'])
@permission_classes([IsAdminUser])
def transactions(request):
    """ Fetch All Transactions. """
    
    if request.method == 'GET':
        transactions = Transaction.objects.all()
        serializer_class = TransactionSerializer(transactions, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


def generate_account_number():
        """ Generate Account Number """

        return str(uuid.uuid4().int)[:6]
