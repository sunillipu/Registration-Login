from multiselectfield import MultiSelectFormField
from django import forms
from django.forms import extras

class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label='Enter Your First Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'First Name',
                'class':'form-control'
            }
        )
    )
    last_name=forms.CharField(
        label='Enter Your Last Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Last Name',
                'class':'form-control'
            }
        )
    )
    username=forms.CharField(
        label='Enter User Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'User Name',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )
    email=forms.CharField(
        label='Enter Your Email Id',
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Your Email',
                'class':'form-control'
            }
        )
    )
    mobile=forms.CharField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Mobule Number',
                'class':'form-control'
            }
        )
    )
    LOCATION_CHOICE = (
        ('hyd', 'HYDERABAD'),
        ('bang', 'BANGALORE'),
        ('che', 'CHENNAI'),
        ('mum', 'MUMBAI'),
    )
    location=MultiSelectFormField(max_length=200,choices=LOCATION_CHOICE)
    JOB_CHOICE = (
        ('HR', 'HR'),
        ('SOFTWARE', 'SOFTWARE'),
        ('MANAGER', 'MANAGER'),
        ('ADMIN', 'ADMIN'),
    )
    job=MultiSelectFormField(max_length=200,choices=JOB_CHOICE)
    GENDER_CHOICE=(
        ('male','MALE'),
        ('female','FEMALE')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(),choices=GENDER_CHOICE
    )
    y=range(1970,2011)

    dob=forms.DateField(
        widget=forms.extras.SelectDateWidget(years=y)
    )
class LoginForm(forms.Form):
    username=forms.CharField(
        label='Enter Your User Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your Username',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':' Your Password',
                'class':'form-control'
            }
        )
    )
