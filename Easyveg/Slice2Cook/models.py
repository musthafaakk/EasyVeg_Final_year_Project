from django.db import models
from vegadmin.models import*
from django.utils import timezone

class user_registration(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=60)
    password=models.CharField(max_length=10)
    state=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6)
    phonenumber=models.CharField(max_length=10)


    def __str__(self):
        return self.name
    
class employee_registration(models.Model):
        firstname=models.CharField(max_length=15)
        lastname=models.CharField(max_length=15)
        phonenumber=models.CharField(max_length=10)
        email=models.EmailField(max_length=70)
        idproof=models.ImageField(upload_to='idproof',default=True)
        username=models.CharField(max_length=20)
        password=models.CharField(max_length=20)
        address=models.CharField(max_length=60)
        adminapprove=models.BooleanField(default=False)
        adminreject=models.BooleanField(default=False)

        def __str__(self):
            return self.firstname



class user_booking(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE)
    product = models.ForeignKey(add_items, on_delete=models.CASCADE)
    booking_date = models.DateField(default=timezone.now)
    delivery_date = models.DateField()
    quantity = models.CharField(max_length=10, null=True)
    suggestions = models.CharField(max_length=100, null=True)
    amount = models.CharField(max_length=10)
    status = models.BooleanField(default=False)
    payment_status = models.BooleanField(default=False)


    def __str__(self):
        return f"Booking by {self.user.name} on {self.booking_date}"


