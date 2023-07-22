from django import forms
from .models import *


class empform(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'

