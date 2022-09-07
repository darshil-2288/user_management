from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import StudentModel
from user_app.forms import register_form,login_form
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.

def register(request):
	form=register_form()
	if request.method=='POST':
		form=register_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form=register_form()
	return render(request,'register.html',{'form':form})
def login(request):
		if request.method == 'POST':
			form = AuthenticationForm(request=request, data=request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				user = authenticate(username=username, password=password)
				if user is not None:
					print(user)
					
					return redirect('/home')
				else:
					print('User not found')
		else:
			form=AuthenticationForm()
		return render(request, 'login.html', {'form': form})		
