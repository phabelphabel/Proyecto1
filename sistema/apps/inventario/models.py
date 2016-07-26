from django.db import models

# Create your models here.

class Accesorio(models.Model):
	codigo_accesorio=models.CharField(max_length=30)
	marca=models.CharField(max_length=30)
	modelo=models.CharField(max_length=30)
	serie=models.CharField(max_length=30)
	descripcion=models.CharField(max_length=50)
	def __unicode__(self):
		return "%s"%(self.codigo_accesorio)

class Activo(models.Model):
	codigo_activo=models.CharField(max_length=30)
	codigo_estado=models.CharField(max_length=30)
	baja=models.CharField(max_length=30)

	def __unicode__(self):
		return self.Accesorio

