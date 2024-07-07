from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    return render(request, 'home/index.html')

def home(request):
    return render(request,'Home/homepage.html')

def about(request):
    return render(request,'home/about.html')

def service(request):
    return render(request,'Home/service.html')



def contact(request):
    return render(request,'Home/contact.html')