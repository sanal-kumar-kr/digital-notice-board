from django import forms
from staffwork.models import *
from department.models import *

class WorkAddForm(forms.ModelForm):
    # staffid = forms.ModelChoiceField(queryset=Register.objects.filter(usertype="2",status=0))
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['staffid'].widget.attrs['class'] = 'custom-select'
    
  
       

    class Meta:
        model = add_work
        fields = ['title','description','start_date','end_date']
        widgets = {
            
            "title" : forms.TextInput(attrs={'class':'contact-input'}),            
            "start_date" : forms.DateInput(attrs={'type':'date','class':'custom-select'}),            
            "date" : forms.DateInput(attrs={'type':'date','class':'custom-select'}),
            "end_date" : forms.DateInput(attrs={'type':'date','class':'custom-select'}),            
            "description" : forms.Textarea(attrs={'class':'contact-input'}),            
        }
        
class WorkEditForm(forms.ModelForm):
    staff = forms.ModelChoiceField(queryset=Register.objects.filter(usertype="2"))
    semestername = forms.ModelChoiceField(queryset=Semesters.objects.all())


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['staff'].widget.attrs['class'] = 'custom-select'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['semestername'].widget.attrs['class'] = 'custom-select'     
    class Meta:
        model = add_work
        fields = ['title','description','start_date','end_date']
        widgets = {
            
            "title" : forms.TextInput(attrs={'class':'contact-input'}),            
            "start_date" : forms.DateInput(attrs={'type':'date','class':'custom-select'}),            
            "date" : forms.DateInput(attrs={'type':'date','class':'custom-select'}),
            "end_date" : forms.DateInput(attrs={'type':'date','class':'custom-select'}),            
            "description" : forms.Textarea(attrs={'class':'contact-input'}),            
        }
        
class AssignWorkForm(forms.ModelForm):
    staffid = forms.ModelChoiceField(queryset=Register.objects.filter(usertype="2"))
    class Meta:
        model = add_work
        fields = ['message'] 
        widgets = {
            'staffid' : forms.TextInput(attrs={'class':'contact-input'}),
            'message' : forms.TextInput(attrs={'class':'contact-input'}),
        }        

STATUS_CHOICES = [
    ('' , 'Select'),
    ('Completed' , 'Completed'),
    ('On Progress' , 'On Progress'),
    ('On Hold' , 'On Hold'),
    ('Not Started' , 'Not Started'),
    ('In Review' , 'In Review'),
]      
class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = StatusClass
        fields = ['update_status','message']
        widgets = {
            'update_status' : forms.Select(choices=STATUS_CHOICES,attrs={'class':'custom-select'}),
            'message' : forms.Textarea(attrs={'class':'contact-input'}),
        } 
        