from notification.models import *
from django import forms

USERTYPE_CHOICES=[
    ('',' Select'),
    ('None',' Public'),
    ('2',' Staff'),
    ('3',' Student')
]
        
class NotificationAddForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = ['title','description','start_date','end_date','usertype']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'contact-input'}),
            'description' : forms.Textarea(attrs={'class':'contact-input'}),
            'start_date' : forms.DateInput(attrs={'type':'date','class':'custom-select'}),
            'end_date' : forms.DateInput(attrs={'type':'date','class':'custom-select'}),
            'usertype' : forms.Select(attrs={'class':'custom-select '},choices=USERTYPE_CHOICES)
        }
        label = {
            'start_date' : 'Start Date',
            'end_date' : 'End Date'
        }
        
class StaffNotificationAddForm(forms.ModelForm):
    
    class Meta:
        model = StaffNotifications
        fields = ['title','description','start_date','end_date']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'contact-input'}),
            'description' : forms.Textarea(attrs={'class':'contact-input'}),
            'start_date' : forms.DateInput(attrs={'type':'date','class':'custom-select'}),
            'end_date' : forms.DateInput(attrs={'type':'date','class':'custom-select'}),
        }
        

        