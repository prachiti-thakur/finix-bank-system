
from django.urls import path
from BankApp import views
urlpatterns = [
    path('',views.home),
    path('customer',views.customer),
    path('aboutUs',views.aboutUs),
    path('transaction_one',views.transaction_one),
    path('transaction_two/<cid>',views.transaction_two),
    path('transaction_history',views.transaction_history),
    
]
