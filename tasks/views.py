from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

class UserLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index')
        
class RegisterPage(FormView):
    template_name = 'tasks/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)

#LoginRequiredMixin para restringir paginas/tareas por usuario
class TaskList(LoginRequiredMixin, ListView):
    model = pending_tasks #En Admin tiene se llama pending_taskss 
    context_object_name = 'pending_tasks'
    
    #Conecta las tareas según el usurio que las creo, es decir, solo las deja visibles a cierto usurio dueño de la tarea
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending_tasks'] = context['pending_tasks'].filter(user=self.request.user)
        context['count'] = context['pending_tasks'].filter(complete=False).count()
        return context
  
  
    
def index(request):
    tasks = pending_tasks.objects.all()
    context = {'tasks': tasks}
    return render (request, "tasks/index.html", context)