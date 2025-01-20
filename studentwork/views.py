from django.shortcuts import render,redirect
from studentwork.models import student_add_work
from .forms import *
# from staffwork.forms import UpdateStatusForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from staffwork.models import *
from django.db.models import Q

# Create your views here.

@login_required(login_url='/login')
def add_work_student(request):
    if(request.method=='POST'):
        form = StudentWorkAdd(request.POST,request.FILES)
        if form.is_valid():
            student_add_work.objects.create(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                date = datetime.today(),
                start_date = form.cleaned_data['start_date'],
                end_date = form.cleaned_data['end_date'],
                staffid=Register.objects.get(id=request.user.id)
            )
            return redirect('/view_student_work')
    else:
        form = StudentWorkAdd()
    return render(request,'student_add_work.html',{'form':form})

@login_required(login_url='/login')
def view_work_student(request):
    k =request.user.id
    j=Register.objects.get(id=k)
    d=j.department
    a = student_add_work.objects.filter(staffid__department =d)
    search = request.GET.get('search','')
    if search:
        a=a.filter(Q(title__icontains=search))
    return render(request,'view_student_work.html',{'a':a})
    
@login_required(login_url='/login')
def edit_work_student(request,id):
    data = student_add_work.objects.get(id=id)
    if request.method =='POST':
        form = StudentWorkAdd(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect('/view_student_work',{'data':data})
    else:
        form = StudentWorkAdd(instance=data)
        return render(request,'edit_student_work.html',{'form':form})
    
@login_required(login_url='/login')
def delete_work_student(request,id):
    data = student_add_work.objects.get(id=id)
    data.delete()
    return redirect('/view_student_work')

@login_required(login_url='/login')
def Status_updates(request, id):
    data = student_add_work.objects.get(id=id)

    if request.method == 'POST':
        form = StudentUpdateStatusForm(request.POST, request.FILES)
        if form.is_valid():
            data.update_status = form.cleaned_data['update_status']
            data.message = form.cleaned_data['message']
            data.files = form.cleaned_data['files'] 
            data.save()
            return redirect('/update_status_views', {'data': data})
    else:
        form = StudentUpdateStatusForm()

    return render(request, 'update_statuses.html', {'form': form})
  
@login_required(login_url='/login') 
def Status_update_views(request):
    b = student_add_work.objects.all()
    return render(request,'update_status_views.html',{'b':b})

@login_required(login_url='/login')
def Status_edit(request,id):
    data = student_add_work.objects.get(id=id)
    if request.method =='POST':
        form = StudentUpdateStatusForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
        return redirect('/update_status_views',{'data':data})
    else:
        form = StudentUpdateStatusForm(instance=data)
        return render(request,'edit_status.html',{'form':form})
    
@login_required(login_url='/login')
def delete_status(request,id):
    data = student_add_work.objects.get(id=id)
    data.delete()
    return redirect('/update_status_views')
    