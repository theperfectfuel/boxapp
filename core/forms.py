from django import forms
from django.contrib.auth.models import User
from registration.forms import RegistrationForm


GENDER_CHOICES = (
	(0, '...'),
	(1, 'Male'),
	(2, 'Female'),
	(3, 'Other'),
	)

class ExRegistrationForm(RegistrationForm):
	age = forms.IntegerField()
	gender = forms.ChoiceField(choices=GENDER_CHOICES)
	profile_image = forms.ImageField()