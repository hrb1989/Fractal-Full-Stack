from django.db import models

# Create your models here.
class Name(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=30)
    age = models.IntegerField(default=18)

#    def __str__(self):
#        return f"{self.fname} {self.lname}"