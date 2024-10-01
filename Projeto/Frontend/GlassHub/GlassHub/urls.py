"""
URL configuration for GlassHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from GlassHubApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.monitoramento, name='monitoramento'), 
    path('alarmes/', views.alarmes, name='alarmes'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('monitoramento/', views.monitoramento, name='monitoramento'), 
    path('dashbord/', views.dashbord, name='dashbord'),  
    path('login/', views.login, name='login'),
    path('faturamento/', views.faturamento, name='faturamento'),
    path('parametrizacao/', views.parametrizacao, name='parametrizacao'),
]