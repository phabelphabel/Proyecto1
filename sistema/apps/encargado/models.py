from django.db import models
from django.contrib.auth.models import *
from sistema.apps.usuario.models import *
import qrcode  
from qrcode import *
import StringIO

# Create your models here.

class Carrera(models.Model):
	nombre_carrera = models.CharField(max_length = 30)
	responsable = models.ForeignKey(Personal, null = True, blank = True)
	def __unicode__(self):
		return self.nombre_carrera

class Proveedor(models.Model):
	nombre_proveedor = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 50)
	telefono = models.IntegerField(max_length = 30, null=True)
	def __unicode__(self):
		return self.nombre_proveedor

class Grupo_contable(models.Model):
	nombre_grupo_contable = models.CharField(max_length = 50)
	def __unicode__(self):
		return self.nombre_grupo_contable

class Activo(models.Model):
	nombre_activo = models.CharField(max_length = 50)
	descripcion = models.CharField(max_length = 50)
	precio = models.FloatField(null=False)
	fecha_incorporacion = models.DateField()
	cantidad = models.IntegerField()
	estado = models.CharField(max_length = 50)
	grupo_contable = models.ForeignKey(Grupo_contable, null = True, blank = True)
#	grupo_contable = models.CharField(max_length = 50)
	caracteristicas = models.CharField(max_length = 50)
	ubicacion_activo = models.CharField(max_length = 50)
#	unidad_trabajo = models.CharField(max_length = 50)
	proveedor = models.CharField(max_length = 50)
#	proveedor_donacion = models.ForeignKey(Proveedor, null = True, blank = True)
	asignar_personal = models.ForeignKey(Personal, null = True, blank = True)

	qrcode = models.ImageField(upload_to = 'qrcode', blank = True, null = True)

#	def get_absolute_url(self):
#		return reverse('activo.views.details', args = [str(self.id)])

	def generate_qrcode(self):
		qr = qrcode.QRCode(
			version = 1,
			error_correction = qrcode.constants.ERROR_CORRECT_L,
			box_size = 6,
			border = 0,
		)
		qr.add_data('Activo')
#		qr.add_data(self.get_absolute_url())
		qr.make(fit = True)
		img = qr.make_image()
		rute = '%s/%s' % (MEDIA_ROOT, 'codigo/qr.png')
		img.save(ruta)
#		buffer = StringIO.StringIO()
#		img.save(buffer)
#		filename = 'activo-%s.png'%(self.id)
#		filebuffer = InMemoryUploadedFile(
#			buffer, None, filename, 'image/png"', buffer.len, None)
#		self.qrcode.save(filename, filebuffer)



#	def generate_qrcode(self):
#		qr = qrcode.QRCode(
#			version = 1,
#			error_correction = qrcode.constants.ERROR_CORRECT_L,
#			box_size = 6,
#			border = 0,
#		)
#		qr.add_data(self.id)
#		qr.make(fit = True)
#		img = qr.make_image()
#		buffer = StringIO.StringIO()
#		img.save(buffer)
#		filename = '%s.png' % (self.id)
#		filebuffer = InMemoryUploadedFile(
#			buffer, None, filename, 'image/png', buffer.len, None)
#		self.qrcode.save(filename, filebuffer)
