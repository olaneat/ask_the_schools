from django.forms import forms
from . models import profile, Schools, school_data

class profileForm(forms.Form):
	class Meta:
		Model = profile


class SchoolsForm(forms.Form):
	class Meta:
		Model = Schools

class school_dataForm(forms.Form):
	class Meta:
		Model = school_data
		