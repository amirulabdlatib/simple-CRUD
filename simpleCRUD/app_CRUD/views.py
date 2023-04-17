from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Member


# Create your views here.
def index(request):
    mem = Member.objects.all()
    context = {
        'mem':mem,
    }
    return render(request,'index.html',context=context)

def addMember(request):
    return render(request,'add.html')

def addrec(request):
    x = request.POST.get("firstName")
    y = request.POST.get("lastName")
    mem=Member(firstname=x,lastname=y,)
    mem.save()

    return redirect('index')
    
def deleterec(request,id):
    mem = Member.objects.get(id=id)
    mem.delete()

    return redirect('index')

def update(request,id):
    mem = Member.objects.get(id=id)
    context = {
        'mem':mem,
    }

    return render(request,'update.html',context=context)

def updaterec(request,id):
    x = request.POST.get("firstName")
    y = request.POST.get("lastName")
    
    mem = Member.objects.get(id=id)

    mem.firstname = x
    mem.lastname = y
    mem.save()

    return redirect('index')