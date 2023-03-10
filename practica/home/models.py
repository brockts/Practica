from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)