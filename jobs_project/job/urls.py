from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from job.views import jobs_all, jobs_contact, jobs_details, signin_user, signup_user,mylogout,add_job
app_name='job'
urlpatterns = [
    path('',jobs_all,name='jobs_all'),
    path('<int:id>',jobs_details,name='jobs_details'),
    path('contact',jobs_contact,name='jobs_contact'),
    path('signup',signup_user,name='signup'),
    path('signin',signin_user,name='signin'),
    path('mylogout',mylogout,name='mylogout'),
    path('addjob',add_job,name='addjob'),
]