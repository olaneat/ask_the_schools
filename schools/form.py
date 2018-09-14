from django.forms import form
from . import Model

class profileForm(forms.ModelForm):
	class Meta:
		Model = profile


class SchoolsForm(forms.ModelForm):
	class Meta:
		Model = Schools

class school_dataForm(forms.ModelForm):
	class Meta:
		Model = school_data
		