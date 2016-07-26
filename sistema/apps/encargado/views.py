from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.http import Http404
import json
# Create your views here.

def encargado_view(request):
	return render_to_response("encargado/encargado.html",{'hora':datetime.datetime.now()},context_instance=RequestContext(request))

def carrera_view(request):
	if request.method == "POST":
		formulario_carrera = fcarrera(request.POST)
		if formulario_carrera.is_valid():
			formulario_carrera.save()
			return HttpResponse("Registrado")
	else:
		formulario_carrera = fcarrera()
	return render_to_response("encargado/registro_carreras.html",{"formulario":formulario_carrera},context_instance=RequestContext(request))

def listar_carrera_view(request):
	if request.method == "POST":
		if "carrera_id" in request.POST:
			try:
				id_carrera = request.POST['carrera_id']
				p = Carrera.objects.get(pk = id_carrera)
				p.delete()
				return HttpResponseRedirect('/user/listar_carreras/')
			except:
				return HttpResponseRedirect('/user/listar_carreras/')
	liss = Carrera.objects.all().order_by('id')
	return render_to_response('encargado/listar_carreras.html',{'liss':liss},context_instance=RequestContext(request))

def editar_carreras_view(request, carrera_id):
	preg = get_object_or_404(Carrera, id = carrera_id)
	if request.method == 'POST':
		formu = fcarrera(request.POST, instance = preg)
		if formu.is_valid():
			formu.save()
			return render_to_response('encargado/modificar.html', context_instance = RequestContext(request))
			#return HttpResponseRedirect('user/registro_personal', personal_id)
	else:
		formu = fcarrera(instance = preg)
	return render_to_response('encargado/editar_carreras.html',{'formu':formu}, context_instance = RequestContext(request))

def proveedor_view(request):
	if request.method == "POST":
		formulario_proveedor = fproveedor(request.POST)
		if formulario_proveedor.is_valid():
			formulario_proveedor.save()
			return HttpResponse("Registrado")
	else:
		formulario_proveedor = fproveedor()
	return render_to_response("encargado/registro_proveedor.html",{"formulario":formulario_proveedor},context_instance = RequestContext(request))

def listar_proveedor_view(request):
	if request.method == "POST":
		if 'proveedor_id' in request.POST:
			try:
				id_proveedor = request.POST['proveedor_id']
				p = Proveedor.objects.get(pk = id_proveedor)
				p.delete()
				return HttpResponseRedirect('/user/listar_proveedor/')
			except:
				return HttpResponseRedirect('/user/listar_proveedor/')
	lista = Proveedor.objects.all().order_by('id')
	return render_to_response('encargado/listar_proveedor.html',{'lista':lista}, context_instance = RequestContext(request))

def editar_proveedor_view(request, proveedor_id):
	preg = get_object_or_404(Proveedor, id = proveedor_id)
	if request.method == 'POST':
		formu = fproveedor(request.POST, instance = preg)
		if formu.is_valid():
			formu.save()
			return render_to_response('encargado/modificar.html', context_instance = RequestContext(request))
	else:
		formu = fproveedor(instance = preg)
	return render_to_response('encargado/editar_proveedor.html',{'formu':formu}, context_instance = RequestContext(request))

def grupo_contable_view(request):
	if request.method == 'POST':
		formulario_grupo_contable = fgrupo(request.POST)
		if formulario_grupo_contable.is_valid():
			formulario_grupo_contable.save()
			return HttpResponse('Registrado')
	else:
		formulario_grupo_contable = fgrupo()
	return render_to_response('encargado/registrar_grupo_contable.html',{'formulario':formulario_grupo_contable}, context_instance = RequestContext(request))

def activo_view(request):
	if request.method == 'POST':
		formulario_activo = factivo(request.POST)
		if formulario_activo.is_valid():
			formulario_activo.save()
			return HttpResponse('Registrado')
	else:
		formulario_activo = factivo()
	return render_to_response('encargado/registrar_activo.html',{'formulario':formulario_activo}, context_instance = RequestContext(request))
