from django.test import TestCase,client
from django.urls import reverse
from django.contrib.auth.models import User
from ..forms import UpdateUserForm


class BaseTest(TestCase):
	def setUp(self):
		self.register_url=reverse('register')
		self.login_url=reverse('login')
		self.profile_url=reverse('profile')
		self.user={
			'first_name':'rajesh',
			'last_name':'patel',  
			'username':'rajesh_patel',
			'email':'rajesh@rajesh.com',
			'password1':'rajesh1234@#',
			'password2':'rajesh1234@#'
				
		}

		
		
		
		self.usertemplateredirection={
			'first_name':'darshil',
			'last_name':'patel',
			'username':'rajesh',
			'email':'rajesh@raje.com',
			'password1':'hel1234@#',
			'password2':'hel1234'
			}
		return super().setUp()

class RegisterTest(BaseTest):
	def test_can_view_page(self):
		response=self.client.get(self.register_url)
		self.assertEqual(response.status_code,200)
	def test_can_register_user(self):
		response=self.client.post(self.register_url,self.user,format='text/html')
		self.assertEqual(response.status_code,302)
	def test_template_redirection(self):
		response=self.client.post(self.register_url,self.usertemplateredirection,format='text/html')
		self.assertTemplateUsed(response,'register.html')

class LoginTest(BaseTest):
	def test_can_access_page(self):
		response=self.client.get(self.login_url)
		self.assertEqual(response.status_code,200)
		


class ProfileTest(BaseTest):
	def test_can_view_page(self):
		response=self.client.post(self.profile_url)
		self.assertEqual(response.status_code,302)


	#if user is un-authenticated
	def test_redirect_user(self):
		response=self.client.get(self.profile_url,format='text/html')
		self.assertRedirects(response,'/login/?next=/profile/')




	


					
