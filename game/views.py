from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
	
def index1(request):
	return HttpResponse("Hello, World. You're at the game index.")
