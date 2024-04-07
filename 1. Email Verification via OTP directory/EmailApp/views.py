from django.shortcuts import render,redirect
from .models import Subscribers
from .forms import Subscribe
from .forms import OTPform
from django.contrib import messages

from django.core.mail import send_mail

import random

# Create your views here.

OTP = 0000
OTP = random.randint(1000,9999) 

def index(request):
    Users = Subscribers.objects.order_by('Name')
    if request.method == 'POST':
        form = Subscribe(request.POST)
        if form.is_valid():
            if len(Subscribers.objects.filter(Email = form.cleaned_data['Email'])) == 0:
                form.save()
                send_mail(
                    'Your OTP for registration test on django',
                    str(OTP),
                    [form.cleaned_data['Email'],], #Recipent List
                    False,
                )
                messages.info(request,"OTP Sent")
                return redirect('OTP')
            else:
                messages.info(request, "Email Already registered, please try a different email")
        else:
            messages.info(request,"Wrong Email")
            return redirect('OTP')
    form = Subscribe()
    User_List = {
        'forms': form, 
        'User_List' : Users,
                 }
    return render(request, 'EmailApp\index.html',User_List)

def OTPview(request):
    if request.method == 'POST':
        form = OTPform(request.POST)
        if form.is_valid():
            if form.cleaned_data['OTP'] == OTP:
                messages.info(request, "Email Verified")
                return redirect('index')
            else:
                messages.info(request,"Wrong OTP please try again")
    form = OTPform()
    context_dict = {
        'forms' : form,
    }
    return render(request, 'EmailApp\otp.html', context_dict)