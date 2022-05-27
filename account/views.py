from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from account.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method=='POST':
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pwd= request.POST['password']
        try:
            save_login= User.objects.create_user(first_name= fname, last_name= lname, username=email, password= pwd, email=email)
            save_login.save()
            EmployeeDetails.objects.create(user=save_login)
            return redirect('login_page')
        except:
            return render(request, 'register.html')
    return render(request, 'register.html')

def user_login(request):
    if request.method== 'POST':
        uname= request.POST['username']
        pwd= request.POST['password']
        user= authenticate(username=uname, password= pwd)
        if user is not None:
            login(request, user)
            return redirect('emp_base')
        else:
            return HttpResponse(' not login')

    return render(request, 'login.html')

def userLogOut(request):
    logout(request)
    return redirect('login_page')


def emp(request):
    if not request.user.is_authenticated:
        return redirect ('login_page')
    return render(request, 'emp_home.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect ('login_page')
    user= request.user
    detail= EmployeeDetails.objects.get(user=user)
    print('.................', detail)
    user_info={
        'detail': detail
    }

    if request.method=='POST':
        fname= request.POST['fname']
        lname= request.POST['lname']
        ecode= request.POST['e_code']
        edept= request.POST['e_dept']
        edesg= request.POST['e_desg']
        econtact= request.POST['e_contact']
        email= request.POST['e_email']
        jdate= request.POST['j_date']
        # e_gender= request.POST['e_gender']

        if jdate:
            EmployeeDetails.join_date=jdate


        try:
            save_login= User.objects.create_user(first_name= fname, last_name= lname, username=email, email=email)
            save_login.save()
            EmployeeDetails.objects.create(user=save_login, email=email, mobile=econtact, emp_code=ecode, emp_dept=edept, join_date=jdate)
            return redirect('login_page')
        except:
            return render(request, 'profile.html')

    return render(request, 'profile.html', user_info)