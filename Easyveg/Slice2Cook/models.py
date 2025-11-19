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




    






