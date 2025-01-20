from django.shortcuts import render,redirect
from feedback.models import Feedbacks
from Authentication.models import Register
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def add_feedback(request):
    if(request.method=='POST'):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedbacks.objects.create(
                subject = form.cleaned_data['subject'],
                message = form.cleaned_data['message'],
                uid =  Register.objects.get(id=request.user.id)
            )
        return redirect('/feedback_view')
    else:
        form = FeedbackForm()
        return render(request,'feedback_add.html',{'form':form})
    
@login_required(login_url='/login')
def view_feedback(request):
    a = Feedbacks.objects.all()
    return render(request,'feedback_view.html',{'a':a})

@login_required(login_url='/login')
def response_feedback(request,id):
    data=Feedbacks.objects.get(id=id)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            data.response = form.cleaned_data['response']
            data.status = 'Responded'
            data.save()
        return redirect('/feedback_view',{'data':data})
    else:
        form = ResponseForm()
    return render(request,'feedback_response.html',{'form':form})


    