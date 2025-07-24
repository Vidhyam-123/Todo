from django.shortcuts import render
from django.contrib.auth.models import User
from.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def homepage(request):
    prof = Profile.objects.filter(user=request.user).first()
    return render(request, 'homepage.html', {'prof': prof})
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
    return render(request,'homepage.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

def profileedit(request,pk):
    proedit=Profile.objects.filter(pk=pk).first()    
    if request.method == "POST":
        proedit.Firstname = request.POST.get("firstname")
        proedit.Lastname = request.POST.get("lastname")
        proedit.Email = request.POST.get("mail")
        proedit.Phonenumber = request.POST.get("number")
        if "image" in request.FILES:
            proedit.image = request.FILES["image"]
        proedit.save()
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, 'homepage.html', {'prof': proedit})


