from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views import View
from . import forms
from django.http import HttpResponse
from django.utils.decorators import classonlymethod
from django.shortcuts import render
import re
from django.utils import timezone
from . forms import ContactUsForm
from collections import OrderedDict
from django import forms
from django.views.generic import TemplateView
from formtools.wizard.views import SessionWizardView, WizardView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import  Schools, profile, school_data, parents_remark
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.views import generic




#class SchoolDetailView(generic.ListView):
#	models = Schools

# Create your views here.
def index(request):
	return render (request, 'index.html')

#def index(request):
	"view for the home page of the project"
	num_of_schoool = Schools.objects.all().count()
	name_of_school = Schools.objects.list()
	return render(
		request,
		'index.html',
		context = {
		'numbers of registered schools': num_of_schoool, 'name_of_school': name_of_school},

		)

	
class add_School(SessionWizardView):
	template_name =  'schoolprofile.html'
	file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'images', 'videos'))

	def register(request):
		if method.request == "POST" :
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				email = form.cleaned_data.get('email')
				password = form.cleaned_data.get('password1')
				user = authenticate(email=email, password = raw_password)
				login = (request, user )

		else:
			form = UserCreationForm()
			return render(request, 'schoolprofile.html', {'form': form})

	



	def done(self, form_list, **kwargs):
		form_data = process_data(form_list)
		return render('index.html', { 'form_data': form_data})
			

def process_data(form_list):
	form_data = [form.cleaned_data for form in form_list]
	
	send_mail(form_data[0]['Schools'],
		form_data[1]['school_data'],
		['tosinayoola0@gmail.com', ], fail_silently = False)

	return form_data





def Contact(request):
	if request.method == 'POST':
		form = ContactUsForm(request.POST)
		if form.is_valid():
			model_instance =form.save(commit = False)
			model_instance.timestamp = timezone.now()
			model_instance.save()
			return redirect('/')


	else:
		form = ContactUsForm()
		return render(request, 'contactus.html', {'form': form})

def send_mail():
	send_mail(
		'Subject here',
		'Here is the message',
		'tosinayoola0@gmail.com',
		['tosinayoola0@gmail.com', '']
		)





