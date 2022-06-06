
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmployeeDetails(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    # email= models.CharField(max_length=50, null=True)
    emp_code= models.CharField(max_length=60, null=True)
    emp_dept =models.CharField(max_length=60, null=True)
    emp_desg= models.CharField(max_length=60, null=True)
    emp_mobile= models.CharField(max_length=12, null=True)
    join_date= models.DateField(null=True)
    emp_gender= models.CharField(max_length=10, null=True)

    # def __str__(self):
    #     return self.user


# education model fo employee
class EmployeeEducations(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    # pg (Post Graduation )
    course_pg= models.CharField(max_length=200, null=True)
    college_name_pg =models.CharField(max_length=200, null=True)
    pass_year_pg= models.CharField(max_length=60, null=True)
    parcentage_pg= models.CharField(max_length=50, null=True)
    # ug (Under Graduation )
    course_ug= models.CharField(max_length=200, null=True)
    college_name_ug =models.CharField(max_length=200, null=True)
    pass_year_ug= models.CharField(max_length=60, null=True)
    parcentage_ug= models.CharField(max_length=50, null=True)
    # ssc(Senior secondary high school)
    course_ssc= models.CharField(max_length=200, null=True)
    college_name_scc =models.CharField(max_length=200, null=True)
    pass_year_ssc= models.CharField(max_length=60, null=True)
    parcentage_ssc= models.CharField(max_length=50, null=True)
    # hc (High school)
    course_hc= models.CharField(max_length=200, null=True)
    college_name_hc =models.CharField(max_length=200, null=True)
    pass_year_hc= models.CharField(max_length=60, null=True)
    parcentage_hc= models.CharField(max_length=50, null=True)

    # def __str__(self):
    #     return  self.user


# employee experiance
class EmployeeExperiance(models.Model):
    user= models.ForeignKey(User ,on_delete=models.CASCADE)
    # company 1
    company1_name= models.CharField(max_length=200, null=True)
    company1_desg =models.CharField(max_length=200, null=True)
    company1_duration= models.CharField(max_length=60, null=True)
    # company 2
    company2_name= models.CharField(max_length=200, null=True)
    company2_desg =models.CharField(max_length=200, null=True)
    company2_duration= models.CharField(max_length=60, null=True)
    # compamy 3
    company3_name= models.CharField(max_length=200, null=True)
    company3_desg =models.CharField(max_length=200, null=True)
    company3_duration= models.CharField(max_length=60, null=True)

    # def __str__(self):
    #     return  self.user