from django.shortcuts import render,redirect
from Emp.models import UsrRg
from Emp.forms import UsregForm,Userupdate
from django.http import HttpResponse


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
	if request.method=="POST":
		u = request.POST['uname']
		p = request.POST['pwd']
		e = request.POST['email']
		a = request.POST['age']
		d = {'us':u,'em':e,'ag':a,'ps':p}
		return render(request,'html/details.html',{'d':d})
	return render(request,'html/registration.html') 

def crud(request):
    if request.method=="POST":
    	us=request.POST['ues']
    	em=request.POST['eml']
    	ps=request.POST['pas']
    	ag=request.POST['ag']
    	data=UsrRg.objects.create(username=us,password=ps,age=ag,email=em)
    	data2=UsrRg.objects.all()
    	return render(request,'html/actions.html',{'info':data2})
    return render(request,'html/actions.html')


def deletedata(request,id):
	data=UsrRg.objects.get(id=id)
	data.delete()
	return redirect('/actions')

def dform(request):
	if request.method == "POST":
		e=UsregForm(request.POST)
		if e.is_valid():
			e.save()
			return HttpResponse("user created succesfully")
	e=UsregForm()
	return render(request,'html/dyform.html',{'tu':e})

def showinfo(request):
	data=UsrRg.objects.all()
	return render(request,'html/showdata.html',{'info':data})

def infodelete(request,id):
	data=UsrRg.objects.get(id=id)
	if request.method=="POST":
		data.delete()
		return redirect('/shw')
	return render(request,'html/userdelete.html',{'sd':data})
# def edit(re,id):
# 	data=UsrRg.objects.get(id=id)
# 	if re.method=="POST":
# 		data.username=re.POST['username']
# 		data.age=re.POST['age']
# 		data.email=re.POST['email']
# 		data.password=re.POST['password']
# 		data.save()
# 		return HttpResponse("datasaved")
# 	return render(re,'html/useredit.html',{'info':data})

def userupdate(up,si):
	t=UsrRg.objects.get(id=si)
	if up.method=="POST":
		d=Userupdate(up.POST,instance=t)
		if d.is_valid():
			d.save()
			return redirect('/shw')
	d=Userupdate(instance=t)
	return render(up,'html/updateuser.html',{'us':d})


	 
	 
    	