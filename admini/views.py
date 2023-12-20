from django.shortcuts import render, redirect
from . forms import userf, teacher_regf, admin_regf, secretary_regf,bursar_regf,dos_regf
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'admin/home.html',{})

def mteachers(request):
    return render(request,'admin/mteachers.html',{})
def teacher_registration(request):
    form =userf
    formt = teacher_regf
    if request.method== "POST":
        form =userf(request.POST or None, request.FILES or None)
        formt = teacher_regf(request.POST or None)
        if form.is_valid() and formt.is_valid():
           user= form.save()
           teacher =formt .save(commit=False)
           teacher.user = user
           teacher.save()
           return redirect('mteachers')  
    return render(request,'admin/registerteacher.html',{'form1':form,'form2':formt})

def mstudents(request):
    return render(request,'admin/mstudents.html',{})

def madministrators(request):
    return render(request,'admin/madministrators.html',{})
def administrator_registration(request):
    form =userf
    forma = admin_regf
    if request.method== "POST":
        form =userf(request.POST or None, request.FILES or None)
        forma = admin_regf(request.POST or None)
        if form.is_valid() and forma.is_valid():
           user= form.save()
           admin =forma .save(commit=False)
           admin.user = user
           admin.save()
           return redirect('madministrators')
    return render(request,'admin/registeradminstrator.html',{'form1':form,'form2':forma})

def mdos(request):
    return render(request,'admin/mdos.html',{})
def dos_registration(request):
    form =userf
    formd = dos_regf
    if request.method== "POST":
        form =userf(request.POST or None, request.FILES or None)
        formd = dos_regf(request.POST or None)
        if form.is_valid() and formd.is_valid():
           user= form.save()
           dos =formd.save(commit=False)
           dos.user = user
           dos.save()
           return redirect('mdos')
    return render (request,'admin/registerdos.html',{'form1':form,'form2':formd})

def msecretary(request):
    return render(request,'admin/msecretary.html',{})
def secretary_registration(request):
    form =userf
    forms = secretary_regf
    if request.method== "POST":
        form =userf(request.POST or None, request.FILES or None)
        forms = secretary_regf(request.POST or None)
        if form.is_valid() and forms.is_valid():
           user= form.save()
           secretary =forms.save(commit=False)
           secretary.user = user
           secretary.save()
           return redirect('msecretary')
    return render (request,'admin/registersecretary.html',{'form1':form,'form2':forms})

def mbursar(request):
    return render(request,'admin/mbursa.html',{})
def bursar_registration(request):
    form =userf
    formb = bursar_regf
    if request.method== "POST":
        form =userf(request.POST or None, request.FILES or None)
        formb = bursar_regf(request.POST or None)
        if form.is_valid() and formb.is_valid():
           user= form.save()
           bursar =formb.save(commit=False)
           bursar.user = user
           bursar.save()
           return redirect('mbursar')
    return render (request,'admin/registerbursar.html',{'form1':form,'form2':formb})

def msupportstaff(request):
    return render(request,'admin/msupportstaff.html',{})
