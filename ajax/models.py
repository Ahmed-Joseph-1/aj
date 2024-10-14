from django.db import models

# Create your models here.
class Contact(models.Model):
	name =  models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	subject = models.TextField()
	message = models.TextField()
	ip = models.CharField(max_length=50)
	details = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	