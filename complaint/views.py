from django.shortcuts import render,redirect
from complaint.models import Complaints
from Authentication.models import Register
from .forms import *
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
@login_required(login_url='/login')
def complaint_add(request):
    if(request.method == 'POST'):
        form = ComplaintForm(request.POST,request.FILES)
        if form.is_valid():
            Complaints.objects.create(
                subject = form.cleaned_data['subject'],
                message = form.cleaned_data['message'],
                uid = Register.objects.get(id=request.user.id)
            )
        return redirect('/add_complaint')
    else:
        form = ComplaintForm()
        return render(request,'add_complaint.html',{'form':form})
 
@login_required(login_url='/login')   
def complaint_views(request):
    a = Complaints.objects.all()
    return render(request,'view_complaint.html',{'a':a})

@login_required(login_url='/login')
def complaint_response(request,id):
    data=Complaints.objects.get(id=id)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            data.response = form.cleaned_data['response']
            data.responsetime = datetime.datetime.now().strftime('%I:%M:%S:%p')
            data.status = 'completed'
            data.respondedby = request.user
            data.save()
            
        return redirect('/view_complaint',{'data':data})
    else:
        form = ResponseForm()
    return render(request,'response_complaint.html',{'form':form})
    
@login_required(login_url='/login')
def complaint_response_view(request):
    a = Complaints.objects.all()
    return render(request,'view_response_complaint.html',{'a':a})

@login_required(login_url='/login')
def complaint_delete(request,id):
    data = Complaints.objects.get(id=id)
    data.delete()
    return redirect('/view_complaint')
            