from django.urls import path
from .views import UserRegistrationAPIView,UserLoginAPIView,create_profile,detail_view
urlpatterns = [
  path('api/register/',UserRegistrationAPIView.as_view()),
  path('api/login/',UserLoginAPIView.as_view()),
  path("api/profilecreate/",create_profile,name="profile_create"),
  path('api/<str:pk>/',detail_view,name="detail_view")
]

