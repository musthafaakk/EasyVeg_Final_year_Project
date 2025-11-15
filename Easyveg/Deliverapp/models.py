from django.db import models

class delivery_registration(models.Model):
    fullname=models.CharField(max_length=30)
    email=models.EmailField(max_length=60)
    phonenumber=models.CharField(max_length=10)
    address=models.CharField(max_length=80)
    time=models.CharField( max_length=50)
    license=models.CharField(max_length=40)
    password=models.CharField(max_length=15)
    adminapprove=models.BooleanField(default=False)
    adminreject=models.BooleanField(default=False)

    def __str__(self):
        return self.fullname

    

    
     


# Create your models here.
