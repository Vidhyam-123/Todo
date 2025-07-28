from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to="profile/",null=True,blank=True,default="")
    Firstname=models.CharField(max_length=25,blank=True,null=True)
    Lastname=models.CharField(max_length=25,blank=True,null=True)
    Email=models.CharField(max_length=500,blank=True,null=True)
    Phonenumber=models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return self.user.username + "profile"

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todos = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)  
    deadline = models.DateField()
    complete= models.BooleanField(default=False)
    
    def __str__(self):
        return self.todos
