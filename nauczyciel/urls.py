#Adresy URL dla aplikacji nauczyciel.

from django.conf.urls import url, include
from django.contrib import admin
from . import views

#Wzorce adresów URL dla aplikacji:
urlpatterns = [
    #Strona główna nauczyciela
    url(r'^nauczyciel_index/$', views.nauczyciel_index, name='nauczyciel_index'),
    #Strona główna zajęć prowadzonych przez nauczyciela.
    url(r'^(?P<portal_id>[0-9]+)/nauczyciel_detail/$', views.nauczyciel_detail, name='nauczyciel_detail'),
    #Strona przeznaczona do dodawania zadań.
    url(r'^(?P<portal_id>[0-9]+)/add_assignment/$', views.add_assignment, name='add_assignment'),
    #Strona przeznaczona do dodawnia dodatkowych materiałów.
    url(r'^(?P<portal_id>[0-9]+)/add_resource/$', views.add_resource, name='add_resource'),
    #Strona przeznaczoma do dodawania ogłoszeń.
    url(r'^(?P<portal_id>[0-9]+)/add_notification/$', views.add_notification, name='add_notification'),
    #Strona przeznaczona do wyświetlania strony z listą zadań.
    url(r'^(?P<portal_id>[0-9]+)/view_all_assignments/$', views.view_all_assignments, name='view_all_assignments'),
    #Strona przeznaczona do wyświetlania listy przesłanych rozwiązań.
    url(r'^(?P<assignment_id>[0-9]+)/view_all_submissions/$', views.view_all_submissions, name='view_all_submissions'),
]
