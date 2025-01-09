from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=63, label='Email', widget=forms.EmailInput(
        attrs={
             "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-emerald-900 dark:focus:border-cyan-500"
        }
        ))
    password = forms.CharField(max_length=63,  label='Mot de passe', widget=forms.PasswordInput(
        attrs={
             "class":"mb-3 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-500 focus:border-cyan-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-emerald-900 dark:focus:border-cyan-500"
        }
        ))