from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 

DEFAULT_EXAM_ID = 1
# les tables de base de donnée

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='1cm')


class Invitation(models.Model):
	user = models.OneToOneField(User)
	accepted = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

class Club(models.Model):
	superviseur = models.ForeignKey(User)
	nom_de_club = models.CharField(max_length=30)
	description = models.TextField(max_length=200)
	email = models.CharField(max_length=30)
	site = models.CharField(max_length=30)
	invitation = models.ManyToManyField(Invitation)

	def __str__(self):
		return self.nom_de_club



class Activity(models.Model):
	user = models.OneToOneField(User)
	activity = models.CharField(max_length=100, default='')

	class Meta:
		verbose_name_plural = "Activities"
	def __str__(self):
		return self.user.username



class UserProfile(models.Model):
	user = models.OneToOneField(User)
	niveau = models.CharField(max_length=100, default='')
	skills = models.CharField(max_length=100, default='')
	site = models.CharField(max_length=100,default='')
	tel = models.IntegerField(default=0)
	user_type = models.CharField(max_length=7,default='')
	image = models.ImageField(upload_to='media_cdn/', blank=True)
	activity = models.ManyToManyField(Activity,default=1,blank=True)
	club = models.ManyToManyField(Club,default=1)
	new = models.BooleanField(default=True,blank=True)
	usertype = models.CharField(max_length=100, default='',blank=True)

 

	def __str__(self):
		return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)




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


 