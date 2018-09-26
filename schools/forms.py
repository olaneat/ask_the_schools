from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms, ModelForm
from . models import profile, Schools, school_data, ContactUs



class profileForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name',  'username',  'password1', 'password2']
		
		def save(self, commit = True):
			user  = super(profileForm, self).save(commit =  False)
			user.first_name =  self.cleaned_data['first_name']
			user.last_name =  self.cleaned_data['last_name']
			user.email =  self.cleaned_data['email']

			if commit:
				user.save()

			return user


#class profileForm(ModelForm):
#	class Meta:
#		password = forms.CharField(widget = forms.PasswordInput)
#		model = profile
#		widget = { 'password': form.PasswordInput(),}
#		fields = ['title', 'first_name', 'surname', 'email', 'password']



class SchoolsForm(ModelForm):
	class Meta:
		model = Schools
		fields = ['name','badge', 'motto', 'advantage', 'address', 'status', 'fees_range', 'school_email', 'school_Phone_Num', 'video', 'town', 'state']

class school_dataForm(ModelForm):
	class Meta:
		model = school_data
		fields = ['curriculum', 'facilites', 'extra_curriculum', 'date_established', 'awards', 'Direction', 'website']


class ContactUsForm(ModelForm):
	class Meta:
		model = ContactUs
		fields = ['full_name', 'email',  'comment']



		