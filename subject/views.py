from django.shortcuts import render,redirect
from .forms import *
from subject.models import Subjects
from django.contrib.auth.decorators import login_required
from department.models import *
from django.db.models import Q
from django.shortcuts import get_object_or_404

from Authentication.models import *

# Create your views here.

@login_required(login_url='/login')
def add_staff_subject(request):
    a = Departments.objects.all()
    b = Semesters.objects.all()
    c = request.user.id
    d = Register.objects.get(id=c)
    e = d.department
    f = e.id
    print(request.user.department.semesters_set.first().id)
    s=Semesters.objects.filter(department=request.user.department.id)
    print(s)
    if(request.method == 'POST'):
        semester_id = request.POST['semester']

        semester_instance = get_object_or_404(Semesters, id=semester_id)

        Subjects.objects.create(    
            name =request.POST['name'],
            description = request.POST['description'],
            department = e,
            semester = semester_instance
        )
        return redirect('/subject_view')
    else:
        return render(request,'subject_add_staff.html',{'a':a,'b':b,'s':s}) 

@login_required(login_url='/login')
def add_subject(request):
    a = Departments.objects.all()
    b = Semesters.objects.all()
    if(request.method == 'POST'):
        try:
            Subjects.objects.get(department = Departments.objects.get(id=request.POST['department']),name=request.POST['name'])
            return render(request,'subject_add.html',{'d':True})
        except Subjects.DoesNotExist:
            Subjects.objects.create(    
                name =request.POST['name'],
                description = request.POST['description'],
                department = Departments.objects.get(id=request.POST['department']),
                semester = Semesters.objects.get(id=request.POST['semester'])
            )
        return redirect('/subject_view')
    else:
        return render(request,'subject_add.html',{'a':a,'b':b}) 

@login_required(login_url='/login')
def view_subject(request):
    a = Subjects.objects.all()
    b = Subjects.objects.filter(department=request.user.department)
    search = request.GET.get('search','')
    if search:
        a=a.filter(Q(name__icontains=search)|Q(department__departmentname__icontains=search))
        b=b.filter(Q(name__icontains=search))
    return render(request,'subject_view.html',{'a':a,'b':b})
    
@login_required(login_url='/login')
def delete_subject(request,id):
    data = Subjects.objects.get(id=id)
    data.delete()
    return redirect('/subject_view')

@login_required(login_url='/login')
def edit_subject(request,id):
    a = Subjects.objects.get(id=id)
    b = Departments.objects.all()
    c = Semesters.objects.all()
    if request.method == 'POST':
            a.name = request.POST['name']
            a.description = request.POST['description']
            a.department = Departments.objects.get(id=request.POST['department'])
            a.semester = Semesters.objects.get(id=request.POST['semester'])
            a.save()
            return redirect('/subject_view')
    return render(request,'subject_edit.html',{'a':a,'b':b,'c':c})

@login_required(login_url='/login')
def add_notes(request):
    print(request.method == 'POST')
    if request.method == 'POST':
        form = NotesAddForm(request.POST, request.FILES)       
        print(form.is_valid())
        if form.is_valid():
            Notes.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                staffid=Register.objects.get(id=request.user.id),
                notes=form.cleaned_data['notes'],
                department=Departments.objects.get(id=request.user.department.id),
                semester=Semesters.objects.get(id=request.POST['semester'])
                
               
                
            )
            print("hellooo1234")   
            return redirect('/view_notes')
        
    else:
        print("hiiiiiiiiiiii")   

        form = NotesAddForm()
        print(request.user.department.id)
        b=Semesters.objects.filter(department=request.user.department.id)


    return render(request, 'add_notes.html', {'form': form,'b':b})
    

@login_required(login_url='/login')
def view_notes(request):
    a = Notes.objects.filter(staffid=request.user)
    return render(request,'view_notes.html',{'a':a}) 

@login_required(login_url='/login')
def edit_notes(request,id):
    
    if request.method == 'POST':
        form = NotesAddForm(request.POST, request.FILES)
        print(request.POST)
       
        print( form.is_valid())
        if form.is_valid():
           
        
            nid = Notes.objects.get(id=id)
            nid.title=form.cleaned_data['title']
            nid.description=form.cleaned_data['description']
            nid.notes=form.cleaned_data['notes']

            nid.save()

            print("hellooo1234")   
            return redirect('/view_notes')
        
    else:
        


        note_instance = Notes.objects.get(id=id)
        form = NotesAddForm(request.POST or None, request.FILES or None, instance=note_instance)

    return render(request,'add_notes.html', {'form': form})

@login_required(login_url='/login')
def delete_notes(request,id):
    a = Notes.objects.filter(id=id)
    a.delete()
    return redirect('/view_notes')

    

