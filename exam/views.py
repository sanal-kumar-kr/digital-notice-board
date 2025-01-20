from django.shortcuts import render,redirect
from .forms import *
from exam.models import Exams
from department.models import *
from subject.models import *
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import Q
from classroom.models import Classes
from classallotment.models import *
import random

# Create your views here.
    
@login_required(login_url='/login')
def add_exam(request):
    a = Departments.objects.all()
    b = Semesters.objects.all()
    c = Subjects.objects.all()
    if(request.method == 'POST'):
        try:
            Exams.objects.get(department = Departments.objects.get(id = request.POST['department']),date = request.POST['date'])
            return render(request,'index.html',{'e':True})
        except Exams.DoesNotExist:
            Exams.objects.create(
                examname = request.POST['examname'],
                date = request.POST['date'],
                start_time = request.POST['start_time'],
                end_time = request.POST['end_time'],
                department = Departments.objects.get(id=request.POST['department']),
                semester = Semesters.objects.get(id=request.POST['semester']),
                subject = Subjects.objects.get(id=request.POST['subject'])
            )
        return redirect('/exam_view')
    else:
        return render(request,'exam_add.html',{'a':a,'b':b,'c':c})
    
@login_required(login_url='/login')
def view_exam(request):
    date=datetime.datetime.today()
    a = Exams.objects.all()
    b = Exams.objects.filter(department=request.user.department,date__gte = date)
    c = Exams.objects.filter(department=request.user.department,date__gte = date)
    search = request.GET.get('search','')
    if search:
        a=a.filter(Q(examname__icontains=search))
        b=b.filter(Q(examname__icontains=search))
        c=c.filter(Q(examname__icontains=search))
    
    
    return render(request,'exam_view.html',{'a':a,'b':b,'c':c})

@login_required(login_url='/login')
def delete_exam(request,id):
    data=Exams.objects.get(id=id)
    data.delete()
    return redirect('/exam_view')

@login_required(login_url='/login')
def edit_exam(request,id):
    a=Exams.objects.get(id=id)
    b=Departments.objects.all()
    c=Semesters.objects.all()
    d=Subjects.objects.all()
    if request.method == 'POST':
        a.examname = request.POST['examname']
        a.department = Departments.objects.get(id=request.POST['department'])
        a.semester = Semesters.objects.get(id=request.POST['semester'])
        a.subject = Subjects.objects.get(id=request.POST['subject'])
        a.date = request.POST['date']
        a.start_time = request.POST['start_time']
        a.end_time = request.POST['end_time']
        a.save()
        return redirect('/exam_view')
    return render(request,'exam_edit.html',{'a':a,'b':b,'c':c,'d':d})


@login_required(login_url='/login')
def student_notes(request):
   
    a = Notes.objects.filter(department=request.user.department.id,semester=request.user.semester.id)
    print(request.user.department.id)
    print(request.user.semester.semestername)
    print(a)
    return render(request,'student_notes_view.html',{'a':a})