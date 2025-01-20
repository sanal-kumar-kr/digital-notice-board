from django import forms
from department.models import *

SEMESTER_CHOICE=[
    ('',' select'),
    ('Sem-I','Semester I'),
    ('Sem-II','Semester II'),
    ('Sem-III','Semester III'),
    ('Sem-IV','Semester IV'),
    ('Sem-V','Semester V'),
    ('Sem-VI','Semester VI'),
    ('Sem-VII','Semester VII'),
    ('Sem-VIII','Semester VIII'),
]

class departmentaddform(forms.ModelForm):
    class Meta:
        model = Departments
        fields = "__all__"
        widgets = {
            'description' : forms.Textarea(attrs={'class':'contact-input'}),
            'departmentname' : forms.TextInput(attrs={'class':'contact-input'}),
            'departmentimage': forms.FileInput(attrs={'class': 'contact-input'})
        
        }
        
class SemesterAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].widget.attrs['class'] = 'custom-select'
    class Meta:
        model = Semesters
        fields = ['department','semestername']
        widgets = {
            'semestername' : forms.TextInput(attrs={'class':'contact-input'})
        }