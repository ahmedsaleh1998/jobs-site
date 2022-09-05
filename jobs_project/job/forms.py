from pyexpat import model
from django.contrib.auth.models import User
from django import forms

from job.models import Apply, Contactus, Job

class Myuser_form_Signup(forms.ModelForm):
    
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password']

class Myuser_form_Signin(forms.ModelForm):
    
    class Meta:
        model = User
        fields =['username','password']
        
class Add_job(forms.ModelForm):
    
    class Meta:
        model = Job
        fields ='__all__'
        exclude =('owner',)


class Apply_job_form(forms.ModelForm):
    
    class Meta:
        model= Apply
        fields ='__all__'
        exclude =('job',)
        
class Contact_form(forms.ModelForm):
    
    class Meta:
        model= Contactus
        fields ='__all__'