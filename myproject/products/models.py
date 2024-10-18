from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name