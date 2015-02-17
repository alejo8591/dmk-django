from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

	user_profile = models.OneToOneField(User)

	# Campos donde extien el modelo base User
	user_profile_website = models.URLField(blank=True, null=True, help_text='Ingrese su sitio Web')
	user_profile_picture = models.ImageField(upload_to='profile_images', blank=True, null=True)
	user_profile_identification = models.CharField(max_length=24,
												   unique=True,
												   verbose_name='Identificacion',
												   help_text='Ingrese su numero de Identificacion')

	def __str__(self):
		return self.user_profile.username
