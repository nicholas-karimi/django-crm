from dataclasses import fields
from statistics import mode
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms
from .models import Lead


User = get_user_model()
#using the ModelForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ("first_name", "last_name", "username", "email",)
        field_classes = {"username": UsernameField}
class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead

        fields = (
           'first_name',
           'last_name',
           'age',
           'contacted',
           'source',
           'special_files',
           'agent',            
        )
        widgets = {
            'source': forms.Select()
        }

        


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)
    # contacted = forms.BooleanField(default=False)
