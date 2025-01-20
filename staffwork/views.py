from django.shortcuts import render,redirect
from staffwork.models import add_work
from .forms import *
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from studentwork.models import *
from django.db.models import Q
# Create your views here.

from django.shortcuts import get_object_or_404

@login_required(login_url='/login')
def Add_Works(request):
    if request.method == 'POST':
        form = WorkAddForm(request.POST)
        if form.is_valid():
            user_id = request.POST["user"]
            staff_instance = get_object_or_404(Register, id=user_id)
            sem=get_object_or_404(Semesters,id=user_id)
            
            d=add_work.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                date=datetime.today(),
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                staffid=staff_instance,
                semester=sem
            )
            a = Register.objects.get(id=d.staffid.id) 
            a.status="1"
            a.save()
            return redirect('/view_work')
    else:
        form = WorkAddForm()
        a = Register.objects.filter(usertype="2",status=0)
        b = Semesters.objects.all()

    return render(request,'add_work.html',{'form':form,'a':a,'b':b})

@login_required(login_url='/login')
def View_Works(request):
    a = add_work.objects.all()
    b = add_work.objects.filter(staffid=request.user.id)
    search = request.GET.get('search','')
    if search:
        a=a.filter(Q(title__icontains=search))
    return render(request,'view_work.html',{'a':a,'b':b})

@login_required(login_url='/login')
def Edit_work(request,id):
    data = add_work.objects.get(id=id)
    initial_staff_value = data.staffid.id if data.staffid else None
    initial_sem_value = data.semester.id if data.semester else None


    if(request.method == 'POST'):
        j=data.staffid
        o=Register.objects.get(id=j.id)
        o.status="0"
        o.save()
        form = WorkEditForm(request.POST,instance=data)
        if form.is_valid():
            k=data.staffid
            r=Register.objects.get(id=k.id)
            r.status="1"
            r.save()
            form.save()
        return redirect('/view_work')
    else:
        form = WorkEditForm(instance=data,initial={'staff': initial_staff_value,'semestername': initial_sem_value})
        return render(request,'edit_work.html',{'form':form})
        
        
@login_required(login_url='/login')
def delete_work(request,id):
    data = add_work.objects.get(id=id)
    staffid=data.staffid
    k=Register.objects.get(id=staffid.id)
    k.status="0"
    k.save()
    data.delete()
    return redirect('/view_work')
    
@login_required(login_url='/login')
def Status_update(request,id):
    data = add_work.objects.get(id=id)
    staff = data.staffid.id
    print(staff)
    a = Register.objects.get(id=staff)
    if request.method =='POST':
        form = UpdateStatusForm(request.POST)
        if form.is_valid():
            update_status_value = form.cleaned_data['update_status']
            data.update_status = form.cleaned_data['update_status']
            data.message = form.cleaned_data['message']
            if update_status_value == 'Completed':
                a.status = 0
                a.save()
            data.save()
            return redirect('/update_status_view',{'data':data})
    else:
        form = UpdateStatusForm()
    return render(request,'update_status.html',{'form':form})            

@login_required(login_url='/login') 
def Status_update_view(request):
    b = add_work.objects.filter(staffid=request.user.id)
    a = add_work.objects.all()
    return render(request,'update_status_view.html',{'b':b})