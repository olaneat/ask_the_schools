from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Button, Fieldset
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . models import profile, Schools, school_data, ContactUs

clubs = (
	('jet', 'Jet Club'),
	('Science', 'Science Club'),
	('Drama', 'Drama Club'),
	('Art & Culture', 'Art & Culture Club'),
	('Debate ', 'Debate Club',),
	('Comedy', 'Comedy Club'),
	('Math', 'Mathematic Club'),
	('Literature', 'Literature Club'),
	('Books', 'Books Club'),
	('History', 'History Club'),
	('Press', 'Press Information and Photography Club'),
	('Adventure', 'Adventure Club'),
	('Religious', 'Religious Club'),
	('Charity', 'Charity Club'),
	('Feeders', 'Feeders Club'),

	)
 	

sport = (
	( 'Swimming Pool', 'Swimming '),
	('BasketBall Court ','BasketBall' ),
	('FootBall Field', 'FootBall'),
	('HandBall Court', 'HandBall'),
	('VolleyBall Court', 'VolleyBall'),
	('Race Track', 'Race'),
	('Javelline', 'Javelline'),
	('Short Put', 'Short Put'),
	('Chess Board', 'Chess')
	) 



class profileForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['email', 	'first_name', 'last_name', 'username','password1', 'password2']


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
	Name = forms.CharField(
		widget = forms.TextInput(
			attrs ={
			'placeholder': "School Name ...."
			}
	 )
		)

	motto = forms.CharField(
		widget = forms.TextInput(
			attrs ={
			'placeholder': "School motto  ...."
			}
	 )
		)

	email = forms.CharField(
		widget = forms.TextInput(
			attrs ={
			'placeholder': "Offical School email  ...."
			}
	 )
		)


	Phone = forms.CharField(
		widget = forms.TextInput(
			attrs ={
			'placeholder': "Offical School Phone Number  ...."
			}
	 )
		)


	class Meta:
		model = Schools
		fields = ['Name','badge', 'motto', 'advantage', 'address', 'status', 'fees_range', 'email', 'Phone', 'video', 'town', 'state']

class school_dataForm(ModelForm):
	extra_curriculum = forms.MultipleChoiceField(
		required = False,
		widget = forms.CheckboxSelectMultiple,
		choices = clubs 
		)


	sport_activities = forms.MultipleChoiceField(
		widget = forms.CheckboxSelectMultiple,
		required = False,
		choices = sport)


	class Meta:
		model = school_data
		fields = ['curriculum', 'sport_activities', 'extra_curriculum', 'date_established', 'awards', 'Direction', 'website']


class ContactUsForm(ModelForm):
	class Meta:
		model = ContactUs
		fields = ['full_name', 'email',  'comment']



		