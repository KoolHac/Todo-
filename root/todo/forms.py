from .models import *
from django import forms

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder':'Add Task', 'class': 'form-control'}))
    class Meta:
        model = Task
        fields = ['title']

class UpdateForm(TaskForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Update an existing task'}))
    class Meta:
        model = Task
        fields = ['title', 'complete']