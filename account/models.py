
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmployeeDetails(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    email= models.CharField(max_length=50, null=True)
    mobile= models.IntegerField(max_length=12, null=True)
    emp_code= models.CharField(max_length=60, null=True)
    emp_dept =models.CharField(max_length=60, null=True)
    emp_dept= models.CharField(max_length=60, null=True)
    gender= models.CharField(max_length=10, null=True)
    join_date= models.DateField(null=True)

    # def __str__(self):
    #     return self.emp_code
