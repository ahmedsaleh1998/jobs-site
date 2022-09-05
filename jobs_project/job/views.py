from multiprocessing import context
from django.shortcuts import render,redirect
from job.filters import JobFilter
from job.forms import Add_job, Apply_job_form, Contact_form, Myuser_form_Signin, Myuser_form_Signup
from django.contrib.auth import authenticate,login,logout
from job.models import Job
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def jobs_all(request):
  if (request.user.is_authenticated):
    context={}
    all_jobs=Job.objects.all()
    
    myfilter=JobFilter(request.GET,queryset=all_jobs)
    job_list=myfilter.qs
    paginator = Paginator(job_list, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj']=page_obj
    context['jobs']=all_jobs
    context['myfilter']=myfilter
    return render (request,'jobs.html',context)
  else:
      return redirect('jobs:signin')

#//////////////////////////
def jobs_details(request , id):
  if (request.user.is_authenticated):
    context={}
    myjob=Job.objects.get(id=id)
    context['job']=myjob
    print(myjob.id)
    if request.method=="POST":
        myform=Apply_job_form(request.POST , request.FILES)
        myform.save()
        context['flag']=1
        context['form']=myform
        return render (request,'job_details.html',context)
    else:
          context['flag']=0
          myform= Apply_job_form()
          context['form']=myform
          return render (request,'job_details.html',context)
          
  else:
      return redirect('jobs:signin')
    
#///////////////////
# def jobs_contact(request):
#      if (request.user.is_authenticated):
#        return render (request,'contact.html')
#      else:
#         return redirect('jobs:signin')

def signup_user(request):
    context={}
    if request.method=="POST":
       myform=Myuser_form_Signup(request.POST)
       if myform.is_valid():
            user1=User.objects.create_user(username=request.POST['username'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'])
            user = authenticate(username=request.POST['username'],password=request.POST['password'])
            login(request,user)
            return redirect('jobs:jobs_all')
    else:
        myform = Myuser_form_Signup()
        context['form']=myform
    return render(request,'signup.html',context)

def signin_user(request):
    context={}
    if request.method=="POST":
     try:
        myform=Myuser_form_Signin(request.POST)
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        login(request,user)
        return redirect('jobs:jobs_all')      
     except:
         myform = Myuser_form_Signin()
         context['form']=myform
         context['msg']='Wrong password or username ... '
         
         return render(request,'signin.html',context)
    else:
        myform = Myuser_form_Signin()
        context['form']=myform
    return render(request,'signin.html',context)

def mylogout(request):
    request.session.clear()
    logout(request)
    return redirect('jobs:signin')

def apply_job(request):
    pass

def jobs_contact(request):
  if (request.user.is_authenticated):
    context={}
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
        return redirect('jobs:jobs_all')  
        
    else:
          myfrom=Contact_form()
          context['form']=myfrom
          return render(request,'contact.html',context)
  else:
          return redirect('jobs:signin')
    
    
    
    
    

def add_job(request):
  context={}
  if request.method=="POST":
        form = Add_job(request.POST , request.FILES)
    # if form.is_valid():
        myform = form.save(commit=False)
        myform.owner = request.user
        myform.save()
        return redirect(reverse('jobs:jobs_all'))    

  else:
        myform=Add_job()
        context['form']=myform
        return render(request,'addjob.html',context)
      
      
# def Apply_job(request):
#   form=Apply_job_form()
#   context['form']=form
#   return render(request,'addjob.html',context)
  