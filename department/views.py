from django.shortcuts import render,redirect
from department.models import Departments
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required(login_url='/login')
def department_add(request):
    print("hellooo")
    if(request.method=='POST'):
        form = departmentaddform(request.POST,request.FILES)
        try:
            Departments.objects.get(departmentname=request.POST['departmentname'])
            return render(request,'add_department.html',{'form':form,'c':True})
        except Departments.DoesNotExist:
            if form.is_valid():
                print("hellooo123")
               
                Departments.objects.create(
                    departmentname = form.cleaned_data['departmentname'],
                    description = form.cleaned_data['description'],
                    departmentimage=form.cleaned_data['departmentimage']
                )
              
              
            return redirect('/view_department')
    else:
        form = departmentaddform()
        return render(request,'add_department.html',{'form':form})
               
def department_view(request):
    a = Departments.objects.all()
    search = request.GET.get('search','')
    print(a)
    if search:
        a=a.filter(Q(departmentname__icontains=search))
    return render(request,'view_department.html',{'a':a})

@login_required(login_url='/login')
def department_edit(request,id):
    data = Departments.objects.get(id=id)
    if request.method == 'POST':
        form = departmentaddform(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect("/view_department",{'data':data})
    else:
        form = departmentaddform(instance=data)
        return render(request,'edit_department.html',{'form':form})

@login_required(login_url='/login')   
def department_delete(request,id):
    data = Departments.objects.get(id=id)
    data.delete()
    return redirect('/view_department')

@login_required(login_url='/login')
def semester_add(request):
    if(request.method=='POST'):
        form = SemesterAddForm(request.POST)
        try:
            Semesters.objects.get(semestername=request.POST['semestername'],department=request.POST['department'])
            return render(request,'add_semester.html',{'form':form,'c':True})
        except Semesters.DoesNotExist:
            if form.is_valid():
                Semesters.objects.create(
                    department = form.cleaned_data['department'],
                    semestername = form.cleaned_data['semestername']
                )
            return redirect('/view_semester')
    else:
        form = SemesterAddForm()
        return render(request,'add_semester.html',{'form':form})
    
@login_required(login_url='/login')
def semester_view(request):
    a = Semesters.objects.all()
    return render(request,'view_semester.html',{'a':a})

@login_required(login_url='/login')
def semester_edit(request,id):
    data = Semesters.objects.get(id=id)
    if request.method == 'POST':
        form = SemesterAddForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect("/view_semester",{'data':data})
    else:
        form = SemesterAddForm(instance=data)
        return render(request,'edit_semester.html',{'form':form})

@login_required(login_url='/login')   
def semester_delete(request,id):
    data = Semesters.objects.get(id=id)
    data.delete()
    return redirect('/view_semester')