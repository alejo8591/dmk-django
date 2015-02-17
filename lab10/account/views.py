from django.shortcuts import render
from django.contrib.auth import authenticate, login
from account.forms import UserForm, UserProfileForm

def register(request):

	register = False

	if request.method == 'POST':
		user_form = UserForm(request.POST, prefix='user')
		profile_form = UserProfileForm(request.POST, prefix='profile')

		if user_form:
			pass
