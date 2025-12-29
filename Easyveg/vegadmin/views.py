import os
from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from Slice2Cook.models import *
from Deliverapp.models import *
# Create your views here.
def indexadmin(request):
    return render(request,"tempadmin/indexadmin.html")
def userdetails(request):
    pro=user_registration.objects.all()
    return render(request,"tempadmin/userdetails.html",{'u':pro})
def deliverydetails(request):
    pro=delivery_registration.objects.all()
    return render(request,"tempadmin/deliverydetails.html",{'d':pro})
def employeedetails(request):
    pro=employee_registration.objects.all()
    return render(request,"tempadmin/employeedetails.html",{'e':pro})
def additems(request):
    if request.method == "POST":
        productname = request.POST.get("productname")
        category = request.POST.get("category")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        description = request.POST.get("description")
        productimage = request.FILES.get("productimage")

        add_items.objects.create(
            productname=productname,
            category=category,
            price=price,
            quantity=quantity,
            description=description,
            productimage=productimage
        )

        return redirect("viewitems")  # reload or go to any page you wan
    return render(request,"tempadmin/additems.html")
def viewitems(request):
    pro=add_items.objects.all()
    return render(request,"tempadmin/viewitems.html",{'v':pro})
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
def eapprove(request,aid):
    pro=employee_registration.objects.get(id=aid)
    pro.adminapprove=True
    pro.save()
    return redirect("employeedetails")
def ereject(request,aid):
    pro=employee_registration.objects.get(id=aid)
    pro.adminreject=True
    pro.save()
    return redirect("employeedetails")
def dapprove(request,did):
    pro=delivery_registration.objects.get(id=did)
    pro.adminapprove=True
    pro.save()
    return redirect("deliverydetails")
def dreject(request,did):
    pro=delivery_registration.objects.get(id=did)
    pro.adminreject=True
    pro.save()
    return redirect("deliverydetails")

def dpedit(request, aid):
    pro = add_items.objects.get(id=aid)
    if request.method == "POST":
        if 'image' in request.FILES:
            if pro.productimage and os.path.isfile(pro.productimage.path):
                os.remove(pro.productimage.path)
            pro.productimage = request.FILES.get("productimage")

        pro.productname = request.POST.get("productname")
        pro.category = request.POST.get("category")
        pro.price = request.POST.get("price")
        pro.quantity = request.POST.get("quantity")
        pro.description = request.POST.get("description")
        pro.save()

        
        return redirect("viewitems")

    return render(request, "tempadmin/edit.html", {'pro': pro})

def fdel(request, aid):
    pro = add_items.objects.get(id=aid)
    pro.delete()
    return redirect("viewitems")
