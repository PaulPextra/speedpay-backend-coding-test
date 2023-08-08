from django.urls import path
from accounts import views


urlpatterns = [
    path('users/', views.active_users, name='users'),
    path('transactions/', views.transactions, name='transactions'),
    path('users/signup/', views.user_signup, name='signup'),
    path('users/create-account/', views.create_account, name='create-account'),
    path('users/deposit/', views.deposit, name='deposit'),
    path('users/withdraw/', views.withdraw, name='withdraw'),
    path('users/check-balance/', views.check_balance, name='check-balance'),
    path('users/transfer/', views.transfer_funds, name='transfer'),
]