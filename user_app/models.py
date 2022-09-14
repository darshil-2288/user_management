from django.db import models
from django.contrib.auth.models import User,AbstractUser
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
	bio = models.TextField(max_length=100)

	def __str__(self):
		return self.user.username


class User(User):
	is_email_verified=models.BooleanField(default=False)

	def __str__(self):
		return self.username	
