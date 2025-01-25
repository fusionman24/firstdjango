"""
URL configuration for firstdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from home.views import *
from home import views

urlpatterns = [
    # path('',home, name='home'),
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(template_name='logginn.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('', login_page, name='login_page'),
    path('', LoginView.as_view(template_name='logginn.html'), name='login'),

    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/approve/<int:pk>/', views.admin_approve_request, name='admin_approve_request'),
    path('coordinator/dashboard/', views.coordinator_dashboard, name='coordinator_dashboard'),
    path('coordinator/add-startup/', views.add_startup, name='add_startup'),
    path('jury/dashboard/', views.jury_dashboard, name='jury_dashboard'),]