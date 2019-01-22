#Formularze dla aplikacji portal:

from django import forms
from django.contrib.auth.models import User

from .models import Assignment
from portal.models import Notification, Resources

#Klasa reprezentująca formularz dodawania ogłoszenia.
class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = ['content']
        labels = {'content': 'Treść'}


#Klasa reprezentująca formularz dodawania zadania.
class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['description', 'file', 'deadline']
        labels = {'description': 'Opis', 'file': 'Plik', 'deadline': 'Termin'}


#Klasa reprezentująca formularz dodawania dodatkowych zasobów.
class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resources
        fields = ['title', 'file_resource']
        labels = {'title': 'Tytuł', 'file_resource': 'Pliki'}

