from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=255)
    password = models.CharField(max_length=10)
    comfirm_password = models.CharField(null = True ,max_length=10)
    
    def __str__(self):
        f"{self.email}({self.phoneNumber})"
    
