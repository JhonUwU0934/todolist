from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# Create your views here.

class UserLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index')
    
    
def index(request):
    tasks = pending_tasks.objects.all()
    context = {'tasks': tasks}
    return render (request, "tasks/index.html", context)