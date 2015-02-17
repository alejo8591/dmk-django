from django.http import HttpResponse

def index(request):
	return HttpResponse("Testing")

def one(request):
	return HttpResponse("One")

def two(request):
	return HttpResponse('Two')

def three(request):
	return HttpResponse("Three")
