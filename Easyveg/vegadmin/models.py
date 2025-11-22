from django.db import models

class login_admin(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=60)
    password=models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class add_items(models.Model):
    CATEGORY_CHOICES = (
        ('vegetables', 'Vegetables'),
        ('fruits', 'Fruits'),
        ('juices', 'Juices'),
    )

    productname = models.CharField(max_length=30)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    productimage = models.ImageField(upload_to='product_doc', default=True)

    def __str__(self):
        return self.productname

