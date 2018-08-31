# - * - Coding: utf -8 - * -
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from clubs.forms import ClubForm, RegistrationForm, UserLoginForm,ProfileRegister, ActivityForm,EventForm, InviForm
from django.contrib.auth.views import login
from django.http import Http404,HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from  clubs.models import UserProfile, Club, Activity,Event, demander, notification
from datetime import date
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

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


def event_view(request,string):
	cal = {'0':["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"],'1':["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"],'2':["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]}
	user = request.user
	template_name='home/event.html'
	event = Event.objects.get(nom_de_event=string)
	acts = Activity.objects.filter(nom_de_event=string)
	club = Club.objects.get(nom_de_club=event.club)
 
	if  request.method == 'POST':

 
		activity =  ActivityForm(data=request.POST,files=request.FILES)
		if activity.is_valid():
			edit = activity.save(commit=False)
			edit.nom_de_club = club
			edit.nom_de_event = string
			
	 
			
		
		
			edit.save()
		 
			
		 


		
		return redirect("/isamm/event/"+string)
	else :
		event = Event.objects.get(nom_de_event=string)
		activity =  ActivityForm(initial={'info': ' '})
		
 
		args = {'event':event,'acts':acts,'date':date.today,'nom_de_club':club,'nom_de_event':string,'activity':activity,'club_form':club,'calenderier':cal}
		return render(request, template_name,args)	



def club_view(request,string):
	users = User.objects.all()
	user = request.user
	template_name='home/club.html'
	
	club = Club.objects.get(nom_de_club=string)
	nb_event =  Event.objects.all().count()
	events =Event.objects.filter(club=club)
	user_from_name =UserProfile.objects.get(user=club.superviseur)
	
	if request.method == 'POST' and 'edit' in request.POST:
		clubedit = ClubForm(data=request.POST,files=request.FILES,instance=club)
		edit = clubedit.save(commit=False)
 
		edit.save()
		return redirect("/isamm/club/"+request.POST['nom_de_club'])


	elif request.method == 'POST' and 'event' in request.POST:
		event = EventForm(data=request.POST)
		edit = event.save(commit=False)
		edit.club = club
		edit.admin = user
		edit.save()
		event_name = request.POST['nom_de_event']
		return redirect("/isamm/event/"+event_name)
		
	elif request.method == 'POST' and 'invi' in request.POST:
 
		b = demander(user_from=request.user,user_from_name=user.last_name,user_to=club.superviseur,accepted=False,invi_type="club",club=club)
		b.save()
		return redirect("/isamm/club/"+string)

 
 
	else:
		club_form = Club.objects.get(nom_de_club=string)
		staff =club_form.staff 
		clubedit = ClubForm(initial={'nom_de_club': club.nom_de_club,'description':club.description,'email':club.email,'site':club.site,'staff':staff})
		activity = ActivityForm()
		event = EventForm()
		demande = InviForm()
		args = {'club_form':club_form,'clb':club,'user':user,'event':event,'demande':demande, 'events':events,'activity':activity,'nb_event':nb_event,'clubEdit':clubedit}
		return render(request, template_name,args)	


def ProfileView(request, string=None):
	template_name='home/profile.html'
	me = request.user
	
	if string:
		user = User.objects.get(username=string)
		nots = notification.objects.filter(user_from=user)
	else:
		
		user = request.user
		nots = notification.objects.filter(user_from=user)
	args = {'user': user,'me':me,'notifications':nots}	
	return render(request, template_name,args)	

 


def InvitationView(request,add=None,delete=None):
	template_name='home/invitation.html'
	ins = demander(user_to=request.user)
	demande = demander.objects.filter(user_to=request.user)
	 
	invi = InviForm(data = request.POST, instance=ins) 
	if add:
		demander.objects.filter(user_from_name=add).update(accepted=True)
		x = demander.objects.get(user_from_name=add)
		info= " participé a {}".format(str(x.club))
		 
		b = notification(club=x.club,user_from=x.user_from, info=info)
		b.save()
		return redirect("/isamm/invitations")
	if delete:
		demander.objects.get(user_from_name=delete).delete()
		return redirect("/isamm/invitations")

	
	args = {'invi': demande}	
	return render(request, template_name, args)




def ProfileEdit(request):
	template_name='home/profileEdit.html'
	user = UserProfile.objects.get(user=request.user)
	if request.method =='POST':	 
 

		
		user_profile = ProfileRegister(data=request.POST, files=request.FILES,  instance=user)
		if user_profile.is_valid():
			edit = user_profile.save(commit=False)
			edit.username = request.user.username
			edit.first_name = request.user.first_name
			edit.last_name = request.user.last_name
			edit.save()
      
		args = {'user_profile': user_profile}
		return render(request, template_name, args)
	else :
		
		user_profile = ProfileRegister(initial={"niveau":user.niveau,'skills':user.skills,'site':user.site,'tel':user.tel,'image':user.image})
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

