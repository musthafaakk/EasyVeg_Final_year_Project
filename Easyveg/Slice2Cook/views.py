from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def userlog(request):
    return render(request,"user/userlog.html")
def userreg(request):
    return render(request,"user/userreg.html")
def userhome(request):
    return render(request,"user/userhome.html")
def emplog(request):
    return render(request,"employee/emplog.html")
def empreg(request):
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


                                                     



