from django.shortcuts import render
def deliverylog(request):
    return render(request,'delivery/deliverylog.html')
def deliveryreg(request):
    return render(request,'delivery/deliveryreg.html')
def deliveryhome(request):
    return render(request,'delivery/deliveryhome.html')
def about(request):
    return render(request,'navbar/about.html')
def profile1(request):
    return render(request,'navbar/profile1.html')

# Create your views here.
