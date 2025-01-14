from django import forms
from authentification.models import User
from patient.models import Patient
from .models import RendezVous


class RendezVousForm(forms.Form):
    medecin = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-cyan-500 dark:focus:border-cyan-500"
        }
        ))
    titre = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-cyan-500 dark:focus:border-cyan-500"
        }
        ))
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), widget=forms.Select(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-cyan-500 dark:focus:border-cyan-500"
        }
        ))
    date = forms.DateField(widget=forms.DateInput(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-cyan-500 dark:focus:border-cyan-500",
             'type':'date'
        }
        ))
    heure = forms.TimeField(widget=forms.TimeInput(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-cyan-500 dark:focus:border-cyan-500",
             'type':'time'
        }
        ))
    lieu = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-cyan-500 dark:focus:border-cyan-500"
        }
        ))
   
    class Meta:
        model = RendezVous
       