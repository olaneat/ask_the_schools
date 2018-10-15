from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
import uuid
from datetime import date
from django.urls import reverse

# Create your models here.


school_fees  =( 
	('#51,000.00 - #100,000.00', '#51,000.00 - #100,000.00'),
	('#101,000.00 - 200,000.00', '#101,000.00 - 200,000.00' ),
	('#201,000.00  - 300,000.00', '#201,000.00  - 300,000.00'),
	('#301,000.00  - 400,000.00', '#301,000.00  - 400,000.00'),
	('#401,000.00  - 500,000.00', '#401,000.00  - 500,000.00'),
	('#501,000.00  - 600,000.00', '#501,000.00  - 600,000.00'),	
	('#601,000.00  - 700,000.00', '#601,000.00  - 700,000.00'),	
	('#701,000.00  - 800,000.00', '#701,000.00  - 800,000.00'),
	('#801,000.00  - 900,000.00', '#801,000.00  - 900,000.00'),
	('#901,000.00  - 1,000,000.00', '#901,000.00  - 1,000,000.00'),

	)


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
	password = models.CharField(max_length =100,  )
	password2 = models.CharField(max_length =100, blank =  False,  help_text="retype your password again")
	username =  models.CharField(max_length =  100, blank = False  )


class Schools(models.Model):
	Name = models.CharField(max_length = 300, )
	motto = models.CharField(null = True, max_length = 200,  )
	badge = models.ImageField(upload_to = "media/images", null = True, blank= True, help_text = "upload a jpg file ")
	level = models.CharField(null = True, max_length = 10, choices = LEVEL)
	advantage = models.TextField(null = True, max_length = 1000, help_text = 'what do parents tend to benefit  by entrusting their children in your school not more than 1000 characters'  )
	address = models.CharField(null = True, max_length  = 250 )
	town = models.CharField(null = True, max_length = 100, help_text = 'enter the Local Government Area')
	state = models.CharField(null = True, max_length = 4, choices = STATE)	
	video = models.FileField(upload_to = 'media/video', null = True, blank= True, help_text = "upload a video file, mp4, " )	
	status = models.CharField(blank = True, max_length = 20, choices = school_status)
	fees_range = models.CharField(max_length = 70,  null = True, choices = school_fees  )
	email = models.EmailField(blank = True, max_length = 50, )
	Phone = models.CharField(null = True, max_length = 15)


	def get_absolute_url(self):
		return reverse ('school-detail', args = [str(self.id)])		


class school_data(models.Model):
	curriculum = models.CharField(max_length =7,  choices = CURRICULUM )
	facilites = models.CharField(max_length = 10)
	website = models.URLField(max_length = 100, )
	extra_curriculum = models.CharField(max_length = 20)
	date_established = models.DateField('') 
	awards = models.CharField( max_length = 150, help_text ='kindly list the schools Awards')
	Direction = models.CharField(max_length = 100, help_text ='give a brief description to your school ' )
	sport_activities = models.CharField(max_length = 50, ) 

	def get_absolute_url(self):
		return reverse('schools:detail', kwargs={'pk': self.pk})



class parents_remark(models.Model):
	full_name = models.CharField(max_length = 300, help_text = "fill in your full name" )
	school_name= models.CharField(max_length =100 , null = True  )
	comment = models.TextField(max_length =1000 )
	

class ContactUs(models.Model):
	full_name = models.CharField(max_length = 300 )
	title = models.CharField(max_length = 100, blank = True)
	email= models.EmailField(max_length =100 , null = True  )
	comment = models.TextField(max_length =1000 )

	def __str__(self):
		return self.comment