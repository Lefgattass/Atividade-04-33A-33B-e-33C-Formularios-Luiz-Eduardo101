"""django_project URL Configuration

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
from django.urls import path

from AppLuizEduardoFagundesGattass import views
urlpatterns = [
    path('',views.home, name="home"),
    path('mcf',views.create_mcf),
    path('mcf/update/<id>',views.update_mcf),
    path('mcf/delete/<id>',views.delete_mcf),
    path('rcv',views.create_rcv),
    path('rcv/update/<id>',views.update_rcv),
    path('rcv/delete/<id>',views.delete_rcv),

