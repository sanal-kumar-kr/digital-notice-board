from django import forms
from complaint.models import Complaints

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ['subject','message']
        widgets = {
            'subject' : forms.TextInput(attrs={'class':'contact-input'}),
            'message' : forms.Textarea(attrs={'class':'contact-input'})
        }
        labels = {
            'subject' : 'Complaint subject'
        }
        
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ['response']
        widgets = {
            "response" : forms.Textarea(attrs={'class':'contact-input'})
        }