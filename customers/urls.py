from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.loadCustomersPage, name='customers'),
    path('customer/<str:pk>/', views.loadCustomerPage, name='view customer')
]