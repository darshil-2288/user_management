from . import serializers
from rest_framework import generics, permissions, status, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from .models import userProfile

class UserRegistrationAPIView(generics.CreateAPIView):
	permission_classes = (permissions.AllowAny, )
	serializer_class = serializers.UserRegistrationSerializer
	queryset = User.objects.all()
	for user in queryset:
		Token.objects.get_or_create(user=user)

class UserLoginAPIView(views.APIView):
		permission_classes = (permissions.AllowAny, )
		serializer_class = serializers.UserRegistrationSerializer
		def post(self, request):
			serializer = self.serializer_class(data=request.data)
			if serializer.is_valid(raise_exception=True):
				return Response(serializer.data, status=status.HTTP_200_OK)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_profile(request):
	queryset=userProfile.objects.all()
	serializer=serializers.userProfileSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['GET'])
def detail_view(request,pk):
	profile=userProfile.objects.get(id=pk)
	serializer=serializers.userProfileSerializer(profile,many=False)
	return Response(serializer.data)			

