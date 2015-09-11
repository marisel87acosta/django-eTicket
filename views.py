from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import datetime


# Create your views here.
def login(request):
	return render_to_response('indexmari.html',context_instance=RequestContext(request))

def inicio(request):
	return render_to_response('indexSara.html',context_instance=RequestContext(request))

def menu(request):
	return render_to_response('indexMenu.html',context_instance=RequestContext(request))

def multa(request):
	return render_to_response('formularioInfractor.html',context_instance=RequestContext(request))

def formulario(request):
	return render_to_response('formulta.html', context_instance=RequestContext(request))

def mulvehiculo(request):
	return render_to_response('formularioVehi.html', context_instance=RequestContext(request))

def formulIma(request):
	return render_to_response('formularioImagen.html', context_instance=RequestContext(request))

def menu1(request):
	return render_to_response('menu1.html', context_instance=RequestContext(request))
def menu2(request):
	return render_to_response('menu2.html', context_instance=RequestContext(request))
	
def menu3 (request):
	return render_to_response('indexMenuListoInfractor.html', context_instance=RequestContext(request))

def menu4 (request):
	return render_to_response('indexMenuListoInfractorYVehiculo.html', context_instance=RequestContext(request))

def menu5 (request): 
	return render_to_response('formularioLIsto.html', context_instance=RequestContext(request))	
	
