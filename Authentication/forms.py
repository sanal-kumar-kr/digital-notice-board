from django import forms
from .models import *
from department.models import *


        
class LoginForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ['username','password']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "password" : forms.PasswordInput(attrs={'class':'form-input','style':'width : 90%;'})
        }
        help_texts = {
            'username' : None
        }
        
    
        
GENDER_CHOICES=[
    ('',' Select'),
    ('male',' male'),
    ('female',' female'),
    ('other',' other')
]


class StaffRegisterForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Departments.objects.all())
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['department'].widget.attrs['class'] = 'custom-select'
            # for visible in self.visible_fields():
            #     visible.field.widget.attrs['class'] = 'custom-select'
            #     visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta:
        model = Register
        fields = ['name','email','password','contact','address','gender','experience','qualification','department']
        widgets = {
            "name" : forms.TextInput(attrs={'class':'contact-input'}),
            "email" : forms.EmailInput(attrs={'class':'contact-input'}),
            "password" : forms.PasswordInput(attrs={'class':'contact-input'}),
            "contact" : forms.TextInput(attrs={'class':'contact-input','maxlength':'10'}),
            "address" : forms.TextInput(attrs={'class':'contact-input'}),
            "gender" : forms.Select(attrs={'class':'custom-select '},choices=GENDER_CHOICES),
            "experience" : forms.TextInput(attrs={'class':'contact-input'}),
            "qualification" : forms.TextInput(attrs={'class':'contact-input'}),
            "department" : forms.TextInput(),

        }
        
        
class StaffRegisterEditForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Departments.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].widget.attrs['class'] = 'custom-select'
        
    class Meta:
        model = Register
        fields = ['name','email','contact','address','gender','experience','qualification','department']
        
        widgets = {
            "name" : forms.TextInput(attrs={'class':'contact-input'}),
            "email" : forms.EmailInput(attrs={'class':'contact-input'}),
            "contact" : forms.TextInput(attrs={'class':'contact-input','maxlength':'10'}),
            "address" : forms.TextInput(attrs={'class':'contact-input'}),
            "gender" : forms.Select(attrs={'class':'custom-select'},choices=GENDER_CHOICES),
            "experience" : forms.TextInput(attrs={'class':'contact-input'}),
            "qualification" : forms.TextInput(attrs={'class':'contact-input'}),
            "department" : forms.TextInput(attrs={'style':'width : 50%;'}),
        }
        
        
        
class StudentRegisterForm(forms.ModelForm):
    # department = forms.ModelChoiceField(queryset=Departments.objects.all())
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['department'].widget.attrs['class'] = 'custom-select'

    class Meta:
        model = Register
        fields = ['name','regno','email','password','gender','dob','address','contact']
        widgets = {
            "dob" : forms.DateInput(attrs={'type':'date','style':'width:100%'}),
            "regno" : forms.TextInput(attrs={'class':'contact-input'}),
            "name" : forms.TextInput(attrs={'class':'contact-input'}),
            "email" : forms.EmailInput(attrs={'class':'contact-input'}),
            "password" : forms.PasswordInput(attrs={'class':'contact-input'}),
            "contact" : forms.TextInput(attrs={'class':'contact-input','maxlength':'10'}),
            "address" : forms.TextInput(attrs={'class':'contact-input'}),
            "gender" : forms.Select(attrs={'class':'custom-select'},choices=GENDER_CHOICES),
            # "department" : forms.TextInput(attrs={'style':'width : 50%;'}),
            # "semester" : forms.Select(attrs={'class':'custom-select'}),
            "batch" : forms.TextInput(attrs={'class':'contact-input'}),
        }
        
        
class StudentRegisterEditForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Departments.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].widget.attrs['class'] = 'custom-select'
     

    class Meta:
        model = Register
        fields = ['name','regno','email','gender','department','semester','dob','address','contact']
        widgets = {
            "dob" : forms.DateInput(attrs={'type':'date','class':'contact-input'}),
            "name" : forms.TextInput(attrs={'class':'contact-input'}),
            "regno" : forms.TextInput(attrs={'class':'contact-input'}),
            "email" : forms.EmailInput(attrs={'class':'contact-input'}),
            "contact" : forms.TextInput(attrs={'class':'contact-input','maxlength':'10'}),
            "address" : forms.TextInput(attrs={'class':'contact-input'}),
            "gender" : forms.Select(attrs={'class':'custom-select'},choices=GENDER_CHOICES),
            "semester" : forms.Select(attrs={'class':'custom-select'}),
            "department" : forms.TextInput(attrs={'style':'width : 50%;'}),
            "batch" : forms.TextInput(attrs={'class':'contact-input'}),
        }

class Studentprofileedit(forms.ModelForm):
    # department = forms.ModelChoiceField(queryset=Departments.objects.all())
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['department'].widget.attrs['class'] = 'custom-select'
     

    class Meta:
        model = Register
        fields = ['name','email','gender','address','contact']
        widgets = {
            "name" : forms.TextInput(attrs={'class':'contact-input'}),
            "email" : forms.EmailInput(attrs={'class':'contact-input'}),
            "contact" : forms.TextInput(attrs={'class':'contact-input','maxlength':'10'}),
            "address" : forms.TextInput(attrs={'class':'contact-input'}),
            "gender" : forms.Select(attrs={'class':'custom-select'},choices=GENDER_CHOICES),
           
        }
        








class ForgotForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['email']
        widgets = {
            "email" : forms.EmailInput(attrs={'class':'contact-input'}),
        }
            
class UpdatePasswordForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['password']
        widgets = {
            "password" : forms.TextInput(attrs={'class':'contact-input','style':'width:70%'})
        }