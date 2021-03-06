from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg
from geoposition.fields import GeopositionField


import os
import uuid

RATING_CHOICES = (
	(0, 'None'),
	(1, '*'),
	(2, '**'),
	(3, '***'),
	(4, '****'),
	(5, '*****'),
	)

YESNO_CHOICES = (
	(1, 'No'),
	(2, 'Yes'),
	)

GENDER_CHOICES = (
	(1, 'Male'),
	(2, 'Female'),
	(3, 'Other'),
	)

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

def upload_to_profile(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('profiles/', filename)

# Create your models here.

class Location(models.Model):
	title = models.CharField(max_length=300, verbose_name='Name of Your Gym')
	description = models.TextField(null=True, blank=True, verbose_name='Description of Your Gym')
	address = models.CharField(null=True, blank=True, max_length=300, verbose_name='Address')
	city = models.CharField(null=True, blank=True, max_length=300, verbose_name='City')
	state = models.CharField(null=True, blank=True, max_length=300, verbose_name='State')
	zipcode = models.CharField(null=True, blank=True, max_length=300, verbose_name='Zip Code')
	position = GeopositionField(null=True, blank=True)
	phone = models.CharField(null=True, blank=True, max_length=300, verbose_name='Phone')
	hours = models.CharField(null=True, blank=True, max_length=300, verbose_name='Hours')
	image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True, verbose_name='Image')
	showers = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Showers')
	kids_area = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Kids Area')
	drop_ins = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Drop Ins')
	lifting_platforms = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Lifting Platforms')
	crossfit_kids = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='CrossFit Kids')
	womens_only = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Womens Only Classes')
	corporate_training = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Corporate Training')
	spec_youth = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Youth Training')
	spec_senior = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Senior Training')
	spec_nutrition = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Nutrition')
	spec_weightmgmt = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Weight Management')
	spec_injuryrec = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Injury Recovery')
	spec_sporttrain = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Sport Specific Training')
	spec_oly = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name='Olympic Style Weightlifting')
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse(viewname="location_list", args=[self.id])

	def get_average_rating(self):
		average = self.review_set.all().aggregate(Avg('rating'))['rating__avg']
		if average == None:
			return average
		else:
			return int(average)

	def get_average_parking(self):
		average = self.review_set.all().aggregate(Avg('parking'))['parking__avg']
		if average == None:
			return average
		else:
			return int(average)

	def get_average_trainers(self):
		average = self.review_set.all().aggregate(Avg('trainers'))['trainers__avg']
		if average == None:
			return average
		else:
			return int(average)

	def get_average_friendliness(self):
		average = self.review_set.all().aggregate(Avg('friendliness'))['friendliness__avg']
		if average == None:
			return average
		else:
			return int(average)

	def get_average_intensity(self):
		average = self.review_set.all().aggregate(Avg('intensity'))['intensity__avg']
		if average == None:
			return average
		else:
			return int(average)

	def get_reviews(self):
		return self.review_set.all()

class Review(models.Model):
	location = models.ForeignKey(Location)
	user = models.ForeignKey(User)
	description = models.TextField(null=True, blank=True)
	rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	trainers = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	parking = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	friendliness = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	intensity = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
	# Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	# Additional attributes for User Profile
	age = models.IntegerField(null=True, blank=True, verbose_name='Age')
	gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True, verbose_name='Gender')
	profile_image = models.ImageField(upload_to=upload_to_profile, null=True, blank=True, verbose_name='Profile Image')

	# Override the __unicode__() method to return out something meaningful
	def __unicode__(self):
		return self.user


