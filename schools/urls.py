from django.urls import path
from . import views
from django.views.generic import TemplateView
from . forms import profileForm, SchoolsForm, school_dataForm
from . views import profile, Schools, add_School
urlpatterns = [
	#path('signup', views.signUp, name = 'signup'),
	path('', views.index, name = 'index' ),
	#path('', views.TemplateView, (template_name = 'index')),
	path('schools/', views.SchoolDetailView.as_view(), name ='schools'),
	path(r'addschools/', views.add_School.as_view([profileForm, SchoolsForm, school_dataForm]), name = 'addSchools')
	
	]