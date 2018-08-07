from django.db import models
import uuid
from datetime import date
from django.urls import reverse

# Create your models here.


class Schools(models.Model):
	School_name = models.CharField(max_length = 300, help_text  = "fill in the name of the school below")
	address = models.CharField(max_length  = 250 )
	school_badge = models.FileField(upload_to = "media/images", default = True, help_text = "upload a jpg file ")
	school_info = models.TextField(max_length = 1000)
	short_video = models.FileField(upload_to = 'media/video', default = True, help_text = "upload a video file, mp4, " )	


	def get_absolute_url(self):
		return reverse ('school-detail', args = [str(self.id)])		

class parent_signup(models.Model):
	first_name = models.CharField(max_length = 100, help_text = "enter your first name" )
	surname = models.CharField(max_length = 150, help_text = "enter your surname")
	bio = models.TextField(max_length = 1000)
	dirth_of_birth = models.CharField(max_length = 15, help_text = "please enter a valid birth date YYYY-MM-DD")
	email = models.CharField(max_length =50)
	phone_no = models.CharField(max_length = 15, blank = True)

	def __str__(self):
		return '%s, %s'%(self.surname, self.first_name)

	def __str__(self):
		return '{0}, {1} '.format(self.surname, self.first_name) 