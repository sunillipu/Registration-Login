from django.db import models
from multiselectfield import MultiSelectField

class RegistrationData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.BigIntegerField()
    LOCATION_CHOICE=(
        ('hyd','HYDERABAD'),
        ('bang','BANGALORE'),
        ('che','CHENNAI'),
        ('mum','MUMBAI'),
    )
    location=MultiSelectField(max_length=200,choices=LOCATION_CHOICE)
    JOB_CHOICE = (
        ('HR', 'HR'),
        ('SOFTWARE', 'SOFTWARE'),
        ('MANAGER', 'MANAGER'),
        ('ADMIN', 'ADMIN'),
    )
    job=MultiSelectField(max_length=200,choices=JOB_CHOICE)
    gender=models.CharField(max_length=50)
    dob=models.DateField(max_length=80)



# Create your models here.
