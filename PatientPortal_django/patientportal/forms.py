from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('firstName', 'lastName', 'DOB', 'phone', 'medication', 'diagnosis')


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
