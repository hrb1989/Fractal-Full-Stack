from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=80)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    city = models.CharField(max_length=50)
