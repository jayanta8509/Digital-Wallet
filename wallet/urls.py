from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('wallet/', views.WalletList, name='wallet-list'),
    path('wallet/<int:pk>/', views.WalletDetail, name='wallet-detail'),
    path('wallet/current/', views.getAmountinWalletforStore, name='wallet-current'),
    path('wallet/transaction/', views.debitView, name='wallet-transaction'),
]

urlpatterns = format_suffix_patterns(urlpatterns)