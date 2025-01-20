from django.shortcuts import render,redirect
from .forms import *
from classroom.models import Classes
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required(login_url='/login')
def add_classroom(request):
    if(request.method=='POST'):
        form = Classroomaddform(request.POST,request.FILES)
        try:
            Classes.objects.get(classname=request.POST['classname'])
            return render(request,'classroom_add.html',{'form':form,'c':True})
        except Classes.DoesNotExist:
            if form.is_valid():
                a = form.cleaned_data['seatrows']
                b = form.cleaned_data['seatcolumns']
                Classes.objects.create(
                    classname = form.cleaned_data['classname'],
                    seatrows = form.cleaned_data['seatrows'],
                    seatcolumns = form.cleaned_data['seatcolumns'],
                    strength = a*b
                )
            return redirect('/classroom_view')
    else:
        form = Classroomaddform()
        return render(request,'classroom_add.html',{'form':form})
    
@login_required(login_url='/login')
def view_classroom(request):
    a = Classes.objects.all()
    search = request.GET.get('search','')
    if search:
        a=a.filter(Q(classname__icontains=search))
    return render(request,'classroom_view.html',{'a':a})

@login_required(login_url='/login')
def edit_classroom(request,id):
    data = Classes.objects.get(id=id)
    if(request.method == 'POST'):
        form = Classroomaddform(request.POST,instance=data)
        if form.is_valid():
            a = form.cleaned_data['seatrows']
            b = form.cleaned_data['seatcolumns']
            data.strength = a*b
            form.save()
        return redirect('/classroom_view',{'data':data})
    else:
        form = Classroomaddform(instance=data)
        return render(request,'classroom_edit.html',{'form':form})
    
@login_required(login_url='/login')
def delete_classroom(request,id):
    a = Classes.objects.get(id=id)
    a.delete()
    return redirect('/classroom_view')