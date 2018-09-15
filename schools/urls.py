from django.urls import path
from . import views
from django.views.generic import TemplateView
from . forms import profileForm, SchoolsForm, school_dataForm
from . views import profile, Schools, addSchool
urlpatterns = [
	#path('signup', views.signUp, name = 'signup'),
	path('', views.index, name = 'index' ),
	#path('', views.TemplateView, (template_name = 'index')),
	path('schools/', views.SchoolDetailView.as_view(), name ='schools'),
	path(r'addschools/', views.addSchool.as_view([profileForm, SchoolsForm, school_dataForm]), name = 'addSchools')
	
	]