from django.contrib import admin
from account.models import EmployeeDetails
from django.contrib.auth.models import Group

# Register your models here.
class EmployeeViews(admin.ModelAdmin):
    list_display=('user', 'emp_code', 'emp_dept', 'emp_dept')
admin.site.register(EmployeeDetails, EmployeeViews)

# customize admin panel
admin.site.unregister(Group)
admin.site.site_header= 'Employee Management System'
