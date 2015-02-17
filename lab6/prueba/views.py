from django.shortcuts import render

def index(request):
	context = {
		'title': 'Mis Peliculas',
		'description': 'Esta es mi pagina de peliculas',
		'movie': 'Inception',
		'director': 'Christopher Nolan',
		'genre': 'Ciencia Ficcion'
	}

	return render(request, 'prueba/index.html', context)