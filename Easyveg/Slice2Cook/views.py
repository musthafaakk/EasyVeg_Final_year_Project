from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")
def userlog(request):
    if request.method=="POST":
        try:
            name=request.POST.get("name")
            email=request.POST.get("email")
            password=request.POST.get("password")
            log=user_registration.objects.get(name=name,email=email,password=password)
            request.session['name']=log.name
            request.session['id']=log.id
            return redirect("userhome")
        except user_registration.DoesNotExist as e :
            messages.info(request,'invalid login')
    return render(request,"user/userlog.html")
def userreg(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")
        state=request.POST.get("state")
        district=request.POST.get("district")
        address=request.POST.get("address")
        pincode=request.POST.get("pincode")
        phonenumber=request.POST.get("phonenumber")
        if password==confirmpassword:
            if user_registration.objects.filter(email=email).exists():
                messages.info(request,'This email is alresdy in use')
            elif user_registration.objects.filter(phonenumber=phonenumber).exists():
                messages.info(request,'This number is already in use')
            else :
                userdata=user_registration(name=name,email=email,password=password,state=state,district=district,address=address,pincode=pincode,phonenumber=phonenumber)
                userdata.save()
                return redirect("userlog")
        else:
            messages.info(request,'password not matched')


    return render(request,"user/userreg.html")
def userhome(request):
    return render(request,"user/userhome.html")
def emplog(request):
    return render(request,"employee/emplog.html")
def empreg(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        phonenumber=request.POST.get("phonenumber")
        email=request.POST.get("email")
        experience=request.POST.get("experience")
        username=request.POST.get("username")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")
        address=request.POST.get("address")
        if password==confirmpassword:
            if employee_registration.objects.filter(username=username).exists():
                messages.info(request,'Thiis email is already in use')
        elif  employee_registration.objects.filter(phonenumber=phonenumber).exists():
            messages.info(request,'The number is already in use')
        else:
            userdata=employee_registration(firstname=firstname,lastname=lastname,
                                           phonenumber=phonenumber,email=email,experience=experience,
                                           username=username,password=password,address=address)
            userdata.save()
            return redirect("emplog")
    else:
        pass
    
    return render(request,"employee/empreg.html")
def emphome(request):  
    return render(request,"employee/emphome.html")
def plist(request):
    return render(request,"product/plist.html")
def pdetails(request):
    return render(request,"product/pdetails.html")
def bdetails(request):
    return render(request,"navbar/bdetails.html")
def profile1(request):
    return render(request,"navbar/profile1.html")
def cartview(request):
    return render(request,"navbar/cartview.html")
def about(request):
    return render(request,"navbar/about.html")


                                                     



