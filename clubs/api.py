from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import ClubSerializer, ActivitySerializer, EventSerializer, DemandeSerializer,UserSerializer,ProfileSerializer
from .models import Club, Activity, Event, demander, UserProfile

class ClubApi(ModelViewSet):
	queryset = Club.objects.all()
	serializer_class = ClubSerializer

class ProfileApi(ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = ProfileSerializer

class ActivityApi(ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

	permission_classes = (permissions.IsAuthenticated,)

class EventApi(ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
 


class UserApi(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
class DemandeApi(ModelViewSet):
	queryset = demander.objects.all()
	serializer_class = DemandeSerializer




	