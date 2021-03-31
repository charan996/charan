from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse("<h2 style='color:white;background-color:REd'>welcome to home</h2>")

def chk(request):
	 return HttpResponse("<script>alert('hii good aftn')</script><h2>welcome</h2>")

def homepage(request):
	return render(request,'raj/homepage.html')

def lgn(lf):
    return render(lf,'raj/login.html')
def reg(rt):
   return render(rt,'raj/register.html')	