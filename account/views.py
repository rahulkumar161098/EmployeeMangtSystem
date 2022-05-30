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
            EmployeeEducations.objects.create(user=save_login)
            EmployeeExperiance.objects.create(user=save_login)
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
    print('mobile.............', detail.emp_mobile)
    print('mobile.............', detail.emp_code)
    print('.................', detail)
    print('date...............',detail.join_date )
    # user_info={
    #     'detail': detail
    # }

    if request.method=='POST':
        fname= request.POST['fname']
        lname= request.POST['lname']
        ecode= request.POST['e_code']
        edept= request.POST['e_dept']
        edesg= request.POST['e_desg']
        econtact= request.POST['e_contact']
        print('con........', econtact)
        email= request.POST['e_email']
        jdate= request.POST['j_date']
        gender= request.POST.get('emp_gender')
        print('gender  .         ...', gender)

        # set_new_value
        detail.user.first_name=fname
        detail.user.last_name= lname
        detail.user.email= email
        detail.emp_mobile= econtact
        detail.emp_code= ecode
        detail.emp_dept= edept
        detail.emp_desg= edesg
        detail.emp_gender= gender

        if jdate:
            detail.join_date=jdate
        print('date...............',detail.join_date )
        try:
            detail.save()
            detail.user.save()
            return redirect('emp_base')
        except:
            return render(request, 'profile.html')

    return render(request, 'profile.html', locals())

def emp_experiance(request):
    if not request.user.is_authenticated:
        return redirect ('login_page')
    user= request.user
    experiance= EmployeeExperiance.objects.get(user=user)
    print('...............', experiance.company1_name)
    print('current user..............', experiance)
    
    return render(request, 'emp_experiance.html', locals())

def edit_experiance(request):
    if not request.user.is_authenticated:
        return redirect ('login_page')
    user= request.user
    edit_exp= EmployeeExperiance.objects.get(user=user)
    if request.method== 'POST':
        c1= request.POST['c_name1']
        c1_desg= request.POST['c_name1_desg']
        c1_exp= request.POST['c_name1_exp']
        c2= request.POST['c_name2']
        c2_desg= request.POST['c_name2_desg']
        c2_exp= request.POST['c_name2_exp']
        c3= request.POST['c_name3']
        c3_desg= request.POST['c_name3_desg']
        c3_exp= request.POST['c_name3_exp']

        edit_exp.company1_name= c1
        edit_exp.company1_desg= c1_desg
        edit_exp.company1_duration= c1_exp
        edit_exp.company2_name= c2
        edit_exp.company2_desg= c2_desg
        edit_exp.company2_duration= c2_exp
        edit_exp.company3_name= c3
        edit_exp.company3_desg= c3_desg
        edit_exp.company3_duration= c3_exp
        print(edit_exp.company1_name)
        print(edit_exp.company2_name)
        print(edit_exp.company2_name)
        try:
            edit_exp.save()
            return redirect('emp_experiance')
        except:
            return render(request, 'edit_experiance.html')

    return render(request, 'edit_experiance.html', locals())


# education function
def education(request):
    return render(request, 'education.html')

# edit education funcation
def edit_education(request):
    return render(request, 'edit_eduaction')