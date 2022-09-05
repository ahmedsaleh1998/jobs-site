from email.mime import image
from pyexpat import model
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

from catigory.models import Catigory
# Create your models here.
all_job_type=(
    ('full time','full time'),
    ('part time','part time'),
)

class Job(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    category =models.ForeignKey(Catigory,on_delete=models.CASCADE)
    title =models.CharField(max_length=30,default='')
    location =models.CharField(max_length=30,default='')
    job_type =models.CharField(choices=all_job_type,max_length=20)
    description =models.TextField(max_length=1000,default='')
    published_at =models.DateField(auto_now=True)
    vacancy= models.IntegerField()
    salary= models.IntegerField()
    experience= models.IntegerField()
    image= models.ImageField(upload_to='jobs/')



class Apply(models.Model):
   
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=60)
    linkedin=models.URLField(max_length=100)
    cv=models.FileField(upload_to='apply/')
    cover_letter=models.TextField(max_length=1000)


class Contactus(models.Model):
    message=models.TextField(max_length=1000)
    name=models.CharField(max_length=30)
    email=email=models.EmailField(max_length=60)
    subject=models.CharField(max_length=60)
    