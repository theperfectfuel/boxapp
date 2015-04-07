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

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

# Create your models here.

class Location(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField(null=True, blank=True)
	address = models.CharField(null=True, blank=True, max_length=300)
	city = models.CharField(null=True, blank=True, max_length=300)
	state = models.CharField(null=True, blank=True, max_length=300)
	zipcode = models.CharField(null=True, blank=True, max_length=300)
	position = GeopositionField(null=True, blank=True)
	phone = models.CharField(null=True, blank=True, max_length=300)
	hours = models.CharField(null=True, blank=True, max_length=300)
	image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)
	showers = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
	kids_area = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
	drop_ins = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
	lifting_platforms = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
	crossfit_kids = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
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
