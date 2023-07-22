from django.shortcuts import render ,redirect
from .models import *
from .forms import *


def home(request):
    return render(request,'home.html')

def email_send(request):
    if request.method == 'POST':
        form=empform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('employee_data')
            except:
                pass
    else:
        form =empform()
    return render(request,'emaildata.html',{'form':form})

def employee_data(request):
    values=employee.objects.all()
    return render(request,'empdata.html',{'values':values})


def update_data(request):
    values=employee.objects.get(id=id)
    if request.POST:
        values.empid=request.POST['empid']
        values.name=request.POST['name']
        values.DO_Birth=request.POST['DO_Birth']
        values.DO_Joining = request.POST['DO_Joining']
        values.DO_Anniversary = request.POST['DO_Anniversary']
        values.Email = request.POST['Email']
        values.sava()
        return redirect('employee_data')

    else:
        form=empform(instance=values)
        return render(request,'editdata.html',{'values':values})


def delete_data(request):
    values=employee.objects.get(id=id)
    values.delete()
    return redirect('employee_data')


