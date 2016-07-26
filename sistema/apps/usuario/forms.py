#encoding:utf-8
from django.forms import ModelForm
from django.db import models 
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

opciones=(
			('0','Administrador'),
			('1','Encargado'),
			('2','Responsable')
		)

class fperfil(ModelForm):
	class Meta:
		model=Perfil
		exclude=['user']

class fusuario(UserCreationForm):
	username=forms.CharField(max_length=40, required=True,help_text=False,label="Usuario")
	password2=forms.CharField(help_text=False,label="Contrasena de confirmacion", widget=forms.PasswordInput)
	first_name=forms.CharField(max_length=50,required=True,label="Nombre")
	last_name=forms.CharField(max_length=50,required=True,label="Apellidos")
	email=forms.EmailField(max_length=100,required=True,label="Email")
	tipo = forms.ChoiceField(choices=opciones)

	class Meta:
		model=User
		fields=("username","password1","password2","first_name","last_name","tipo","email")
	
	def save(self, commit=True):
		user=super(fusuario,self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.last_name=self.cleaned_data.get("last_name")
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return user

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username = username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de Usuario ya existe')

	def clean_last_name(self):
		last_name = self.cleaned_data['last_name']
		try:
			User.objects.get(last_name = last_name)
		except User.DoesNotExist:
			return last_name
		raise forms.ValidationError('Apellidos ya registrados')
	
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado')
	
	#def clean_password2(self):
	#	if 'password' in self.cleaned_data:
	#	password = self.cleaned_data['password']
	#	password2 = self.cleaned_data['password2']
	#	if password == password2:
	#		return password2
	#	raise forms.ValidationError('El password no coinciden')

class PersonalForm(ModelForm):
	class Meta:
		model = Personal
		fields = ('nombres','apellido_paterno','apellido_materno','cedula_identidad','cargo','email','telefono')

	#def clean_email(self):
	#	email = self.cleaned_data['email']
	#	try:
	#		User.objects.get(email=email)
	#	except User.DoesNotExist:
	#		return email
	#	raise forms.ValidationError('Email ya registrado')

class fbucar(forms.Form):
	texto = forms.CharField(max_length = 30, label = 'Buscar personal')
