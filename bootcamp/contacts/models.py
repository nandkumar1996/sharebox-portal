from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Contact_form(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	message = models.CharField(max_length=4000)
	
