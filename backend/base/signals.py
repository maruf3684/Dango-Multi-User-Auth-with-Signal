from django.db.models.signals import post_save, pre_delete
from .schoolmodels import Student
from .models import Account
from django.dispatch import receiver
from .schoolmodels import Student



def updateProfile(sender,instance,**kwargs):
    if instance:
        student = Student.objects.filter(account=instance).exists() or None
        print(student)

        if not student:
            account=instance
            student=Student(account=account)
            student.save()
        else:
            pass

post_save.connect(updateProfile, sender=Account)
