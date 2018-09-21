from django.forms import forms, ModelForm
from . models import profile, Schools, school_data, ContactUs

class profileForm(ModelForm):
	class Meta:
		model = profile
		fields = ['title', 'first_name', 'surname', 'email', 'password']


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
		fields = ['full_name', 'email', 'title', 'comment']



		