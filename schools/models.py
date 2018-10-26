from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
import uuid
from . choice_mode import school_status, level, curriculum, STATE, school_fees
from datetime import date
from django.urls import reverse

# Create your models here.






class Schools(models.Model):
	

	SCHOOL_NAME = models.CharField(max_length = 300, null = False )
	MOTTO = models.CharField(null = False, max_length = 200,  )
	BADGE = models.ImageField(upload_to = "media/images", null = False, blank= True, help_text = "upload a jpg file ")
	LEVEL = models.CharField(null = False, blank=True, max_length = 20, choices =level )
	ADVANTAGE = models.TextField(null = True, max_length = 1000, help_text = 'what do parents tend to benefit  by entrusting their children in your school not more than 1000 characters'  )
	ADDRESS = models.CharField(null = False, max_length  = 250 )
	TOWN = models.CharField(null = False, max_length = 100, help_text = 'enter the Local Government Area')
	STATE = models.CharField(null = False, max_length = 4, choices = STATE)	
	VIDEO = models.FileField(upload_to = 'media/video', null = False, blank= True, help_text = "upload a video file, mp4, " )	
	SCHOOL_TYPE = models.CharField(blank = True, max_length = 20, choices = school_status)
	FEES_RANGE = models.CharField(max_length = 70,  null = True, choices = school_fees  )
	EMAIL = models.EmailField(blank = True, max_length = 50, )
	PHONE = models.CharField(null = False, max_length = 15)



	def get_absolute_url(self):
		return reverse ('school-detail', args = [str(self.id)])		


class school_data(models.Model):

	
	CURRICULUM = models.CharField(max_length =20,  choices = curriculum )
	WEBSITE = models.URLField(max_length = 100, blank = True )
	EXTRA_CURRICULUM = models.CharField(max_length = 20)
	AWARDS = models.CharField( max_length = 150, blank = True,  help_text ='kindly list the schools Awards')
	DIRECTION = models.CharField(max_length = 100, help_text ='give a brief description to your school ' )
	SPORT_ACTIVITIES = models.CharField(max_length = 50, null = False ) 

	def get_absolute_url(self):
		return reverse('schools:detail', kwargs={'pk': self.pk})




class parents_remark(models.Model):
	full_name = models.CharField(max_length = 300, help_text = "fill in your full name" )
	school_name= models.CharField(max_length =100 , null = False  )
	comment = models.TextField(max_length =1000 )
	

class ContactUs(models.Model):
	full_name = models.CharField(max_length = 300 )
	title = models.CharField(max_length = 100, blank = True)
	email= models.EmailField(max_length =100 , null = False )
	message = models.TextField(max_length =1000 )

	def __str__(self):
		return self.comment