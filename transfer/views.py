from django.shortcuts import render, redirect
from django.http import  HttpResponseNotFound

from django.contrib import messages

from customers.models import Customers
from .models import Transfer

import time 

def conversion(var):
    var = str(var)
    var = float(var)
    var = int(var)
    return var




def loadTransferPage(request):
    customers = Customers.objects.all()
    current_user = request.user
    context = {
        'customers': customers,
    }

    # main_balance = Customers.objects.get(id='cea05954-8f5b-40e2-8151-d3dc6ecb811e').current_balance
    # print(main_balance)

    # main_balance = conversion(main_balance)

   # form validation 
    
    if request.method == 'POST':
        amount = request.POST['amount']
        transferees = request.POST.getlist('select')

    # Loop for looping through the selected options 

        for i in range(len(transferees)):
            pk = transferees[i]

    # Getting the amount from the database and doing the maths for the transfer
        try:
            if Customers.objects.filter(id=pk).exists():
                print('exists')
                user_amount = Customers.objects.get(id=pk).current_balance
                # print(user_amount)
                user_amount = conversion(user_amount)

                # main_balance -= int(amount)
    
                update_user_amt = user_amount + int(amount)

                original_amount = Customers.objects.get(id=pk).current_balance
                sender = Customers.objects.get(user_id=current_user.id)
                
    
                saveUser = Customers.objects.filter(id=pk).update(current_balance=update_user_amt)
                saveTransfer = Transfer(transfered_amt=int(amount), transferee=sender)
                saveTransfer.save()
                messages.success(request, 'Transfer Successful!')
                return redirect('customers')

        except (DeprecationWarning, ValueError, InterruptedError, IndentationError):
            return HttpResponseNotFound('<h1>Something is wrong</h1>')

                     
    return render(request, 'pages/transfer.html', context)



