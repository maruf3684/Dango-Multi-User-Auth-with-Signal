from django.shortcuts import render
from .schoolforms import UserForm

# Create your views here.

def student(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            ##use this or user.set_password() for password save
            account = Account.objects.create_user(name=name, email=email, password=password)

            form=UserForm()
            return render(request, 'student.html',context={'form':form})
        else:
            print ("error submitting form")
            form=UserForm()
            return render(request, 'student.html',context={'form':form})
    if request.method =='GET':
        form=UserForm()
    return render(request, 'student.html',context={'form':form})
