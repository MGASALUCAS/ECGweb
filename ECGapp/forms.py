from django import forms
from . import models
from .models import Post


class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patients
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'form-control',
        'placeholder': 'Write a post....'
    }))

    class Meta:
        model = Post
        fields = ('post',)
