
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import serializers
from .models import userProfile
User = get_user_model()




class UserRegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        label="Email Address"
    )

    password = serializers.CharField(
        required=True,
        label="Password",
        
    )

   

    first_name = serializers.CharField(
        required=True
    )

    last_name = serializers.CharField(
        required=True
    )

   

    class Meta(object):
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
   
        

class UserLoginSerializer(serializers.ModelSerializer):

	    username = serializers.CharField(
	        required=True,
	        
	        write_only=True,
	    )

	    email = serializers.EmailField(
	        required=True,
	        
	        write_only=True,
	        label="Email Address"
	    )

	    

	    password = serializers.CharField(
	        required=True,
	        write_only=True,
	        style={'input_type': 'password'}
	    )

	    class Meta(object):
	        model = User
	        fields = ['email', 'username', 'password']



class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=userProfile
        fields=['id','location','description']



