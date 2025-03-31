from django.db import models
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView


# Create your models here.

class pending_tasks(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    done_task = models.BooleanField(default=False)
    
    def form_invalid(self, form):  #Conecta la información del usuario
        form.instance.user = self.request.user
        return super (pending_tasks, self).form_valid(form)

    def  __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'user'
    