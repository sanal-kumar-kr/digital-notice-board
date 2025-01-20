# forms.py
from django import forms
from .models import Notes
from department.models import Semesters

class NotesAddForm(forms.ModelForm):
   

    class Meta:
        model = Notes
        fields = ['title', 'description', 'notes']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'title-input'}),
            'description': forms.Textarea(attrs={'class': 'title-input'}),
            'notes': forms.FileInput(attrs={'accept': 'application/pdf'}),
        }
