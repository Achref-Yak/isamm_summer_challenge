from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 

DEFAULT_EXAM_ID = 1
# les tables de base de donnée

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='1cm')



class Club(models.Model):
	nom_de_club = models.CharField(max_length=30)
	description = models.TextField(max_length=200)
	email = models.CharField(max_length=30)
	site = models.CharField(max_length=30)


	def __str__(self):
		return self.nom_de_club

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    niveau = models.CharField(max_length=100, default='')
    skills = models.CharField(max_length=100, default='')
    site = models.CharField(max_length=100,default='')
    tel = models.IntegerField(default=0)
    club = models.ManyToManyField(Club,default=1)

 

    def __str__(self):
        return self.user.username
 


 




class Event(models.Model):
	type_de_event = models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	date = models.DateField()
	salle = models.CharField(max_length=20)
	def __str__(self):
		return self.nom_de_club

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


 