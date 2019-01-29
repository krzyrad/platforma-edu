#Modele aplikacji portal.

from django.db import models
from django.contrib.auth.models import User
from nauczyciel.models import Course
from django.core.urlresolvers import reverse

#Miejsce na modele;

#Klasa reprezentująca studentów zarejestrowanych w aplikacji.
class Student(models.Model):
    #Użytkownik powiązany ze studentem.
    user = models.ForeignKey(User, default=1)

    #Imię i nazwisko studenta.
    name = models.CharField(max_length=100)

    #Numer albumu studenta.
    roll_no = models.CharField(max_length=100)

    #Zajęcia, do których student jest zapisany.
    portal_list = models.ManyToManyField(Course)

    class Meta:
        verbose_name_plural = 'studenci'

    #Funkcja zwracająca reprezentację modelu w postaci ciągu znaków.
    #self jest wskaźnikiem do obiektu;
    def __str__(self):
        return self.name

#Klasa reprezentująca wiadomośći wyświetlane na forum.
class Message(models.Model):
    #Treść wiadomości.
    content = models.CharField(max_length=500)

    #Zajęcia związane z wiadomośćią.
    portal = models.ForeignKey(Course,default=1,on_delete=None)

    #Nadawca wiadomości.
    sender = models.ForeignKey(User,default=1, on_delete=None)

    #Data i godzina zamieszczenia wiadomości na forum.
    time = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'wiadomosci'

#Klasa reprezentująca powiadomienia otrzymywane przez studentów.
class Notification(models.Model):
    #Treść powiadomienia.
    content = models.TextField()

    #Zajęcia związane z powiadomieniem.
    portal = models.ForeignKey(Course, default=1, on_delete=None)

    #Data i godzina otrzymania powiadomienia.
    time = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'aktualnosci'

#Klasa reprezentująca dodatkowe materiały edukacyjne dla określonych zajęć.
class Resources(models.Model):
    #Plik dodatkowych materiałów.
    file_resource = models.FileField(default='')

    #Nazwa dodatkowych zasobów.
    title = models.CharField(max_length=100)

    #Powiązanie zajęć z dodatkowymi plikami.
    portal = models.ForeignKey(Course, default=1, on_delete=None)

    class Meta:
        verbose_name_plural = 'pliki'

#Klasa reprezentująca tematy notatek studenta.
class Topic(models.Model):
    #Nazwa tematu notatki.
    text = models.CharField(max_length=200)
    #Data i godzina utworzenia tematu.
    date_added = models.DateTimeField(auto_now_add=True)
    #Określenie właściciela tematu.
    owner = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'tematy'

    #Funkcja zwracająca reprezentację modelu w postaci ciągu tekstowego.
    #self jest wskaźnikiem do obiektu;
    def __str__(self):
        return self.text

#Klasa reprezentująca notatki przechowywane przez studenta.
class Entry(models.Model):
    #Powiązanie notatki z tematem.
    topic = models.ForeignKey(Topic)
    #Zawartość notatki.
    text = models.TextField()
    #Data i godzina utworzenia notatki.
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'notatki'

    #Funkcja zwracająca reprezentację modelu, w postaci ograniczonego do 50 znaków ciągu tekstowego.
    #self jest wskaźnikiem do obiektu;
    def __str__(self):
        """Zwraca reprezentację modelu w postaci ciągu tekstowego."""
        return self.text[:50] + "..."
