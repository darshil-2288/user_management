from django.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import userProfile

class UserRegistrationSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=['username','email','password']


class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=userProfile
        fields=['id','location','description']




