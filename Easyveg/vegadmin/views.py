from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.
def indexadmin(request):
    return render(request,"tempadmin/indexadmin.html")
def userdetails(request):
    return render(request,"tempadmin/userdetails.html")
def deliverydetails(request):
    return render(request,"tempadmin/deliverydetails.html")
def bookingdetails(request):
    return render(request,"tempadmin/bookingdetails.html")
def additems(request):
    return render(request,"tempadmin/additems.html")
def viewitems(request):
    return render(request,"tempadmin/viewitems.html")
def edit(request):
    return render(request,"tempadmin/edit.html")
def logadmin(request):
    if request.method=="POST":
        try:
            email=request.POST.get("email")
            password=request.POST.get("password")
            log=login_admin.objects.get(email=email,password=password)
            request.session['name']=log.name
            request.session['id']=log.id
            return redirect("indexadmin")
        except login_admin.DoesNotExist as e :
            messages.info(request,'invalid login')


            
    return render(request,"tempadmin/logadmin.html")


