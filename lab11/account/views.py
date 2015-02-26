from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, logout, login as user_login
from account.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required

def register(request):

	context = {}

	registered = False

	if request.method == 'POST':
		user_form = UserForm(request.POST, prefix='user')
		profile_form = UserProfileForm(request.POST, prefix='profile')

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()

			user.set_password(user.password)

			user.save()

			profile = profile_form.save(commit=False)

			profile.user_profile = user

			if 'profile-user_profile_picture' in request.FILES:
				profile.user_profile_picture = request.FILES['profile-user_profile_picture']

			profile.save()

			# Flag para el formulario de registro
			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm(prefix='user')
		profile_form = UserProfileForm(prefix='profile')

	context.update({'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

	return render(request, 'account_register.html', context)


def login(request):

	if request.method == 'POST':
		
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user.is_active:

			user_login(request, user)

			return HttpResponseRedirect('/order/')

		else:
			print('Ingreso Invalido: {0}, {1}'.format(str(username, password)))
			return HttpResponse('Su cuenta esta desactivada')

	else: 
		return render(request, 'account_login.html', {})


@login_required
def user_logout(request):

	logout(request)

	return HttpResponseRedirect('/account/login/')		  