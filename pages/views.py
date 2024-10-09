from django.shortcuts import render
from .models import Login
from .forms import LoginForms,LoginForms2,LoginForms3,LoginForms4
# Create your views here.

def index(request):
    return render(request,'pages/index.html',{'current_page':'home'})

def about(request): 
    return render(request,'pages/about.html',{'current_page':'about'})


def login1(request):
    if request.method== 'POST': 
        data =LoginForms(request.POST)
        data2=LoginForms2(request.POST)
        data3=LoginForms3(request.POST)
        data4=LoginForms4(request.POST) 
        if data.is_valid() and data2.is_valid() and data3.is_valid() and data4.is_valid(): 
            data.save()
            data2.save()
            data3.save()
            data4.save()

    return render(request,'pages/login1.html',{'lf':LoginForms,'lf2':LoginForms2,'lf3':LoginForms3,'lf4':LoginForms4}) 
