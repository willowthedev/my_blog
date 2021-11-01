from django import forms
from django.forms import widgets

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Subject', max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control'}))