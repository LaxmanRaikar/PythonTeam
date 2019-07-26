from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfileInfo(models.Model):
	""" This class make the model of user and create new model in database """
	# define user field
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

	# define image field in database
	image = models.ImageField(upload_to='Images', blank=True, null=True)

	def __str__(self):
		return self.user.username


class Note(models.model):
  text = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
