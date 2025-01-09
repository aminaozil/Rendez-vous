from django import forms
from .models import Docteur


class DocteurForm(forms.ModelForm):
    class Meta:
        model = Docteur
        