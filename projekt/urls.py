"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login_user, name='login_user'),
    url(r'^register_user/$', views.register_user, name='register_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^portal/', include('portal.urls', namespace='portal')),
    url(r'^nauczyciel/', include('nauczyciel.urls', namespace='nauczyciel')),
    url(r'^summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
