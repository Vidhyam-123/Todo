from django.shortcuts import render
from django.contrib.auth.models import User
from.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')
def tasks(request):
    return render(request,'tasks.html')
def edit(request):
    return render(request,'edit.html')
def signup(request):
    if request.method=="POST":
        user=User.objects.create(username=request.POST.get("username"))
        user.set_password(request.POST.get("password"))
        user.save()
        Profile.objects.create(
            user=user,
            Firstname=request.POST.get("firstname"),
            Lastname=request.POST.get("lastname"),
            Email=request.POST.get("email"),
            image=request.FILES["image"],
            Phonenumber=request.POST.get("number"),
            )
        return HttpResponseRedirect(reverse("homepage"))

def userlogin(request):
    msg=""
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)  #for authentication .value will be true or false
        if user:
            login(request,user)
            print("login successful")
            return HttpResponseRedirect(reverse("homepage"))
        else:
            print("No such user found")
            msg="invalid login credentials"
        print(username,password)
