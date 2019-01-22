#Formularze dla aplikacji portal.
from django import forms
from django.contrib.auth.models import User

from .models import Message, Topic, Entry
from nauczyciel.models import Submission
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

#Klasa reprezntująca formularz wysyłanie wiadomości na forum.
class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['content']


#Klasa reprezntująca formularz dodawania rozwiązania do zadania.
class SubmissionForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ['file_submitted']
        labels = {'file_submitted': 'Pliki'}

#Klasa reprezntująca formularz dodawania tematu.
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

#Klasa reprezntująca formularz dodawania notatki do tematu.
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': SummernoteWidget(),
        }
