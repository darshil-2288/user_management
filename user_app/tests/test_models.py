from django.test import TestCase
from ..models import Profile
from django.contrib.auth.models import User
from datetime import datetime

class test_str_string(TestCase):
	def test(self):
		user=User.objects.create_user(username="darshil",email="darshil@darshil.com",password="dnp123")
		user.save()
		self.assertEqual(str(user),'darshil')
	


