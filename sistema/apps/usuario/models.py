from django.db import models
#from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
	user=models.OneToOneField(User, unique=True)
	rol=models.CharField(max_length=30)

class Personal(models.Model):
	nombres = models.CharField(max_length=30)
	apellido_paterno = models.CharField(max_length=30)
	apellido_materno = models.CharField(max_length=30)
	cedula_identidad = models.IntegerField(max_length=30)
	telefono = models.IntegerField(max_length=30)
	email = models.EmailField()
	cargo = models.CharField(max_length=30)
	#fecha=models.DateField()
	def __unicode__(self):
		return "%s %s" % (self.nombres, self.apellido_paterno)

