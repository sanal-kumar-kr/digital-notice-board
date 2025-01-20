from django import forms
from classroom.models import Classes

class Classroomaddform(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ['classname','seatrows','seatcolumns']
        widgets = {
            'classname' : forms.TextInput(attrs={'class':'contact-input'}),
            'seatrows' : forms.TextInput(attrs={'class':'contact-input'}),
            'seatcolumns' : forms.TextInput(attrs={'class':'contact-input'})
        }
        labels = {
            'classname' : 'Class Name',
            'seatrows' : 'No of Rows',
            'seatcolumns' : 'No of Columns'
        }