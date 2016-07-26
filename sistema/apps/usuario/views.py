from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from forms import *
from django.db.models import Q

from models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import login, authenticate, logout

#from django.conf import setting
import os
import StringIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string
import datetime

#from sistema.setting import RUTA_PROYECTO
#from sistema.setting import MEDIA_ROOT
#import csv
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import A4, cm
#from reportlab.lib.styles import getSampleStyleSheet
#from reportlab.platypus import Paragraph, Table, TableStyle, Image
#from reportlab.lib.enums import TA_CENTER
#from reportlab.lib import colors
#this_path = os.getcwd() + '/polls'

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.http import Http404
import json
#from django.http import JsonResponse

# Create your views here.

def registro_view(request):

	#myUser=request.user.get_all_permissions()
	#print myUser

	#ct=ContentType.objects.get_for_model(Perfil)
	#permiso1=Permission.objects.create(codename='buscar_perfil', name='Puede buscar perfil', content_type=ct)

	if request.method == "POST":
		formulario_registro=fusuario(request.POST)
		if formulario_registro.is_valid():
			nuevo_usuario=request.POST['username']
			formulario_registro.save()
			usuario=User.objects.get(username=nuevo_usuario)
			
			tipo = int(request.POST['tipo'])

			if tipo == 0:
				grupo,grupocreado=Group.objects.get_or_create(name='Administrador')
			if tipo == 1:	
				grupo,grupocreado=Group.objects.get_or_create(name='Encargado')
			if tipo == 2:
				grupo,grupocreado=Group.objects.get_or_create(name='Responsable')
			

			if grupocreado != None:
				usuario.groups.add(grupo)
				usuario.save()
			else:
				print('error')


			perfil=Perfil.objects.create(user=usuario)

			#ct=ContentType.objects.get_for_model(Perfil)

			#permiso1, p1=Permission.objects.get_or_create(codename='registrar_usuario', name='Puede registrar al usuario', content_Type=ct)

			#g_administrador.Permissions.add(permiso1)

			#if user==administrador:
			#	user.groups.add(g_administrador)
			#else:

			#		user.groups.add(g_encargado)
			#	else:
			#		user.groups.add(g_responsable)
			return render_to_response('usuario/registro_exitoso.html',context_instance=RequestContext(request))
			#return render_to_response("usuario/activar.html",{'formulario':formulario_registro},context_instance=RequestContext(request))
	else:
		formulario_registro=fusuario()
	return render_to_response("usuario/registro_usuario.html",{'formulario':formulario_registro},context_instance=RequestContext(request))

def login_view(request):
	mensaje = " "
	if request.method=="POST":
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			#usuario=forms.cleaned_data['username']
			usuario=request.POST['username']
			contrasena=request.POST['password']
			acceso=authenticate(username=usuario,password=contrasena)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)

					return HttpResponseRedirect("/user/tipo/")
				else:
					login(request, acceso)
					return HttpResponseRedirect("/user/active/")
			else:
				mensaje="Usuario y/o password incorrectos"
				#return HttpResponse("Error en los datos")
	else:
		formulario=AuthenticationForm()
		#ctx={'formulario':formulario,'mensaje':mensaje}
	return render_to_response("usuario/login.html",{'formulario':formulario,'mensaje':mensaje},context_instance=RequestContext(request))
	#return render_to_response("usuario/login.html",{'formulario':formulario},context_instance=RequestContext(request))

def tipo_view(request):
	usuario = request.user
	grupos = usuario.groups.all()
	for g in grupos:
		if g.name == 'Administrador':
			#return render_to_response("usuario/perfil.html",{'formulario':formulario,'mensaje':mensaje},context_instance=RequestContext(request))
			return HttpResponseRedirect('/user/administrador/')
		if g.name == 'Encargado':	
 			#return render_to_response('usuario/registro_exitoso.html',context_instance=RequestContext(request))
			return HttpResponseRedirect('/user/encargado/')
		if g.name == 'Responsable':
			return HttpResponseRedirect('/user/responsable/')

def administrador_view(request):
	return render_to_response("usuario/administrador.html",{'hora':datetime.datetime.now()},context_instance=RequestContext(request))

def encargado_view(request):
	return render_to_response("encargado/encargado.html",{'hora':datetime.datetime.now()},context_instance=RequestContext(request))


def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

def perfil_view(request):
	return render_to_response("usuario/perfil.html",{'hora':datetime.datetime.now()},context_instance=RequestContext(request))

