#Modele dla aplikacji nauczyciel.

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


#Klasa reprezentująca zarejestrowanych nauczycieli.
class Instructor(models.Model):
    #Użytkownik powiązany z nauczycielem.
    user = models.ForeignKey(User, default=1)

    #Imię i nazwisko nauczyciela.
    name = models.CharField(max_length=100)

    #informacje na temat nauczyciela.
    information = models.CharField(max_length=1000,default=1)

    class Meta:
        verbose_name_plural = 'nauczyciele'

    #Funkcja zwracająca reprezentację modelu w postaci ciągu znaków.
    #self jest wskaźnikiem do obiektu;
    def __str__(self):
        return self.name


#Klasa reprezentująca zajęcia.
class Course(models.Model):
    #Nazwa zajęć.
    name = models.CharField(max_length=100)

    #Kod zajęć.
    code = models.CharField(max_length=100)

    #Prowadzący zajęcia nauczyciel.
    nauczyciel = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    #Logotyp zajęć.
    portal_logo = models.FileField(default=1)

    class Meta:
        verbose_name_plural = 'zajecia'

    #Funkcja zwracająca reprezentację modelu w postaci ciągu znaków.
    #self jest wskaźnikiem do obiektu;
    def __str__(self):
        return self.name


#Klasa reprezentująca zadania.
class Assignment(models.Model):
    #Opis zadania.
    description = models.TextField(max_length=1000, default='')

    #Materiały pomocnicze do zadania.
    file = models.FileField(default='')

    #Zajęcia powiązane z zadaniem.
    portal = models.ForeignKey(Course)

    #Data i godzina zamieszczenia zadania.
    post_time = models.CharField(max_length=100)

    #Ostateczny termin odesłania rozwiązania do zadania.
    deadline = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'zadania'


#Klasa reprezentująca rozwiązanie zadania.
class Submission(models.Model):
    #Plik przesyłany przez studenta.
    file_submitted = models.FileField(default='')

    #Data i godzina wysłania rozwiązania.
    time_submitted = models.CharField(max_length=100)

    #Powiązanie użytkonika z zadaniem, do którego wysyła rozwiązanie.
    user = models.ForeignKey(User, default=1)

    #Zadanie powiązane z rozwiązaniem.
    assignment = models.ForeignKey(Assignment, default=1)

    class Meta:
        verbose_name_plural = 'rozwiazania'
