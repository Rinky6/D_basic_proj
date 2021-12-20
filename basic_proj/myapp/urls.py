from django.urls import path
"""basic_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import *
from . import views

urlpatterns = [
    path('name/', views.index),
    path('index/', views.index1),
    path('ftch/<str:p_no>', views.index2),
    path('hpage/',views.index3),
    path('hpage1/<int:number>' ,views.index4),
    path('hpage2/loops' ,views.index5),
    path('cls',views.Fst_Cls.as_view(),name = 'Fst_Cls'),
    path('clss/<int:p_no>',views.Scd_Cls.as_view(),name = 'Scd_Cls'),


]
