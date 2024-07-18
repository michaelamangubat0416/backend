from django.db import models

# Create your models here.

class Item(models.Model):
    sname = models.CharField(max_length=100, blank=True, null=True)
    fname = models.CharField(max_length=100, blank=True, null=True)
    mname = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    
