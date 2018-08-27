from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from datetime import date

DEFAULT_EXAM_ID = 1
# les tables de base de donnée

 


 







class Club(models.Model):
	superviseur = models.ForeignKey(User,default=1,related_name='superviseur')
	nom_de_club = models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	email = models.CharField(max_length=30)
	site = models.CharField(max_length=30)
 
 
	
	def __str__(self):
		return self.nom_de_club


class demander(models.Model):
	user_from = models.ForeignKey(User,related_name='user_from',default=1)
	user_from_name = models.CharField(max_length=35,default=1)
	user_to = models.ForeignKey(User,related_name='user_to',default=1)
	accepted = models.BooleanField(default=False)
	invi_type = models.CharField(max_length=20,default="")
	club = models.ForeignKey(Club,default=1)
	
	def __str__(self):
		return self.user_from_name


class Event(models.Model):
	admin  = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	club = models.ForeignKey(Club, on_delete=models.CASCADE,default=1)
	nom_de_event =  models.CharField(max_length=50,default="")
	type_de_event = models.CharField(max_length=50,default="")
	description = models.CharField(max_length=200,default="")
	date = models.DateField()
	salle = models.CharField(max_length=20,default="")
	recompenses = models.CharField(max_length=20,default="")
	partenaires = models.CharField(max_length=20,default="")
	sponsors  = models.CharField(max_length=20,default="")
	def __str__(self):
		return self.nom_de_event


class Activity(models.Model):
	nom_de_club = models.ForeignKey(Club,default=1,blank=True)	
	nom_de_event = models.CharField(max_length=30, default='')
	info = models.CharField(max_length=1000, default='')
	event = models.ForeignKey(Event,on_delete=models.CASCADE,default=1 )
	date = models.DateField(("Date"), default=date.today)

	class Meta:
		verbose_name_plural = "Activities"
	def __str__(self):
		return self.info

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	niveau = models.CharField(max_length=100, default='')
	skills = models.CharField(max_length=100, default='')
	site = models.CharField(max_length=100,default='')
	tel = models.IntegerField(default=0)
	user_type = models.CharField(max_length=7,default='')
	image = models.ImageField(upload_to='profile/', default='profile/default-user.png')
	
	club = models.ManyToManyField(Club,default=1)
	new = models.BooleanField(default=True,blank=True)
	usertype = models.CharField(max_length=100, default='',blank=True)

 

	def __str__(self):
		return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)






class President(models.Model):
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	niveau = models.CharField(max_length=30)
	club= models.ForeignKey(Club, on_delete=models.CASCADE)
	def __str__(self):
		return self.nom


class SuperAdmin1(models.Model):
	class Meta:
		verbose_name_plural = "SuperAdmin1"
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	niveau = models.CharField(max_length=30)
	club= models.ForeignKey(Club, on_delete=models.CASCADE)
	def __str__(self):
		return self.nom

class SuperAdmin2(models.Model):
	class Meta:
		verbose_name_plural = "SuperAdmin2"
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	niveau = models.CharField(max_length=30)
	club= models.ForeignKey(Club, on_delete=models.CASCADE)
	def __str__(self):
		return self.nom

class admin(models.Model):
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	niveau = models.CharField(max_length=30)
	club= models.ForeignKey(Club, on_delete=models.CASCADE)
	def __str__(self):
		return self.nom


 
class Etudiant(models.Model):

	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	niveau = models.CharField(max_length=30)
	
	username = models.CharField(max_length=30,default="")
	password = models.CharField(max_length=50,default="")
 
	 
	def __str__(self):
		return self.nom


 