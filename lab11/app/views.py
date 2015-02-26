from django.shortcuts import render

def index(request):
	context = {'message':'hola django'}
	return render(request, 'index.html', context)