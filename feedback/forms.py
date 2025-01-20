from feedback.models import Feedbacks
from django import forms

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ['subject','message']
        widgets = {
            'subject' : forms.TextInput(attrs={'class':'contact-input'}),
            'message' : forms.TextInput(attrs={'class':'contact-input'})
        }
        
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ['response']
        widgets = {
            "response" : forms.Textarea(attrs={'class':'contact-input'})
        }