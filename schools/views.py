from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import  Schools, profile, school_data, parents_remark
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail


from django.views import generic

class SchoolDetailView(generic.ListView):
	models = Schools

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

	

class addSchools(CreateView):
	template_name =  'schoolprofile.html'
	models = Schools
	fields = ['name', 'motto', 'badge', 'level', 'advantage', 'address', 'town', 'state', 'status', 'fees_range', 'school_email', 'school_Phone_Num']


class add_School(SessionWizardView):
	template_name =  'schoolprofile.html'

	def done(self, form_list, **kwargs):
		form_data = process_data(form_list)
		return render('done.html', { 'form_data': form_data}
			)

def process_data(form_list):
	form_data = [form.cleaned_data for form in form_list]
	send_mail(form_data[0]['profile'],
		form_data[1]['Schools'], form_data[2]['school_data'],
		['tosinayoola0@gmail.com'], fail_silently = False)

	return form_data


