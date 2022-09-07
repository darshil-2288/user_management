from user_app.models import StudentModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class register_form(UserCreationForm):
	class Meta:
		model=	User
		fields=['id','username','email','password']
class login_form(UserCreationForm):
	class Meta:
		model=	User
		fields=['email']		

