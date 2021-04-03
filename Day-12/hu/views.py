from django.shortcuts import render,redirect
from hu.models import Usrg

# Create your views here.
def home(request):
	return render(request,'html/home.html')
def about(request):
    return render(request,'html/about.html')
def contact(request):
    return render(request,'html/contact.html')
def login(request):
    return render(request,'html/login.html') 
def registration(request):
	if request.method =="POST":
		u=request.POST['uname']
		p=request.POST['pd']
		e=request.POST['eml']
		a=request.POST['ag']
		d={'us':u,'em':e,'ps':p,'ag':a}
		return render(request,'html/details.html',{'charan':d})
	return render(request,'html/registration.html')

def action(request):
	if request.method=="POST":
		un=request.POST['username']
		email=request.POST['email']
		pas=request.POST['password']
		age=request.POST['age']
		data=Usrg.objects.create(username=un,password=pas,age=age,email=email)
		data2=Usrg.objects.all()
		return render(request,'html/action.html',{'info':data2})
	return render(request,'html/action.html')

def delte(request,r):
	s = Usrg.objects.get(id=r)
	s.delete()
	return redirect('/crud')