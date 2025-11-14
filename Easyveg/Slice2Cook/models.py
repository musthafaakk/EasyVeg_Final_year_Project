from django.db import models

class user_registration(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=60)
    password=models.CharField(max_length=10)
    state=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6)
    phonenumber=models.CharField(max_length=10)






