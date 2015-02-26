from django import forms
from django.contrib.auth.models import User
from account.models import UserProfile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('user_profile_website', 'user_profile_picture', 'user_profile_identification',)
		excludes = ('user_profile',)