from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Formation, Projets

def index(request):
	formation=Formation.objects.all()
	projets=Projets.objects.all()
	requests.get("https://serveur.pythonanywhere.com/cool/poper")
	return render(request, "index/index.html",{"formation":formation, "projets":projets})
	
def checker(request):
	return HttpResponse("iOBtt5U4fsQBzb2L5SSsIlkVQ1AQ2G9cyJTcorkwbGY.dKu2rqEOe0s1P47nC55iSK0ZHklTZpOnEByxLSVTeZg")