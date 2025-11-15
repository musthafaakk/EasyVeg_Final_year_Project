from django.db import models

class login_admin(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=60)
    password=models.CharField(max_length=25)

    def __str__(self):
        return self.name
