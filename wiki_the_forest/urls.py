"""
URL configuration for wiki_the_forest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views import index, registro, recupero_contra, cuenta, lugares, animales, armas, consumibles, enemigos, construcciones, inicio_sesion,foro, flora, forowiki, historia, logros, iniciosesion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registro/', registro, name="registro"),
    path('recuperar_contra/', recupero_contra, name="recuperar_contra"),
    path('cuenta/', cuenta, name="cuenta"),
    path('lugares/', lugares, name="lugares"),
    path('animales/', animales, name='animales'),
    path('armas/', armas, name='armas'),
    path('construcciones/', construcciones, name='construcciones'),
    path('consumibles/', consumibles, name='consumibles'),
    path('enemigos/', enemigos, name='enemigos'),
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion'),
    path('foro/', foro, name='foro'),
    path('flora/',flora, name='flora'),
    path('forowiki/',forowiki, name='forowiki'),
    path('historia/',historia, name='historia'),
    path('logros/',logros, name='logros'),
    path('iniciosesion/',iniciosesion, name='iniciosesion'),
]
