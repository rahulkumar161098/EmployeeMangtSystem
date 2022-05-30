from django.contrib import admin
from account.models import EmployeeDetails, EmployeeEducations, EmployeeExperiance
from django.contrib.auth.models import Group

# Register your models here.
class EmployeeViews(admin.ModelAdmin):
    list_display=('user', 'emp_code', 'emp_dept', 'emp_dept')
admin.site.register(EmployeeDetails, EmployeeViews)

class EmployeeEducationView(admin.ModelAdmin):
    list_display=('user','course_pg')
admin.site.register(EmployeeEducations,EmployeeEducationView)


class EmployeeExView(admin.ModelAdmin):
    list_display=('user','company1_name')
admin.site.register(EmployeeExperiance,EmployeeExView)

# customize admin panel
admin.site.unregister(Group)
admin.site.site_header= 'Employee Management System'
