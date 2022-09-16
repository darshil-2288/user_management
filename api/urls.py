from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views
urlpatterns = [
		path('api/register/',views.UserRegistrationAPIView.as_view()),
		path('api/login/',views.UserLoginAPIView.as_view()),
		path('api/create-profile/',views.create_profile),
		path('api/profiles/<str:pk>/',views.detail_view),
		path('api-token-auth/',auth_views.obtain_auth_token)
  
]

