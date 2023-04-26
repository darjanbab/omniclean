from django.db import models
from django import forms

class NewNutzer(models.Model):
    vorname = models.CharField(max_length=50)
    nachname = models.CharField(max_length=50)
    email = models.EmailField(default='')
    tel = models.CharField(max_length=20, default='')
    firma = models.CharField(max_length=50, default='')
    message = models.TextField(max_length=300, default='')
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if email and '@' not in email:
            raise forms.ValidationError('Invalid email address')
        return cleaned_data