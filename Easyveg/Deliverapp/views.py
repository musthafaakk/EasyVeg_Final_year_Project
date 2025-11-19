from django.shortcuts import render
from.models import *
from django.contrib import messages
def deliverylog(request):
    return render(request,'delivery/deliverylog.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import delivery_registration
def deliverylog(request):
        if request.method =="GET":
         return render(request,'delivery/deliverylog.html')
        else:
            try:
                email=request.POST.get('email')
                password=request.POST.get('password')
                error_message = NameError 
                flag=0
                obj= delivery_registration.objects.get(email=email)
                print(obj.email,obj.password)
                if obj and obj.adminapprove==1 :
                    print("logged in")
                    if(password==obj.password):
                        flag=1
                        if flag==1 :
                            request.session['email']=obj.email
                            request.session['id']=obj.id
                            return redirect("deliveryhome")
                        else:
                            error_message = 'email or password invalid !!!'
                            return render(request,"delivery/deliverylog.html",{'error':error_message})
                    else:
                        if obj.adminapprove==0:
                            error_message="admin permission required"
            except delivery_registration.DoesNotExist as e:
                error_message = 'email or password INVALID !!!'
                return render(request,"delivery/deliverylog.html",{'error':error_message})
            return render(request,"delivery/deliverylog.html",{'error':error_message})





             
def deliveryreg(request):
    # POST: process submitted form
    if request.method == "POST":
        name = request.POST.get("fullname")
        email = request.POST.get("email")
        phonenumber = request.POST.get("phone")
        address = request.POST.get("address")
        availabletime = request.POST.get("time")
        liscenceimg=request.POST.get("liscenceimg")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")

        if password == confirmpassword:
            # fixed typo: .filter (was .fiter)
            if delivery_registration.objects.filter(email=email).exists():
                messages.info(request, 'This email is already in use')
            elif delivery_registration.objects.filter(phonenumber=phonenumber).exists():
                messages.info(request, 'This number is already in use')
            else:
                # Use the correct variable: licensenumber (you had license=license which was undefined)
                userdata = delivery_registration(
                    fullname=name,
                    email=email,
                    phonenumber=phonenumber,
                    address=address,
                    time=availabletime,
                    liscenceimg=liscenceimg,
                    password=password
                )
                userdata.save()
                return redirect("deliverylog")
        else:
            # fixed spelling: messages (was messsages)
            messages.info(request, 'Password not matched')

        # If we reach here, either validation failed or messages were added.
        return render(request, 'delivery/deliveryreg.html')

    # GET: show empty registration form (must return a response)
    return render(request, 'delivery/deliveryreg.html')

def deliveryhome(request):
    return render(request,'delivery/deliveryhome.html')
def about(request):
    return render(request,'navbar/about.html')
def profile1(request):
    return render(request,'navbar/profile1.html')

# Create your views here.
