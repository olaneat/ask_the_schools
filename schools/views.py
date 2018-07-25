from django.shortcuts import render
from django.urls import reverse_lazy
from .models import parent_signup, Reg_Schools
from django.contrib.auth.forms import UserCreationForm

from django.views import generic

# Create your views here.



class signUp(generic.CreateView):
	form_class = UserCreationForm
	successfull_url = reverse_lazy('login')
	template_name = 'signup.html'