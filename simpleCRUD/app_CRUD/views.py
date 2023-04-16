from django.http import HttpResponse
from django.shortcuts import render
from .models import Member


# Create your views here.
def index(request):
    mem = Member.objects.all()
    context = {
        'mem':mem,
    }
    return render(request,'index.html',context=context)