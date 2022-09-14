from django.test import TestCase
from ..forms import RegisterForm,LoginForm,UpdateUserForm,UpdateProfileForm

class ValidTest(TestCase):
	def RegisterFormTest(self):
		form_data={'first_name':'darshil','last_name':'patel','username':'dar','email':'dar@dar.com','password1':'dar1234@#','password2':'dar1234@#'}
		form=RegisterForm(data=form_data)
		self.assertTrue(form.is_valid())
	def LoginFormTest(self):
		form_date={'username':'dar','password':'dar1234@#'}
		form=LoginForm(data=form_data)
		self.assertTrue(form.is_valid())
	def UpdateUserFormTest(self):
		form_data={'username':'dar','email':'dar@dar.com'}
		form=UpdateUserForm(data=form_data)
		self.assertTrue(form.is_valid())
	def UpdateProfileFormTest(self):
		form_data={'avatar':'default.jpg','bio':'hii my name is darshil'}
		form=UpdateProfileForm(data=form_data)
		self.assertTrue(form.is_valid())
