from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Club, Activity, Event, demander

		

class ActivitySerializer(serializers.ModelSerializer):

	class Meta:
		model = Activity 

class EventSerializer(serializers.ModelSerializer):

	class Meta:
		model = Event 

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User 
		



		
class DemandeSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = demander 


class ClubSerializer(serializers.ModelSerializer):
	demandes = DemandeSerializer(read_only=True, many=True)
	class Meta:
		model = Club		
	
		 
 
