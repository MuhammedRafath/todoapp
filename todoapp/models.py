from django.db import models

# Create your models here.
class todoapp (models.Model):
    taskname=models.CharField(max_length=100)
    date=models.DateField()
    