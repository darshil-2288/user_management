from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from user_app.views import CustomLoginView,home,RegisterView,profile
from user_app.forms import LoginForm

urlpatterns = [

    path('', home, name='users-home'),
    
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='profile')]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

