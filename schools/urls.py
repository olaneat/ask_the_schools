from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
	path('signup', views.signUp, name = 'signup'),
	path('', views.index, name = 'index' ),
	#path('', views.TemplateView, (template_name = 'index')),
	path('schools/', views.SchoolDetailView.as_view(), name ='schools'),
	]