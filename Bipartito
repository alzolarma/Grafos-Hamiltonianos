#Realizado por: Alzolar Maria
#Fecha:16 de Agosto del 2014
#Verificar si grafo es bipartito balanceado, minimo grado de un grafo 

import matplotlib.pyplot as plt
from collections import deque
import networkx as grafo

class Grafobipartito:
	
	def __init__(self):
		self.bipartito = {}
		self.minimoGrado
	 
	def __str__(self):
		return str(self.bipartito)
	
	def leerNodos(self):
		nodo = '1' 
		while nodo != 0:
			nodo = input('Ingrese los nodos (Presione "0" para terminar):  ')
			G.add_node(nodo)
			print G.nodes()
			pass

	def leerEdges(self):
		edge='1'
		while edge != 0:
			nodo = input('Ingrese Nodo 1: ')
			edge = input('Ingrese Nodo 2: ')
			peso = input('Ingrese  peso: ')
			G.add_edge(nodo,edge,weight=peso)
			print G.edges()
			pass

	def minimoGrado(self):
		gradoMayor=0
		print "Proceso: minimoGrado"
		print G.number_of_nodes()
		print G.number_of_edges()
		print "Nodos:"
		print G.nodes()
		print "Relaciones:"
		print G.edges()
		
		#Incidencias de un nodo en especifico
		cantidad_nodos=G.nodes()
		for x in cantidad_nodos:
			var=G.neighbors(cantidad_nodos[x])
			print "Nodo:"
			print cantidad_nodos[x]
			print "Nodos Incidentes:"
			print var
			print "Cantidad de nodos incidentes:"
			cont=len(var)
			print cont
			if cont>gradoMayor:
				gradoMayor=cont
				pass
			pass
		print "El minimo grado del grafo es:"`
		return gradoMayor

	def dibujarGrafo(self):
		elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
		esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]
		pos=grafo.spring_layout(G) # positions for all nodes
		grafo.draw_networkx_nodes(G,pos,node_size=700)
		grafo.draw_networkx_edges(G,pos,edgelist=elarge,width=6)
		grafo.draw_networkx_edges(G,pos,edgelist=esmall,width=6,alpha=0.5,edge_color='b',style='dashed')
		grafo.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
		plt.axis('off')
		plt.show() # display
	
	def grafoBipartito(self):
		inicio=1
		cantidad_nodos=G.nodes()
		print G.nodes()
		for x in cantidad_nodos:
			var=G.neigh bors(cantidad_nodos[x])
			print var
			pass

		#busquedaProfundidad(inicio)

	def busquedaProfundidad(self,inicio):
		cantidad_nodos=G.nodes()
		print G.nodes()
		#x=1
		#for x in cantidad_nodos:
			#var=G.neigh bors(cantidad_nodos[x])
			#print var
			#pass
		
	def dfsVisitar(tiempo):
		estado[u]=1
		tiempo=tiempo+1
		d[u]=tiempo
		for x in xrange(1,10):
			pass

G=grafo.Graph()
Prueba = Grafobipartito()
Prueba.leerNodos()
Prueba.leerEdges()
print Prueba.minimoGrado()
print Prueba.grafoBipartito()


def imprimir (elemento):
    print elemento
    print "fin" 

Prueba.dibujarGrafo()
