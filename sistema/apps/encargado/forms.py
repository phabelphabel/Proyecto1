#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import *

CHOICES = (('1', 'Bueno',), ('2', 'Malo',), ('3', 'Regular',), ('4', 'Baja'))

class fcarrera(ModelForm):
	class Meta:
		model = Carrera

	def clean_nombre_carrera(self):
		nombre_carrera = self.cleaned_data['nombre_carrera']
		try:
			Carrera.objects.get(nombre_carrera = nombre_carrera)
		except Carrera.DoesNotExist:
			return nombre_carrera
		raise forms.ValidationError('Carrera ya Registrado')

class fproveedor(ModelForm):
	class Meta:
		model = Proveedor

#	def clean_nombre_proveedor(self):
#		nombre_proveedor = self.cleaned_data['nombre_proveedor']
#		try:
#			Proveedor.objects.get(nombre_proveedor = nombre_proveedor)
#		except Proveedor.DoesNotExist:
#			return nombre_proveedor
#		raise forms.ValidationError('Proveedor ya Registrado')

#	def clean_telefono(self):
#		telefono = self.cleaned_data['telefono']
#		try:
#			Proveedor.objects.get(telefono = telefono)
#		except Proveedor.DoesNotExist:
#			return telefono
#		raise forms.ValidationError('Telefono ya Registrado')

class fgrupo(ModelForm):
	class Meta:
		model = Grupo_contable

class factivo(ModelForm):
	estado = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
	#fecha_incorporacion=forms.DateField(initial='dia-mes-anio',widget=SelectDateWidget(years=lista_anios))
	class Meta:
		model = Activo