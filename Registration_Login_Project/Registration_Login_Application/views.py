from django.shortcuts import render,redirect
from .models import RegistrationData
from .forms import RegistrationForm,LoginForm
from django.http.response import HttpResponse

def Registration_View(request):
    if request.method == 'POST':
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            first_name=rform.cleaned_data.get('first_name','')
            last_name = rform.cleaned_data.get('last_name','')
            username = rform.cleaned_data.get('username','')
            password = rform.cleaned_data.get('password','')
            email = rform.cleaned_data.get('email','')
            mobile = rform.cleaned_data.get('mobile','')
            location = rform.cleaned_data.get('location','')
            job= rform.cleaned_data.get('job','')
            gender = rform.cleaned_data.get('gender','')
            dob = rform.cleaned_data.get('dob','')
            data=RegistrationData(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email,
                mobile=mobile,
                location=location,
                job=job,
                gender=gender,
                dob=dob,
            )
            data.save()
            lform=LoginForm()
            return render(request,'login.html',{'lform':lform})
        else:
            return HttpResponse('invalid Data...')
    else:
        rform=RegistrationForm()
        return render(request,'Registration.html',{'rform':rform})

def Login_View(request):
    if request.method=='POST':
        lform=LoginForm(request.POST)
        if lform.is_valid():

            username=request.POST.get('username','')
            password=request.POST.get('password','')
            uname=RegistrationData.objects.filter(username=username)
            pwd=RegistrationData.objects.filter(password=password)

            if uname and pwd :
                return HttpResponse('Login Successfully..........')
            else:
                return HttpResponse('Invalid Data....')
        else:
            return HttpResponse('Invalid Form')
    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})




