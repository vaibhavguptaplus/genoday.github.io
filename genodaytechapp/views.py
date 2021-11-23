from django.shortcuts import render
from .models import *
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('phone')
        message=request.POST.get('message')
        contact(
        name=name,
        email=email,
        number=number,
        message=message
        ).save()
    if request.method=="POST":
        nameC=request.POST.get('nameC')
        domainName=request.POST.get('domainName')
        companyName=request.POST.get('companyName')
        emailC=request.POST.get('emailC')
        ChatBox(
            nameC=nameC,
            domainName=domainName,
            companyName=companyName,
            emailC=emailC
        ).save()
        
        return render(request, 'index.html',)
    else:
        return render(request,'index.html')
    
