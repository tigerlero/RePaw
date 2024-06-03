from django import forms
from .models import Dog


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'
