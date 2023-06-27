from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    def __str__(self):
        return self.name