from django import forms
from studentwork.models import *
from staffwork.models import *

class StudentWorkAdd(forms.ModelForm):
    class Meta:
        model = student_add_work
        fields = ['title','description','start_date','end_date']
        widgets = {
            "start_date" : forms.DateInput(attrs={'type':'date','class':'custom-select'}),
            "end_date" : forms.DateInput(attrs={'type':'date','class':'custom-select'}),
            "description" : forms.Textarea(attrs={'class':'contact-input'}),
            "title" : forms.TextInput(attrs={'class':'contact-input'}),
        }
        
STATUS_CHOICES = [
    ('Completed' , 'Completed'),
    ('On Progress' , 'On Progress'),
    ('On Hold' , 'On Hold'),
    ('Not Started' , 'Not Started'),
    ('In Review' , 'In Review'),
] 
           
class StudentUpdateStatusForm(forms.ModelForm):
    files = forms.FileField(required=False)
    class Meta:
        model = student_add_work
        fields = ['update_status','message']
        
        widgets = {
            'update_status' : forms.Select(choices=STATUS_CHOICES,attrs={'class':'custom-select'}),
            'message' : forms.Textarea(attrs={'class':'contact-input'}),
        } 
        