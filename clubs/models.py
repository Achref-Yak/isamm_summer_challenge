from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from datetime import date
from PIL import Image,ExifTags
from io import StringIO
import os
from django.db.models.signals import post_save
from django.dispatch import receiver

DEFAULT_EXAM_ID = 1
# les tables de base de donnée

 


 







class Club(models.Model):
	superviseur = models.ForeignKey(User,default=1,related_name='superviseur')
	nom_de_club = models.CharField(max_length=30)
	description = models.CharField(max_length=1000,default="")
	email = models.CharField(max_length=30,default="")
	site = models.CharField(max_length=30,default="")
	CoverImage = models.ImageField(upload_to='cover/',blank=True)
	staff = models.ManyToManyField(User, default=1)
 
 
	
	def __str__(self):
		return self.nom_de_club


class notification(models.Model):
	club = models.ForeignKey(Club,related_name='club_to_notification',default=1)
	user_from = models.ForeignKey(User,related_name='user_from_notification',default=1)
	info = models.CharField(max_length=65,default=1)
	seen = models.BooleanField(default=False)

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

def rotate_image(filepath):
  try:
    image = Image.open(filepath)
    for orientation in ExifTags.TAGS.keys():
      if ExifTags.TAGS[orientation] == 'Orientation':
            break
    exif = dict(image._getexif().items())

    if exif[orientation] == 3:
        image = image.rotate(180, expand=True)
    elif exif[orientation] == 6:
        image = image.rotate(270, expand=True)
    elif exif[orientation] == 8:
        image = image.rotate(90, expand=True)
    image.save(filepath)
    image.close()
  except (AttributeError, KeyError, IndexError):
    # cases: image don't have getexif
    pass
	
class Activity(models.Model):
	nom_de_club = models.ForeignKey(Club,default=1,blank=True)	
	nom_de_event = models.CharField(max_length=30, default='')
	info = models.CharField(max_length=1000, default='',blank=True)
	event = models.ForeignKey(Event,on_delete=models.CASCADE,default=1 )
	date = models.DateField(("Date"), default=date.today)
	image = models.ImageField(upload_to='pics/',blank=True,default=None)

	class Meta:
		verbose_name_plural = "Activities"
	def __str__(self):
		return self.nom_de_event
 


@receiver(post_save, sender=Activity, dispatch_uid="update_image_profile")
def update_image(sender, instance, **kwargs):
  if instance.image:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.image.url
    rotate_image(fullpath)		 



class UserProfile(models.Model):
	user = models.OneToOneField(User)
	username = models.CharField(max_length=100, default='')
	first_name = models.CharField(max_length=100, default='')
	last_name = models.CharField(max_length=100, default='')
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

@receiver(post_save, sender=UserProfile, dispatch_uid="update_image_profile")
def update_image(sender, instance, **kwargs):
  if instance.image:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.image.url
    rotate_image(fullpath)	

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


 