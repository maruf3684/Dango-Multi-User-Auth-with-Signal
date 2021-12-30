from django.db.models.signals import post_save, pre_delete
from .schoolmodels import Student
from .models import Account
from django.dispatch import receiver




def updateProfile(sender,instance,**kwargs):
    account=instance
    student=Student(account=account)
    print("cholse")
    student.save()

post_save.connect(updateProfile, sender=Account)