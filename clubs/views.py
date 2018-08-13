# - * - Coding: utf -8 - * -
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from clubs.forms import ClubForm, RegistrationForm, UserLoginForm,ProfileRegister
from django.contrib.auth.views import login
from django.http import Http404,HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from  clubs.models import UserProfile
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,logout)

 
 

def ProfileView(request):
	template_name='home/profile.html'
	user = request.user
	args = {'user': user}
	return render(request, template_name,args)	

def ProfileEdit(request):
	template_name='home/profileEdit.html'
	if request.method =='POST':
		user_profile = ProfileRegister(request.POST)
		niveau =request.POST.get("niveau")
		tel =request.POST.get("tel")
		skills =request.POST.get("skills")
		niveau =request.POST.get("niveau")
		site =request.POST.get("site")
		club =request.POST.get("club")
		
		instance = user_profile.save(commit=False)
		instance.user = request.user
		instance.niveau = niveau
		instance.tel = tel
		instance.skills = skills
		instance.site = site
		instance.club.id = club
		instance.save()
		 
		args = {'user_profile': user_profile}
		return render(request, template_name, args)
	else :
		user_profile = ProfileRegister()
		args = {'user_profile': user_profile}
		return render(request, template_name, args)

def register(request):
	template_name='home/index.html'
 
	if request.method =='POST':
		user_registration = RegistrationForm(request.POST)
 
		if user_registration.is_valid():
			user_registration.save()
		args = {"user_registration":user_registration}
		return redirect("/isamm/login",message='seccuss')
	else:
		user_registration = RegistrationForm()
		args = {'user_registration': user_registration}
		return render(request, template_name, args)

def login_view(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request,user)
		print(request.user.is_authenticated())
		return redirect("/isamm/profileEdit")
	return render(request, "home/login.html",{"form":form})

def logout_view(request):
	logout(request)
	print(request.user.is_authenticated())

