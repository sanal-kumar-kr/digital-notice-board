from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import *
from Authentication.models import Register
from django.core.mail import send_mail
from django.conf import settings
import secrets
import string
from django.db.models import Q
import datetime
from notification.models import *

def index(request):
    ef = Departments.objects.all()
    ab = Notifications.objects.filter(usertype = "None").order_by('-start_date')[:3]
    de = Notifications.objects.order_by('-start_date')[:3]
    bc = Notifications.objects.filter(usertype = 2).order_by('-start_date')[:3]
    cd = Notifications.objects.filter(usertype = 3).order_by('-start_date')[:3]
    return render(request, 'index.html',{'ab':ab,'bc':bc,'cd':cd,'de':de,'ef':ef})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

@login_required(login_url='/login')
def add_staff(request):
    if request.method=='POST':
        form = StaffRegisterForm(request.POST,request.FILES)
        try:
            Register.objects.get(username=request.POST['email'])
            return render(request,'add_staff.html',{'form':form,'z':True})
        except Register.DoesNotExist:
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                
                Register.objects.create_user(
                    name = form.cleaned_data["name"],
                    email = form.cleaned_data["email"],
                    password = form.cleaned_data["password"],
                    username = form.cleaned_data["email"],
                    contact = form.cleaned_data["contact"],
                    address = form.cleaned_data["address"],
                    gender = form.cleaned_data["gender"],
                    department = form.cleaned_data["department"],
                    experience = form.cleaned_data["experience"],
                    qualification = form.cleaned_data["qualification"],
                    usertype = "2"
                    )
                subject = 'You are register Successfully By Admin'
                message = 'Your Password Is' +str(password)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                
                send_mail(subject,message,email_from,recipient_list)
                return render(request,'index.html',{'form':form ,'y':True})
    else:
        form = StaffRegisterForm()
    return render(request,'add_staff.html',{'form':form})

@login_required(login_url='/login')
def add_student(request):
    a = Departments.objects.filter()
    b = Semesters.objects.all()
    if(request.method=='POST'):
        form = StudentRegisterForm(request.POST,request.FILES)
        try:
            Register.objects.get(username=request.POST['email'])
            return render(request,'add_student.html',{'form':form,'x':True})
        except Register.DoesNotExist:
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                # department = form.cleaned_data["department"]
                # semester = form.cleaned_data["semester"]
                department_id = request.POST["department"]
                semester_id = request.POST["semester"]
                department = Departments.objects.get(id=department_id)
                semester = Semesters.objects.get(id=semester_id)

                regno = form.cleaned_data["regno"]
                Register.objects.create_user(
                    username = form.cleaned_data["email"],
                    name = form.cleaned_data["name"],
                    regno = form.cleaned_data["regno"],
                    email = form.cleaned_data["email"],
                    gender = form.cleaned_data["gender"],
                    department = department,
                    semester =semester,
                    dob = form.cleaned_data["dob"],
                    address = form .cleaned_data["address"],
                    contact = form.cleaned_data["contact"],
                    password = form.cleaned_data["password"],
                    usertype = "3"
                )
                subject = 'You Are Registered Successfully By Staff'
                message = "your password is " + str(password) + " your department is " + str(department) + " your semester is " + str(semester) + " Your Register Number is " + str(regno)
                email_from = settings.EMAIL_HOST_USER
                recepient_list = [email]
                send_mail(subject,message,email_from,recepient_list)
                return render(request,'index.html',{'form':form,'x':True})
    else:
      
        form = StudentRegisterForm()
    return render(request,'add_student.html',{'form':form,'a':a,'b':b})
from django.core.exceptions import ObjectDoesNotExist

def doLogin(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'login.html', {'form': form, 'k': True})
        else:
            try:
                data = Register.objects.get(username=username)
                request.session['ut'] = data.usertype
                request.session['userid'] = data.id
                login(request, user)
                return redirect('/')
            except ObjectDoesNotExist:
                # Handle the case where no matching record is found
                return render(request, 'login.html', {'form': form, 'k': True})

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login')
def doLogout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/login')
def view_staff(request):
    a = Register.objects.filter(usertype="2")
    search = request.GET.get('search', '')
    if search:
        a = a.filter(Q(name__icontains=search)|Q(email__icontains=search)|Q(department__departmentname__icontains=search))
        print(a)
    return render(request,'view_staff.html',{'a':a})

