
from django.urls import path
from  . import views
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . forms import profileForm, SchoolsForm, school_dataForm
from . views import profile, Schools, add_School, Contact, Login
urlpatterns = [
	#path('signup', views.signUp, name = 'signup'),
	path('', views.index, name = 'index' ),
	#path('', views.TemplateView, (template_name = 'index')),
	#path('schools/', views.SchoolDetailView.as_view(), name ='schools'),

	path(r'add_schools', add_School.as_view([profileForm, SchoolsForm, school_dataForm]), name = 'add_Schools'),
	path('contact/', views.Contact, name = 'Contact'),
	path('login/', views.Login, name = 'Login'),
	path('logout/', views.Logout, name = 'Logout' ),
	
	]
