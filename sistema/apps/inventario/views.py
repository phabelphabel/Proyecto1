from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *

# Create your views here.

def accesorio_view(request):
	if request.method=="POST":
		formulario_ac=factivo(request.POST)
		if formulario_ac.is_valid():
			formulario_ac.save()
			return HttpResponse("Registrado")
	else:
		formulario_ac=faccesorio()
	return render_to_response("inventario/registro_accesorio.html",{'formulario':formulario_ac},context_instance=RequestContext(request))