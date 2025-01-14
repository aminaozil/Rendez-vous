from django import forms
from authentification.models import User
from .models import Patient


class PatientForm(forms.ModelForm):
    docteur = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-cyan-500 dark:focus:border-cyan-500"
        }
        ))
    nom = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-cyan-500 dark:focus:border-cyan-500"
        }
        ))
    prenom = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-cyan-500 dark:focus:border-cyan-500"
        }
        ))
    age = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-cyan-500 dark:focus:border-cyan-500"
        }
        ))
    adresse = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-cyan-500 dark:focus:border-cyan-500"
        }
        ))
    telephone = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-cyan-500 dark:focus:border-cyan-500"
        }
        ))
    class Meta:
        model = Patient
        fields = '__all__'