"""
Definition of urls for DjangoProject.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('profile/', views.profile, name='profile'),
    path('Forum/', views.Forum, name='Forum'),
    path('ForumA/', views.ForumA, name='ForumA'),
    path('Administration/Ban', views.Ban, name='Ban'),
    path('Administration/Moderation', views.Moderation, name='Moderation'),
    path('Administration/Servers', views.Servers, name='Servers'),
    path('Administration/Players', views.Players, name='Players'),
    path('Administration/ForumAdministration', views.ForumAdministration, name='ForumAdministration'),
    path('Administration/Bug', views.Bug, name='Bugy'),

]
