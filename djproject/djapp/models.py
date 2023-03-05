from django.db import models

# Create your models here.

class Student(models.Model):
    # student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default=None)
    last_name =  models.CharField(max_length=50, default=None)
    address =  models.CharField(max_length=255, default=None)
    age = models.PositiveSmallIntegerField(default=None)
