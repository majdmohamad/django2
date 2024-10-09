from django.db import models

# Create your models here.



class Login(models.Model):
    username= models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    useremail=models.CharField(max_length=50)