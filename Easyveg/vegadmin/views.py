from django.shortcuts import render

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
    return render(request,"tempadmin/logadmin.html")


