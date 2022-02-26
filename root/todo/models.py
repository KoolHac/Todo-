from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.title
