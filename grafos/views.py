from django.db.models import  Q
from reportlab.pdfgen import canvas
from django.views.generic import ListView
from grafos.models import Grafo, Historial
from django.contrib.auth.models import User
from django.shortcuts import render_to_response , get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.core.mail import EmailMessage
import matplotlib.pyplot as plt
from collections import deque
import networkx as grafo
import os


def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))	

def explorar(request):
	return render_to_response('index2.html',context_instance=RequestContext(request))	

def sobre(request):
	html = "<html><body>Ejemplo mas </body><html>"
	return HttpResponse(html)
"""
def inicio(request):
	grafo = Grafo.objects.all	return render_to_response('inicio.html',{'grafos':grafo},context_instance=RequestContext(request))
"""
def pruebas(request):
	return render_to_response('grafos.html',context_instance=RequestContext(request))	

def registro(request):
	return render_to_response('registro.html',context_instance=RequestContext(request))	

def search(request):
	grafoB = Grafo()
	G=grafo.Graph()
	nodos=grafoB.leerNodos(request.POST.get('input_nodes'))
	edges=grafoB.leerEdges(request.POST.get('input_edges'))
	minimoGrado = grafoB.minimoGrado()
	print request.POST.get('opc')
	comb_final=nodos
	listanueva=[]
	conjunto=[]
	conjuntoDisjunto=[]
	mitad = grafoB.gradoGrafo()/2
	cont = 0
	print "comb_final"
	print comb_final
	print mitad
	
	while cont<mitad-1:    #Un bucle que llama la funcion hasta que esten todas las combinaciones posibles
		comb_final=grafoB.combinacion(comb_final,nodos,listanueva,mitad,conjunto)
		print comb_final
		cont = cont +1
		comb_final=grafoB.disjunto(comb_final,edges)
	Resultado = grafoB.comparar(comb_final,edges)
	if Resultado:
		hamiltoniano ="Si"
		pass
	else:
		hamiltoniano = "No"
		pass
	print "conjunto disjunto"
	print comb_final

	"""
	_nodes = request.POST.get('input_nodes')
	_edges = request.POST.get('input_edges')
	result= _nodes
	indice = 0
	if _nodes and _edges:
		G=grafo.Graph()
		G.add_node(_nodes)
		results = G.nodes()
		print type (results[0])
	else:
		results=[]
	"""
	#response = HttpResponse(content_type='application/pdf')
	#response['Content-Disposition'] = 'attachment; filename=hello.pdf'
	#p = canvas.Canvas(response)
	#p.drawString(50,760,"Reporte Detallado")
	#p.drawString(50,765,"contenido texto en general que quiero se incluya en el PDF")
	#p.drawString(100,110,hamiltoniano)
	#p.line(50,759,580,760)
	#p.showPage()
	#p.save()
	#return response

	grafoB.dibujarGrafo()
	return render_to_response('grafos.html',{'results': grafoB.leerNodos(request.POST.get('input_nodes')) , 'edges': grafoB.leerEdges(request.POST.get('input_edges')), 'hamiltoniano': hamiltoniano, 'minimoGrado': minimoGrado , 'conjuntoA':grafoB.getConjuntoA() , 'conjuntoB':grafoB.getConjuntoB() },context_instance=RequestContext(request))

def contacto(request):
	if request.method=='POST':
		formulario = GrafoForm(request.POST)
		if formulario.is_valid:
			titulo='mensaje titulo'
			contenido = formulario.cleaned_data['mensaje']+"/n"
			nodes = EmailMessage(titulo,contenido,to=['destinatario@email.com'])
			nodes.send()
			return HttpResponseRedirect('/')
	else:
		formulario = ContactoForm()
	return render_to_response('contactoform.html' , {'formulario':formulario}, context_instance=RequestContext(request))
 
def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
 
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.z("Helvetica", 12)
    p.drawString(5,5,"contenido texto en general que quiero se incluya en el PDF")
    p.drawString(5,5,"contenido texto en general que quiero se incluya en el PDF")
    p.line(50,760,580,760) # Para hacer una linea horizontal
 
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def form(request,id):
	p=get_object_or_404(Grafo,pk=id)
	try:
		selected = p
	except Exception, e:
		raise
	else:
		pass
	finally:
		pass