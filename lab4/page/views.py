#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hola desde Django")

def test(request):
	return HttpResponse("Esta es la repuesta de pruebas")