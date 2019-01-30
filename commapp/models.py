from django.db import models
class Details(models.Model):
    Firstname=models.CharField(max_length=10)
    Lastname=models.CharField(max_length=10)
    Username=models.CharField(max_length=20,primary_key=True)
    Phonenumber=models.IntegerField()
    Email=models.EmailField(max_length=20)
    Gender=models.CharField(max_length=10)
    Password=models.CharField(max_length=10)
    Caste=models.CharField(max_length=10)
    Address=models.CharField(max_length=10)
    District=models.CharField(max_length=10)
    State=models.CharField(max_length=10)

class Events(models.Model):
    Name=models.CharField(max_length=50)
    Eventname=models.CharField(max_length=100)
    Description=models.TimeField()
    Date=models.DateField()
    Time=models.TimeField()




# Create your models here.
