from django.shortcuts import render,redirect
from .forms import *
from .models import *
from notification.models import Notifications
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mass_mail
from django.conf import settings
from Authentication.models import Register
# Create your views here.


@login_required(login_url='/login')
def add_admin_notification(request):  
    if(request.method == 'POST'):
        a = Register.objects.filter(usertype=2)
        form = NotificationAddForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Notifications.objects.create(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                date = datetime.today(),
                start_date = form.cleaned_data['start_date'],
                end_date = form.cleaned_data['end_date'],
                usertype = form.cleaned_data['usertype']
            )
            for i in a:
                    email=i.email
                    subject = "The Notification By DigitalNoticeBoard"
                    message = str(title) + str(description)
                    email_from = settings.EMAIL_HOST_USER
                    recepient_list = [email]
                    messages = [(subject,message,email_from,recepient_list)]
                    send_mass_mail(messages)
        return redirect('/notification_admin_view')
    else:
        form = NotificationAddForm()
        return render(request,'notification_admin_add.html',{'form':form})
    
def view_admin_notification(request):
    date = datetime.today()
    a = Notifications.objects.all()
    b = Notifications.objects.filter(usertype=2)
    c = Notifications.objects.filter(usertype=3)
    d = Notifications.objects.filter(usertype="None")
    e = StudentNotifications.objects.all()

    if request.method == 'POST':
        usertype = request.POST.get('usertype')
        if usertype == "None":
            d = Notifications.objects.filter(usertype="None")
            return render(request,'notification_admin_view.html',{'a': d })
        elif usertype == "2":
            b = Notifications.objects.filter(usertype="2")
            
            return render(request, 'notification_admin_view.html', {'a': b })
        elif usertype == "3":
            c = Notifications.objects.filter(usertype="3")
            e = StudentNotifications.objects.all()
            print(e)
            return render(request, 'notification_admin_view.html', {'a': c ,'e':e})
    return render(request, 'notification_admin_view.html', {'a': a, 'b': b, 'c': c, 'd': d,'e':e})
   

@login_required(login_url='/login')
def add_staff_notification(request):
    if(request.method == 'POST'):
        a = Register.objects.filter(usertype=3)
        form = StaffNotificationAddForm(request.POST)
        if form.is_valid(): 
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']           
            StudentNotifications.objects.create(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                start_date = form.cleaned_data['start_date'],
                end_date = form.cleaned_data['end_date'],
                # usertype = form.cleaned_data['usertype'],
                date = datetime.today(),
                staffid=Register.objects.get(id=request.user.id)
            )
            for i in a:
                email=i.email
                subject = "The Notification By DigitalNoticeBoard"
                message = str(title) + str(description)
                email_from = settings.EMAIL_HOST_USER
                recepient_list = [email]
                messages = [(subject,message,email_from,recepient_list)]
                send_mass_mail(messages)
        return redirect('/notification_admin_view')
    else:
        form = StaffNotificationAddForm()
        return render(request,'notification_staff_add.html',{'form':form})
    
    
# @login_required(login_url='/login')
# def add_admin_staff_notification(request):  
#     if(request.method == 'POST'):
#         form = StaffNotificationAddForm(request.POST)
#         if form.is_valid():
#             StaffNotifications.objects.create(
#                 title = form.cleaned_data['title'],
#                 description = form.cleaned_data['description'],
#             )
#         return redirect('/notification_admin_view')
#     else:
#         form = StaffNotificationAddForm()
#         return render(request,'notification_admin_add_staff.html',{'form':form})
    
    
# @login_required(login_url='/login')
# def add_admin_student_notification(request):  
#     if(request.method == 'POST'):
#         a = Register.objects.filter(usertype=2)
#         form = StaffNotificationAddForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             description = form.cleaned_data['description']
#             StudentNotifications.objects.create(
#                 title = form.cleaned_data['title'],
#                 description = form.cleaned_data['description'],
#                 date = datetime.today(),
#                 start_date = form.cleaned_data['start_date'],
#                 end_date = form.cleaned_data['end_date'],
#             )
#             for i in a:
#                     email=i.email
#                     subject = "The Notification By DigitalNoticeBoard"
#                     message = str(title) + str(description)
#                     email_from = settings.EMAIL_HOST_USER
#                     recepient_list = [email]
#                     messages = [(subject,message,email_from,recepient_list)]
#                     send_mass_mail(messages)
#         return redirect('/notification_admin_view')
#     else:
#         form = StaffNotificationAddForm()
#         return render(request,'notification_admin_add_student.html',{'form':form})

 
@login_required(login_url='/login')
def edit_notification(request,id):
    data = Notifications.objects.get(id=id)
    if request.method == 'POST':
        form = NotificationAddForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect("/notification_admin_view",{'data':data})
    else:
        form = NotificationAddForm(instance=data)
        return render(request,'notification_edit.html',{'form':form})
    
@login_required(login_url='/login')
def edit_staffnotification(request,id):
    data = StudentNotifications.objects.get(id=id)
    if request.method == 'POST':
        form = StaffNotificationAddForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect("/notification_admin_view",{'data':data})
    else:
        form = StaffNotificationAddForm(instance=data)
        return render(request,'notification_staffedit.html',{'form':form})
    
@login_required(login_url='/login')
def delete_notification(request,id):
    data = Notifications.objects.get(id=id)
    data.delete()
    return redirect('/notification_admin_view')
    
@login_required(login_url='/login')
def delete_staffnotification(request,id):
    data = StudentNotifications.objects.get(id=id)
    data.delete()
    return redirect('/notification_admin_view')
    
