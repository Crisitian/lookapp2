from django.db import models

# Create your models here.
class Usuario(models.Model):
	userID = models.IntegerField(primary_key=True)
	userNickname = models.CharField(max_length=50)
	userName = models.CharField(max_length=50)
	userPassword = models.CharField(max_length=100)
	userIPAdress = models.CharField(max_length=15)
