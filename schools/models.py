from django.db import models
from django.forms import ModelForm
import uuid
from datetime import date
from django.urls import reverse

# Create your models here.

Title =(
	('Mr.', 'Mr.'),
	('Mrs.', 'Mrs.'),
	('Miss', 'Miss'),
	('Barr.', 'Barr.'),
	('Dr.', 'Dr'),
	('Prof', 'Prof'),
	)

school_status = (
	('Day', 'Day'),
	('Boarding', 'Boarding'),
	('Boarding and Day', 'Boarding and Day'),
	) 

STATE = (
	('ABI', 'ABIA'),
	('ADA', 'ADAMAWA'),
	('AKW', 'AKWA IBOM'),
	('ANA', 'ANAMBRA'),
	('BAU', 'BAUCHI'),
	('BAY', 'BAYELSA'),
	('BEN', 'BENUE'),
	('BOR', 'BORNO'),
	('CRO', 'CROSS RIVER'),
	('DEL', 'DELTA'),
	('EBO', 'EBONYI'),
	('EDO', 'EDO'),
	('EKI', 'EKITI'),
	('ENU', 'ENUGU'),
	('GOM', 'GOMBE'),
	('IMO', 'IMO'),
	('JIG', 'JIGAWA'),
	('KAD', 'KADUNA'),
	('KAN', 'KANO'),
	('KAT', 'KATSINA'),
	('KEB', 'KEBBI'),
	('KOG', 'KOGI'),
	('KWA', 'KWARA'),
	('LAG', 'LAGOS'),
	('NAS', 'NASARAWA'),
	('NIG', 'NIGER'),
	('OGU', 'OGUN'),
	('OND', 'ONDO'),
	('OSU', 'OSUN'),
	('OYO', 'OYO'),
	('PLA', 'PLATEAU'),
	('RIV', 'RIVERS'),
	('SOK', 'SOKOTO'),
	('TAR', 'TARABA'),
	('YOB', 'YOBE'),
	('ZAM', 'ZAMFARA'),
	('FCT', 'FEDERAL CAPITAL TERRITORY'),
	)

CURRICULUM = (
	('Bri', 'British'),
	('Ame', 'American'),
	('Bri & Ame', 'British American'),
	('Ger', 'German'),
	('Fre', 'French'),

	)

LEVEL = (
	('Pri', 'Primary' ),
	('Sec', 'Secondary',),
	('Pri and Sec', 'Primary and Secondary')
	) 

class profile(models.Model):
	title = models.CharField(max_length = 5, choices = Title)
	first_name = models.CharField(max_length = 50, blank = False)
	surname = models.CharField(max_length = 50, blank = False)
	email = models.EmailField(max_length = 100, help_text = "enter your E-mail address here")
	password = models.CharField(max_length =100 )

class Schools(models.Model):
	name = models.CharField(max_length = 300, help_text  = "fill in the name of the school below")
	motto = models.CharField(null = True, max_length = 200, help_text = 'enter the school motto above ' )
	badge = models.FileField(upload_to = "media/images", null = True, blank= True, help_text = "upload a jpg file ")
	level = models.CharField(null = True, max_length = 10, choices = LEVEL)
	advantage = models.TextField(null = True, max_length = 1000, help_text = 'what do parents tend to benefit  by entrusting their children in your school not more than 1000 characters'  )
	address = models.CharField(null = True, max_length  = 250 )
	town = models.CharField(null = True, max_length = 100, help_text = 'enter the Local Government Area')
	state = models.CharField(null = True, max_length = 4, choices = STATE)	
	video = models.FileField(upload_to = 'media/video', null = True, blank= True, help_text = "upload a video file, mp4, " )	
	status = models.CharField(blank = True, max_length = 20, help_text ="kindly select the school type i.e Boarding or Day", choices = school_status)
	fees_range = models.CharField(max_length = 70, help_text = 'kindly enter the appropriate fees', null = True)
	school_email = models.EmailField(blank = True, max_length = 50, help_text = "enter the school email address")
	school_Phone_Num = models.CharField(null = True, max_length = 15)


	def get_absolute_url(self):
		return reverse ('school-detail', args = [str(self.id)])		


class school_data(models.Model):
	curriculum = models.CharField(max_length =7,  choices = CURRICULUM )
	facilites = models.CharField(max_length = 10)
	website = models.CharField(max_length = 100, )
	extra_curriculum = models.CharField(max_length = 20)
	date_established = models.DateField('') 
	awards = models.CharField( max_length = 150, help_text ='kindly list the schools Awards')
	Direction = models.CharField(max_length = 100, help_text ='give a brief description to your school ' )

	def get_absolute_url(self):
		return reverse('schools:detail', kwargs={'pk': self.pk})



class parents_remark(models.Model):
	full_name = models.CharField(max_length = 300, help_text = "fill in your full name" )
	school_name= models.CharField(max_length =100 , null = True  )
	comment = models.TextField(max_length =1000 )
	