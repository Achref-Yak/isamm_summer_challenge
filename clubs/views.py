# - * - Coding: utf -8 - * -
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from clubs.forms import ClubForm

class LoginView(TemplateView):
	template_name='home/index.html'

	def get(self, request):
		form= ClubForm()
		return render(request, self.template_name,{'form':form})

	def post(self, request):
		form = ClubForm(request.POST)
		if form.is_valid():
			club = form.save(commit=False)
			club.save()
		return render(request, self.template_name, {'form': form})	

def ProfileView(request):
	template_name='home/profile.html'
	return render(request, template_name, {})	