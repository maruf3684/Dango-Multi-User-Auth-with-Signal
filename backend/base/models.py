from django.db import models
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)

from django.utils import timezone


class MyUserManager(BaseUserManager):
    def create_user(self, name,email,password=None, ):

        if not email:
            raise ValueError('Users must have an email address')
        
        if not password:
                raise ValueError('Users must have valid password')

        user = self.model(name=name,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
     
     
    # def create_staffuser(self, phone, password):
    #  pass

    def create_superuser(self,name,email,password=None,):
        user = self.create_user(
            name=name,
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.is_student = True
        user.is_teacher = True
        user.save(using=self._db)
        return user






class Account(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email address',unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_student = models.BooleanField(default=False)
    is_teacher= models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] #create superuser a chabe
    def __str__(self):
        return self.email
    
    #this function gives super user power /self.is_stuff dela stuff power pabe/aita o mixin a ache
    # def has_perm(self, perm, obj=None):
    #     return self.is_superuser
    
    # ai class mixin a age theke e ache
    # def has_module_perms(self, app_label):
    #     return self.is_superuser

#! always remember
#is_superuser
#is_staff
#is_active 
# ai 3 ta field change korba na
