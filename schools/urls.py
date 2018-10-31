
from django.urls import path
from  . import views
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls import url
#from django.contrib.auth.views import login
from . forms import profileForm, SchoolsForm, school_dataForm
from . views import  Schools, add_School, Contact, login



urlpatterns = [	
	path(r'login/', views.login_view, name = 'login'),
	path('', views.index, name = 'index' ),
	path(r'add_schools', add_School.as_view([profileForm, SchoolsForm, school_dataForm]), name = 'add_Schools'),
	path('contact/', views.Contact, name = 'Contact'),
	#path('login/', auth_views.login, name = 'login'),
	#path('logout/', views.Logout, name = 'Logout' ),
	
	]

urlpatterns =[
	url(r'^login/$', login, {'template_name': 'schools/login.html'}),

]
