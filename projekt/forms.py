#Formularze dla aplikacji portal.

from django import forms
from django.contrib.auth.models import User
from portal.models import Student

#Klasa reprezentująca formularz rejesstracji użytkownika.
class UserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {'username': 'Nazwa użytkownika', 'password': 'Hasło użytkownika'}


#Klasa reprezentująca formularz rejestracji studenta.
class StudentRegistration(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'portal_list']
        labels = {'portal_list': 'Grupy zajęciowe', 'roll_no': 'Numer albumu', 'name': 'Imię i nazwisko'}
