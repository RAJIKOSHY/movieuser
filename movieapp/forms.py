
from django import forms
from .models import movie



class movieform(forms.ModelForm):
    class Meta:
        model=movie
        fields=['name','details','link','pic','creator']
