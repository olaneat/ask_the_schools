from django.urls import path
from . import views


urlpatterns = [
	path('signup', views.signUp, name = 'signup'),
	path('', views.index, name = 'index' ),
	

	]