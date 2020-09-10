"""OnlineFoodOrder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from pwn import views

urlpatterns = [
    path("",views.ShowIndex,name='pwn_main'),
    path('pwn_login_check/', views.pwn_login_check, name='pwn_login_check'),
    path('welcome/', views.welcome, name='welcome'),

    path('state/', views.openState, name='state'),
    path('saveState/',views.saveState,name='saveState'),

    path('city/', views.openCity, name='city'),
    path('cuisine/', views.openCusine, name='cuisine'),
    path('vendor/', views.openVendor, name='vendor'),
    path('resports/', views.openReporsts, name='reports'),
    path('logout/', views.pwn_login_check, name='logout'),

]
