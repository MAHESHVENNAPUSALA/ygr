from .models import *
from django import forms
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'time_taken', 'link', 'image1', 'image2', 'image3', 'image4']
 

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'description']

from django import forms
from .models import InternshipRegistration

class InternshipForm(forms.ModelForm):
    class Meta:
        model = InternshipRegistration
        fields = '__all__'