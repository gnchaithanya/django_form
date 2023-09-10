from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse
def insert_student(request):

    SFEO=StudentForms()
    d={'SFEO':SFEO}
    if request.method=='POST':
        SFDO=StudentForms(request.POST)
        if SFDO.is_valid():
            Sname=SFDO.cleaned_data['Sname']
            Sid=SFDO.cleaned_data['Sid']
            Semail=SFDO.cleaned_data['Semail']

            so=Student.objects.get_or_create(Sname=Sname,Sid=Sid,Semail=Semail)[0]
            so.save()
            QSO=Student.objects.all()
            d1={'QSO':QSO}
            return render(request,'display_student.html',d1)



    return render(request,'insert_student.html',d)

def update_student(request):
    SFEO=StudentForms()
    d={'SFEO':SFEO}
    if request.method=='POST':
        SFDO=StudentForms(request.POST)
        if SFDO.is_valid():
            Sname=request.POST['Sname']
            Sid=request.POST['Sid']
            Semail=request.POST['Semail']
            Student.objects.filter(Sname=Sname).update(Semail=Semail,Sid=Sid)
            QSO=Student.objects.all()
            d1={'QSO':QSO}
            return render(request,'display_student.html',d1)

           
    return render(request,'update_student.html',d)

def delete_student(request):
    SEFO=StudentForms()
    d={'SEFO':SEFO}
    if request.method=='POST':
        SFDO=StudentForms(request.POST)
        if SFDO.is_valid():
            Sname=request.POST['Sname']
           
            Student.objects.filter(Sname=Sname).delete()
            QSO=Student.objects.all()
            d1={'QSO':QSO}
            return render(request,'display_student.html',d1)
    return render(request,'delete_student.html',d)

   


