from django.db import models
from .models import Account

class Teacher(models.Model):
    account = models.OneToOneField(Account,on_delete=models.CASCADE,default=None)
    identity = models.CharField(max_length=30,null=True,blank=True)
    salary = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.account.name


class Student(models.Model):
    account = models.OneToOneField(Account,on_delete=models.CASCADE,default=None)
    identity = models.CharField(max_length=30,null=True,blank=True)
    classnumber = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
       return self.account.name


