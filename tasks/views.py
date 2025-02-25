from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    ontasks = pending_tasks.objects.all()
    context = {'tasks': ontasks}
    return render (request, "tasks/index.html", context)