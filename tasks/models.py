from django.db import models

# Create your models here.

class pending_tasks(models.Model):
    tittle = models.CharField(max_length=200)
    done_task = models.BooleanField(default=False)

    def  __str__(self):
        return self.tittle
    