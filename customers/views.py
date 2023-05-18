from django.shortcuts import render
from django.http import HttpResponse
from customers.models import  Customers


def loadCustomersPage(request):
    customers = Customers.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'pages/customers.html', context)


def loadCustomerPage(request, pk):
    customer = Customers.objects.get(id=pk)
    context = {
        'customer': customer,
    }

    return render(request, 'pages/customer.html', context)