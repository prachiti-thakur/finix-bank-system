from django.core.checks import messages
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from BankApp.models import Customer,Transaction_history
from django.db import transaction
from django.utils import timezone
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"home.html",{})
    
def customer(request):
    customer=Customer.objects.all()
    return render(request,"customer.html",{"cust":customer})
    
def aboutUs(request):
    return render(request,"about_us.html",{})

def transaction_one(request):
    #customers to select the the sender
    customer=Customer.objects.all()
    return render(request,"transaction.html",{"cust":customer})

def transaction_two(request,cid):
    sender=Customer.objects.get(id=cid)
    
    if(request.method=="GET"):
        # form of transction
        return render(request,"form.html",{"sender":sender})
    
    else:
        try:
            with transaction.atomic():
                receiver_id=request.POST['receiver']
                receiver=Customer.objects.get(id=receiver_id)
                amount=float(request.POST['amount'])
                
                sender.amount-=amount
                receiver.amount+=amount
                
                sender.save()
                receiver.save()
                
                t1=Transaction_history()
                t1.sender=sender.id
                t1.receiver=receiver.id
                t1.amount=amount
                t1.dnt=timezone.now()
                t1.save()
                
                messages.success(request,"Transaction done successfully!!")
                return redirect(transaction_history)
        except:
            messages.error(request,"something wents wrong!!")
            return redirect(transaction_history)
            

def transaction_history(request):
    trans=Transaction_history.objects.all()
    return render(request,"transaction_history.html",{"trans":trans})

def abc(request):
    pass