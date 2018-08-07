from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .models import parent_signup, Schools
from django.contrib.auth.forms import UserCreationForm


from django.views import generic

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

	

def signUp(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form._cleaned_data.get('username')
			raw_password = form._cleaned_data.get('password')
			user = authenticate(username=username, raw_password=password)
			login(request, user)
			return('parent')
		else:
			form = UserCreationForm()
			return render(request, 'signup.html', {form.form})
