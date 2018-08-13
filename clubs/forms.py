# importer les modules des formulaires
from django import forms
from clubs.models import Club, Etudiant, UserProfile
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,logout)

class ProfileRegister(forms.ModelForm):
	tel = forms.CharField(required=False)
	niveau = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'niveau'}))
	skills = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'skills'}))
	site  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'site'}))
	tel  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'telephone'}))
	club = forms.ModelChoiceField(queryset=Club.objects.all())
	class Meta:
		model = UserProfile
		fields = {'niveau','skills','site','tel','club'}

class RegistrationForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

         


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
       

        if commit:
            user.save()

        return user


 
#la formulaire de ClubForm
class ClubForm(forms.ModelForm):
	nom_de_club = forms.CharField(max_length=30)
	description = forms.CharField(max_length=200)
	email = forms.CharField(max_length=30)
	site = forms.CharField(max_length=30)

	class Meta:
		model = Club
		fields = {'nom_de_club','description','email','site'}

	def cleaned_email(self):
		print(self.cleaned_data)
		email_qs = Club.objects.filter("email")
		if email_qs.exists():
			raise forms.ValidationError("This email has already been registered")

"""class user(forms.ModelForm):
	nom = forms.CharField(max_length=20)
	prenom = forms.CharField(max_length=20)
	email = forms.EmailField(validators=[validate_edu_email_address])
	password1 = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())
"""



class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		if not user:
			raise forms.ValidationError("This user does not exist")
		if not user.check_password(password):
			raise forms.ValidationError("Incorrect password")
		if not user.is_active:
			raise forms.ValidationError("This user is not longer active.")
		return super(UserLoginForm,self).clean()



NIVEAU = (
    ('1cm', '1cm'),
    ('2cm', '2cm'),
    ('3cm', '3cm'),
)

 