"""EmpManagementSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index_page"),
    path('register/', register, name='register_page'),
    path('login/', user_login, name='login_page'),
    path('logout/', userLogOut, name='logout'),
    path('emp/', emp, name='emp_base'),
    path('profile/', profile, name="user_profile"),
    path('emp_experiance/', emp_experiance, name='emp_experiance'),
    path('edit_experiance/', edit_experiance, name="edit_experiance"),
    path('education/', education, name="education"),
    path('edit_education/', edit_education, name="edit_educations"),
    path('change_password/', change_emp_password, name="change_emp_password"),
    # admin url
    path('adminc/', admin_login, name="admin_login"),
    path('admin_home/', admin_home, name="admin_home_page"),
    path('change_admin_password/', change_admin_pass, name="change_admin_pass"),
    path('all_employee/', all_employee, name="all_employee"),
    path('delete_emp/<int:pid>', delete_emp, name="delete_emp"),
    path('emp_all_details/<int:id>', emp_all_details, name="emp_all_details")
]
