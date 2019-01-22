#Adresy URL dla apliakcji portal.

from django.conf.urls import url, include
from django.contrib import admin
from . import views

#Wzorce adresów URL dla aplikacji:
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<portal_id>[0-9]+)/detail/$', views.detail, name='detail'),
    #Strona główna.
    url(r'^index/$', views.index, name='index'),
    #Wyświetlanie wszystkich tematów.
    url(r'^topics/$', views.topics, name='topics'),
    #Strona szczegółowa dotycząca pojedynczego tematu.
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #Strona przeznaczona do dodawania nowego tematu.
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #Strona przeznaczona do dodawania nowego wpisu.
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #Strona przeznaczona do edycji wpisu.
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    #Strona przeznaczona do wysyłania rozwiązania.
    url(r'^(?P<assignment_id>[0-9]+)/upload_submission/$', views.upload_submission, name='upload_submission'),
    #Strona przeznaczona do wyświetlania i pobierania zadań.
    url(r'^(?P<portal_id>[0-9]+)/view_assignments/$', views.view_assignments, name='view_assignments'),
    #Strona przeznaczona do wyświetlania i pobierania dodatkowych materiałów.
    url(r'^(?P<portal_id>[0-9]+)/view_resources/$', views.view_resources, name='view_resources'),
]

