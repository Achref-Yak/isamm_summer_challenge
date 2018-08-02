# importer les modules des formulaires
from django import forms
from clubs.models import Club
from django.core.exceptions import ValidationError

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


 
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

