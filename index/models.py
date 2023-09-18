from django.db import models

class Formation(models.Model):
	ids=models.CharField(max_length=200)
	titre=models.CharField(max_length=200)
	lieu=models.CharField(max_length=200)
	datee=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	image=models.CharField(max_length=5000)

class Projets(models.Model):
	ids=models.CharField(max_length=200)
	titre=models.CharField(max_length=200)
	datee=models.CharField(max_length=200)
	desciption=models.CharField(max_length=5000)
	image=models.CharField(max_length=5000)
	langage=models.CharField(max_length=500)