from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import FormView,CreateView,TemplateView
from .forms import Mysignup,File,Name
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth import authenticate
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Check, Csvfile
import csv
from random import randint

class Home(SuccessMessageMixin ,CreateView):
    template_name='home.html'
    model=Csvfile
    fields=['file']
    success_url = reverse_lazy('chart')
    success_message = "Your file has been uploaded successfully!"    


class Chart(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        dt=Csvfile.objects.all().order_by('-pk')[0]
        print(dt.file)
        if str(dt.file).endswith(".csv"):      
            ff=dt
            title=[]
            c=0
            raw=[]
            lst=[]
            color=[]
            with open(ff.file.path,'r') as f:
                reader=csv.reader(f)
                for row in reader:
                    if c==0:
                        title.append(row)
                        c+=1
                    else:
                        raw.append(row)
            length=len(title[0])
            
            for i in range(length):
                temp=[]
                for j in raw:
                    try:
                        cnv=int(j[i])
                        temp.append(cnv)
                    except:
                        temp.append(j[i])
                lst.append(temp)
            context['label']=''
            context['data']=''
            for i in range(length):
                if (context['data']!='' and context['label']!=''):
                    break
                if type(lst[i][0])==int:
                    if context['data']=='':
                        context['data']=lst[i]
                    continue
                else:
                    if context['label']=='':
                        context['label']=lst[i]
                    continue
            for v in range(len(lst[0])):
                q=f"rgb({str(randint(1,255))},{str(randint(1,255))},{str(randint(1,255))})"
                color.append(q)
            context['color']=color
            return context
        else:
            messages.warning(self.request,'file should be .csv only' )
            return context
        
        
class Signup(SuccessMessageMixin,CreateView):
    template_name='signup.html'
    success_url = reverse_lazy('home')
    form_class = Mysignup
    success_message = "Your profile was created successfully"

class Logout(SuccessMessageMixin,LogoutView):
    template_name='home.html'
    success_message="You have Logout from your account!"
    next_page =  reverse_lazy('home')

class Login(SuccessMessageMixin, LoginView):
    template_name='login.html'
    success_message='successfully login!'

class Newpass(PasswordChangeView):
    template_name='newpass.html'
    success_url='/newpassdone'

class Newpassdone(SuccessMessageMixin, PasswordChangeDoneView):
    template_name='newpassdone.html'
    success_message='Your password has been change !'

class Circle(TemplateView):
    template_name='anim.html'