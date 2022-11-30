from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=100, decimal_places=2)
    grade = models.DecimalField(max_digits=5, decimal_places=1)