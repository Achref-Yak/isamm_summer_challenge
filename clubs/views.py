# - * - Coding: utf -8 - * -
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from clubs.forms import ClubForm, RegistrationForm, UserLoginForm,ProfileRegister
from django.contrib.auth.views import login
from django.http import Http404,HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from  clubs.models import UserProfile, Club
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,logout)

 


def club_create_view(request):
	template_name='home/club_create.html'
	if request.method =='POST':	 
		
		club = ClubForm(request.POST)
		instance = club.save(commit=False)
		instance.superviseur = request.user
		instance.save()
		args= {'club':club}
		return render(request, template_name,args)	
	else:
		club = ClubForm()
		args= {'club':club}
		return render(request, template_name,args)	



def club_view(request,string):
	 template_name='home/club.html'
	 club = Club.objects.get(nom_de_club=string)
	 args = {'club':club}
	 return render(request, template_name,args)	

def ProfileView(request, string=None):
	template_name='home/profile.html'
	me = request.user
	if string:
		user = User.objects.get(username=string)
	else:
		
		user = request.user
	args = {'user': user,'me':me}	
	return render(request, template_name,args)	

def ProfileEdit(request):
	template_name='home/profileEdit.html'
	if request.method =='POST':	 
		"""
		user_profile =ProfileRegister()
		niveau = request.POST['niveau']
		skills = request.POST['skills']
		site = request.POST['site']
		tel = request.POST['tel']
		image = request.POST['image']
		UserProfile.objects.filter(user=request.user).update(niveau=niveau,skills =skills,site=site,tel=tel,image=image)"""

		user = UserProfile.objects.get(user=request.user)
		user_profile = ProfileRegister(request.POST or None, request.FILES or None,  instance=user)
		if user_profile.is_valid():
			edit = user_profile.save(commit=False)
			edit.save()
      
		args = {'user_profile': user_profile}
		return render(request, template_name, args)
	else :
		
		user_profile = ProfileRegister()
		user_new = UserProfile.objects.get(user=request.user)
		#if user_new.new == True:

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