@login_required(login_url='/login')
def view_student(request):
    a = Register.objects.filter(usertype="3")
    search = request.GET.get('search', '')
    b = Register.objects.filter(usertype="3").filter(department=request.user.id)
    if search:
        a = a.filter(Q(name__icontains=search)|Q(email__icontains=search)|Q(department__departmentname__icontains=search))
        print(a)
    return render(request,'view_student.html',{'a':a,'b':b})

@login_required(login_url='/login')
def edit_staff(request,id):
    data = Register.objects.get(id=id)
    if request.method == 'POST':
        form = StaffRegisterEditForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect("/view_staff",{'data':data})
    else:
        form = StaffRegisterEditForm(instance=data)
    return render(request,'edit_staff.html',{'form':form})

@login_required(login_url='/login')
def delete_staff(request,id):
    data=Register.objects.get(id=id)
    data.delete()
    return redirect("/view_staff")

@login_required(login_url='/login')
def edit_student(request,id):
    data=Register.objects.get(id=id)
    if request.method == 'POST':
        form = StudentRegisterEditForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect('/view_student',{'data':data})
    else:
        form = StudentRegisterEditForm(instance=data)
    return render(request,'edit_student.html',{'form':form})

@login_required(login_url='/login')
def delete_student(request,id):
    data=Register.objects.get(id=id)
    data.delete()
    return redirect("/view_student")

@login_required(login_url='/login')
def staff_profile_update(request):
    data = Register.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = StaffRegisterEditForm(request.POST,instance=data)
        if form.is_valid():
            # data.set_password(request.POST["password"])
            # data.save()
            form.save()
        return redirect("/")
    else:
        form = StaffRegisterEditForm(instance=data)
    return render(request,'update_profile_staff.html',{'form':form})

@login_required(login_url='/login')
def student_profile_update(request):
    data = Register.objects.get(id=request.user.id)
    if request.method =='POST':
        form = Studentprofileedit(request.POST,instance=data)
        if form.is_valid():
            # data.set_password(request.POST['password'])
            # data.save()
            form.save()
        return redirect('/')
    else:
        form = Studentprofileedit(instance=data)
    return render(request,'update_profile_student.html',{'form':form})

@login_required(login_url='/login')
def staff_profile_view(request):
    a = Register.objects.filter(id=request.user.id)
    return render(request,'view_profile_staff.html',{'a':a})

@login_required(login_url='/login')
def student_profile_view(request):
    a = Register.objects.filter(id=request.user.id)
    return render(request,'view_profile_student.html',{'a':a})

@login_required(login_url='/login')
def admin_profile_view(request):
    a = Register.objects.filter(id=request.user.id)
    return render(request,'view_profile_admin.html',{'a':a})

def password_forgot(request):
    if request.method=="POST":
        form = ForgotForm(request.POST, request.FILES)
        try:
            x = Register.objects.get(email=request.POST['email'])
            if form.is_valid():
                password_length = 6
                print(secrets.token_urlsafe(password_length))
                password=secrets.token_urlsafe(password_length)
                subject = 'YOUR NEW PASSWORD'
                message = password
                print(message)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [x.email]
                send_mail(subject,message,email_from,recipient_list)
                form=LoginForm()
                x.set_password(password)
                x.save()
            return render(request,'index.html',{'o':True,'form':form})
        except Register.DoesNotExist:
            return render(request,'index.html',{'n':True}) 
    else:
        form = ForgotForm()
    return render(request,'forgot_password.html',{'form':form})
    
@login_required(login_url='/login')
def password_reset(request):
    data = Register.objects.get(id=request.user.id)
    print(data)
    if request.method =='POST':
        form = UpdatePasswordForm(request.POST,instance=data)
        if form.is_valid():
            data.set_password(request.POST['password'])
            data.save()
            form.save()
        return redirect('/login',{'data':data})
    else:
        form = UpdatePasswordForm()
    return render(request,'admin_reset_password.html',{'form':form})

