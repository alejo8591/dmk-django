from django.shortcuts import render

def index(request):
	context = {'title': 'Titulo del Index de la Aplicacion testing en el template ubicado en "templates/testing/index.html"'}

	return render(request, 'testing/index.html', context)