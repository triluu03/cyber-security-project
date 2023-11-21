from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    suggested_by = models.ForeignKey(User, on_delete=models.CASCADE)

# Fix for Flaw 3: Sensitive Data Exposure: 
# Delete the following model
class UserInfo(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)