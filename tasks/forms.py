from django import forms 
from django import ModelForm
from .models import *

class FormTask(form.ModelForm)
    class Meta:
        model = pending_tasks
        