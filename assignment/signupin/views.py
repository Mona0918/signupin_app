from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import RegisterForm,UserTypeForm
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import SignUpModel

def homeview(request):
    return render(request,'signupin.html')

def usertypeview(request):
    if request.method=='POST':
        form=UserTypeForm(request.POST)
        if form.is_valid():
            form.save()
            type=form.cleaned_data['usertype']
            url=reverse('signupin:signup',args=[type])
            return redirect(url)
    else:
        form=UserTypeForm()
    return render(request,"usertype.html",{'usertype_form':form})

def signupview(request,type):
    if request.method=='POST':
        form=RegisterForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.utype=type
            form.save()
            return redirect(reverse('signupin:signin'))
    else:
        form=RegisterForm()
    return render(request,'signup.html',{'register_form':form})

def loginview(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                auth_login(request,user)
                name=user.get_username()
                url=reverse('signupin:dashboard',args=[name])
                return redirect(url)
    else:
        form=AuthenticationForm()
    return render(request,'signin.html',{'form':form})

def dashboardview(request,name):
    data=SignUpModel.objects.get(username=name)
    return render(request,"dashboard.html",{'data':data})

@login_required
def logoutview(request):
    auth_logout(request)
    return redirect(reverse('signupin:usertype'))