def user_active_view(request):
	if request.user.is_authenticated():
		usuario=request.user
		if usuario.is_active:
			return HttpResponseRedirect("/user/perfil/")
		else:
			if request.method=="POST":
				u=User.objects.get(username=usuario)
				perfil=Perfil.objects.get(user=u) 
				formulario=fperfil(request.POST,request.FILES,instance=perfil)
				if formulario.is_valid():
					formulario.save()
					u.is_active=True
					u.save()
					return HttpResponseRedirect("/user/perfil/")
			else:
				formulario=fperfil()
			return render_to_response("usuario/activar.html",{'formulario':formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")

def listar_usuario_view(request):
	if request.method == "POST":
		if "id_user" in request.POST:
			try:
				id_usuario = request.POST['id_user']
				p = User.objects.get(pk = id_usuario)
				#msn = {"status":"True","id_user":p.id}
				p.delete()
				return HttpResponseRedirect('/user/listar_usuario/')
				#return HttpResponse(json.dumps(msn),content_type="application/json")
			except:
				#msn = {"status":"False"}
				return HttpResponseRedirect('/user/listar_usuario/')
				#return HttpResponse(json.dumps(msn),content_type="application/json")
	lis=User.objects.order_by("id")
	up=Perfil.objects.order_by("id")
	return render_to_response('usuario/listar_usuario.html',{'lis':lis,'upp':up},context_instance=RequestContext(request))

def editar_usuario_view(request, id_user):
	preg = get_object_or_404(User, id = id_user)
	if request.method == 'POST':
		formulario = fusuario(request.POST, instance = preg)
		if formulario.is_valid():
			formulario.save()
			return render_to_response('usuario/Modificar.html', context_instance = RequestContext(request))
	else:
		formulario = fusuario(instance = preg)
	return render_to_response('usuario/editar_usuario.html',{'formulario':formulario}, context_instance = RequestContext(request))

def registro_personal_view(request):
 	if request.method == "POST":
 		form = PersonalForm(request.POST)
 		if form.is_valid():
 			#u = Personal(
 			#		nombres = form.cleaned_data['nombres'],
 			#		apellido_paterno = form.cleaned_data['apellido_paterno'],
 			#		apellido_materno = form.cleaned_data['apellido_materno'],
 			#		cedula_identidad = form.cleaned_data['cedula_identidad'],
 			#		cargo = form.cleaned_data['cargo'],
 			#		email = form.cleaned_data['email'],
 			#		telefono = form.cleaned_data['telefono'],
 					#fecha = datetime.datetime.now().time(),
 			#		)
 			form.save()
 			return render_to_response('usuario/registro_exitoso.html',context_instance=RequestContext(request))
 	else:
 		form = PersonalForm()
	return render_to_response("usuario/registro_personal.html",{'formulario':form},context_instance=RequestContext(request))

def listar_personal_view(request):
	if request.method == "POST":
		if "personal_id" in request.POST:
			try:
				id_personal = request.POST['personal_id']
				p = Personal.objects.get(pk = id_personal)
				#msn = {"status":"True","personal_id":p.id}
				p.delete()
				return HttpResponseRedirect('/user/listar_personal/')
			except:
				#msn = {"status":"False"}
				return HttpResponseRedirect('/user/listar_personal/')
	lis = Personal.objects.all().order_by('id')
	return render_to_response('usuario/listar_personal.html',{'lis':lis},context_instance=RequestContext(request))

def editar_personal_view(request, personal_id):
	preg = get_object_or_404(Personal, id = personal_id)
	if request.method == 'POST':
		formu = PersonalForm(request.POST, instance = preg)
		if formu.is_valid():
			formu.save()
			return render_to_response('usuario/Modificar.html', context_instance = RequestContext(request))
			#return HttpResponseRedirect('user/registro_personal', personal_id)
	else:
		formu = PersonalForm(instance = preg)
	return render_to_response('usuario/editar_personal.html',{'formu':formu}, context_instance = RequestContext(request))

#def eliminar_personal_view(request, id):
#	perso = Personal.objects.get(id = id
#	id = perso.id
#	perso.delete()
#	return HttpResponseRedirect('/user/editar_personal/'+str(id)+'/')

#def buscar_personal_view(request):
#	if request.method == "POST":
#		form = BuscadorForm(request.POST)
#		if form.is_valid():
#			print 'hola'
#			criterio = request.POST['buscar']
#			lista = Personal.objects.filter(Q(nombres__contains = criterio) or Q(apellido_paterno__constains = criterio))
#			print lista
#			return render_to_response('usuario/resultados_personal.html',{'lista':lista}, RequestContext(request))
#	form = BuscadorForm()
#	return render_to_response('usuario/buscar_personal.html',{'form':form}, context_instance = RequestContext(request))

def buscar_personal_view(request):
    if request.method=="POST":
        texto=request.POST["texto"]
        busqueda=(
            Q(nombres__icontains=texto) |
            Q(apellido_paterno__icontains=texto) |
            Q(apellido_materno__icontains=texto)
        )
        resultados=Personal.objects.filter(busqueda).distinct()
        html="<ul class='ul_lista'>"
        for i in resultados:
            html=html+"<li><a href='/user/listar_personal/"+str(i.id)+"/'>"+i.nombres+"</a></li>"
        html=html+"<ul>"
        return HttpResponse(html)
    else:
        texto=request.GET["texto"]
        busqueda=(
            Q(nombres__icontains=texto) |
            Q(apellido_paterno__icontains=texto) |
            Q(apellido_materno__icontains=texto)
        )
        resultados=Personal.objects.filter(busqueda).distinct()
        html="<ul class='ul_lista'>"
        for i in resultados:
            html=html+"<li><a href='/user/buscar_personal/"+str(i.id)+"/'>"+i.nombres+"</a></li>"
        html=html+"<ul>"
        return HttpResponse(html)
    #formulario=fbuscar()
    #return render_to_response("usuario/listar_personal.html",{'fbuscar':formulario},context_instance=RequestContext(request))

def crear_reporte_personal_view(request):
    personal = Personal.objects.all()
    html = render_to_string("usuario/reporte_personal.html",{'pagesize':'A4','lis':personal},context_instance=RequestContext(request))
    return generar_pdf(html)

def generar_pdf(html):
    resultado = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF:8")),resultado)
    if not pdf.err:
        return HttpResponse(resultado.getvalue(), content_type = 'application/pdf')
    return HttpResponse("Error en generar el pdf")