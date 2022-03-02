"""TClearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from gestion.views import indexL



urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', indexL, name="land"),
    path('', include('gestion.urls')),
    path('teoria/', include('teoria.urls')),
    path('ejemplo/', include('ejemplo.urls')),
    path('calculadora/', include('calculadora.urls')),
    path('video/', include('video.urls')),
    path('examen/', include('examen.urls')),
    path('sesion/', include('loginout.urls')),
    path('account/', include('django.contrib.auth.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
