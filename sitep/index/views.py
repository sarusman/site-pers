from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Formation, Projets

def index(request):
	formation=Formation.objects.all()
	projets=Projets.objects.all()
	return render(request, "index/index.html",{"formation":formation, "projets":projets})
	
