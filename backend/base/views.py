from django.shortcuts import render
from .schoolforms import UserForm

# Create your views here.

def student(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        print (request.POST['name'])
        if form.is_valid():
            form.save()
            form=UserForm()
            return render(request, 'student.html',context={'form':form})
        else:
            print ("error submitting form")
            form=UserForm()
            return render(request, 'student.html',context={'form':form})
    if request.method =='GET':
        form=UserForm()
    return render(request, 'student.html',context={'form':form})