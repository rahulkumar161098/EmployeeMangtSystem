from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from account.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method=='POST':
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pwd= request.POST['password']
        data={
            'name': fname,
            'subtitle': lname
        }
        if User.objects.filter(username=email):
            messages.info(request, 'User already exist')
            return render(request, 'register.html', data)
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
            messages.info(request, 'Invalid username/password')
            return render(request, 'login.html', locals())

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
    # print('.................', detail)
    # print('date...............',detail.join_date )
    # user_info={
    #     'detail': detail
    # }

    if request.method=='POST':
        fname= request.POST['fname']
        lname= request.POST['lname']
        ecode= request.POST['e_code']
        edept= request.POST['e_dept']
        edesg= request.POST['e_desg']
        mob= request.POST['e_contact']
        email= request.POST['e_email']
        jdate= request.POST['j_date']
        gen= request.POST['dropdown']
        print('gender  .         ...', gen)

        # set_new_value
        detail.user.first_name=fname
        detail.user.last_name= lname
        detail.user.email= email
        detail.emp_mobile= mob
        detail.emp_code= ecode
        detail.emp_dept= edept
        detail.emp_desg= edesg
        detail.emp_gender= gen

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
    if not request.user.is_authenticated:
        return redirect('login_page')

    user= request.user
    education= EmployeeEducations.objects.get(user=user)
    return render(request, 'education.html', locals())

# edit education funcation
def edit_education(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    user= request.user
    edit_education= EmployeeEducations.objects.get(user=user)

    if request.method== 'POST':
        # pg data (Post Graduation )
        pg_name= request.POST['pg_name']
        pg_clg= request.POST['pg_college']
        pg_year= request.POST['pg_year']
        pg_percent= request.POST['pg_per']
        # ug data (Under Graduation )
        ug_name= request.POST['ug_name']
        ug_clg= request.POST['ug_college']
        ug_year= request.POST['ug_year']
        ug_percent= request.POST['ug_per']
        # SSC data (Senior secondary high school)
        ssc_name= request.POST['ssc_name']
        ssc_clg= request.POST['ssc_college']
        ssc_year= request.POST['ssc_year']
        ssc_pernt= request.POST['ssc_per']
        # hc data (High school)
        hc_clg= request.POST['hc_college']
        hc_year= request.POST['hc_year']
        hc_percent= request.POST['hc_per']


        edit_education.course_pg= pg_name
        edit_education.college_name_pg= pg_clg
        edit_education.pass_year_pg= pg_year
        edit_education.parcentage_pg= pg_percent

        edit_education.course_ug= ug_name
        edit_education.college_name_ug= ug_clg
        edit_education.pass_year_ug= ug_year
        edit_education.parcentage_ug= ug_percent

        edit_education.course_ssc= ssc_name
        edit_education.college_name_scc= ssc_clg
        edit_education.pass_year_ssc= ssc_year
        edit_experiance.parcentage_ssc= ssc_pernt

        edit_education.college_name_hc= hc_clg
        edit_education.pass_year_hc= hc_year
        edit_education.parcentage_hc= hc_percent

        try:
            edit_education.save()
            return redirect('education')
        except:
            return render('edit_educations')

    return render(request, 'edit_education.html', locals())

# change password
def change_emp_password(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    user= request.user
    if request.method== 'POST':
        old_pass= request.POST['old_pass']
        new_pass= request.POST['new_pass']
        try:
            if user.check_password(old_pass):
                user.set_password(new_pass)
                user.save()
                return redirect('logout')
        except:
            return redirect('change_emp_password')

    return render(request, 'change_password.html')


# admin control .......................................................................

def admin_login(request):

    if request.method== 'POST':
        a_name= request.POST['admin_name']
        a_pass= request.POST['admin_password']
        user= authenticate(username=a_name, password= a_pass)
        if user.is_staff:
            login(request,user)
            return redirect('admin_home_page')
        else:
            messages.info(request, 'Invalid creadentials')
            return render(request, 'admin_login.html')

    return render(request, 'admin_login.html')

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    return render(request, 'admin_home.html')


def change_admin_pass(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    user= request.user
    if request.method== 'POST':
        old_pass= request.POST['old_pass']
        new_pass= request.POST['new_pass']
        try:
            if user.check_password(old_pass):
                user.set_password(new_pass)
                user.save()
                return redirect('admin_login')
        except:
            return redirect('change_emp_password')

    return render(request, 'change_admin_pass.html')

def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    all_emp= EmployeeDetails.objects.all()
    return render(request, 'all_employee.html', locals())

def delete_emp(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    all_emp= User.objects.get(id=pid)
    all_emp.delete()
    return redirect('delete_emp')

def emp_all_details(request, id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user= request.user
    # print('user................', user)

    emp_all_detail= EmployeeDetails.objects.get(id= id)

    emp_edu= emp_all_detail.user

    # getting emp eduaction by username
    edu_details= EmployeeEducations.objects.filter(user=emp_edu).get()
    # print('emp educations...............', edu_details)

    # getting emp experiance by username
    emp_exp= EmployeeExperiance.objects.filter(user= emp_edu).get()
    # print('emp experiance.............', emp_exp)

    return render(request, 'emp_all_details.html', locals())

