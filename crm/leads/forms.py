from pyexpat import model
from django import forms
from .models import Lead

#using the ModelForm
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
