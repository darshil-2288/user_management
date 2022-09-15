from django.contrib.auth import get_user_model
from rest_framework.response import Response
from . import serializers
from rest_framework import status,generics,views
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import userProfile
from .serializers import userProfileSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import io
from rest_framework.decorators import api_view
from django.shortcuts import HttpResponse



User=get_user_model()
class UserRegistrationAPIView(generics.CreateAPIView):
	"""
	Endpoint for user registration.
	"""


	serializer_class = serializers.UserRegistrationSerializer
	queryset = User.objects.all()

class UserLoginAPIView(views.APIView):
	"""
	Endpoint for user login. Returns authentication token on success.
	"""

	serializer_class = serializers.UserLoginSerializer

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			return Response(serializer.data, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_profile(request):
	queryset=userProfile.objects.all()
	serializer=userProfileSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['GET'])
def detail_view(request,pk):
	profile=userProfile.objects.get(id=pk)
	serializer=userProfileSerializer(profile,many=False)
	return Response(serializer.data)





    


    


