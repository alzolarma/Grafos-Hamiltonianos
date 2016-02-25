from django.db import models
import matplotlib.pyplot as plt
from collections import deque
import networkx as grafo
import os

# Create your models here.

class Grafo(models.Model):

    nodes = models.CharField(max_length=50)
    edges = models.CharField(max_length=100)
    conjuntoA = models.CharField(max_length=100)
    conjuntoB = models.CharField(max_length=100)
    miniGrado = models.CharField(max_length=5)
    conjuntos_independiente= models.CharField(max_length=5)

    def __init__(self):
		self.bipartito = dict()
		self.nodos= []
		self.edges= []
		self.conjuntos_independiente= [];
		self.miniGrado=0
		self.conjuntoA=[]
		self.conjuntoB=[]

    def getConjuntoA(self):
    	return self.conjuntoA

    def getConjuntoB(self):
    	return self.conjuntoB

    def getminiGrado(self):
    	return self.miniGrado
    
    def _unicode_(self):
		return self.nodes

    def leerNodos(self,nodes):
		archivo = open("nodos_min3_h14.txt") #enlace con el archivo
		nodos = archivo.readlines() #lee linea a linea del archivo y lo almacena en una lista, donde los elementos de la lista son las lineas del archivo
		for x in nodes:
			if x!= ',':	
				G.add_node(x)
			pass
		return G.nodes()

    def leerEdges(self,edges):
		#print edges
		peso=3
		lista = []
		lista = edges.split('-')
		archivo = open("lados_min3_h14.txt") #enlace con el archivo
		edges = archivo.readlines() #lee linea a linea del archivo y lo almacena en una lista, donde los elementos de la lista son las lineas del archivo
		
		for x in lista:
			a = x.rstrip('\n')
			cont = 0
			nodo1 = '0'
			nodo2 = '0'
			for i in x:
				if i!= ',':
					cont = cont + 1
					if cont==1:
						nodo1= i
					if cont ==2:
						cont=0
						nodo2= i
						pass
					pass
				pass
			if(nodo1!='0' and nodo2!='0'):
				G.add_edge(nodo1,nodo2,weight=peso)
				pass
			pass
		return G.edges()

    def minimoGrado(self):
    	for x in G.nodes():
    		var=G.neighbors(x)
    		cont=len(var)
    		if self.miniGrado ==0 and cont>self.miniGrado:
    			self.miniGrado = cont
    			pass
    		if  self.miniGrado!=0 and cont<self.miniGrado:
    			self.miniGrado = cont
    			pass
    		pass
    	return self.miniGrado
  	
    def dibujarGrafo(self):
		elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
		esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]
		pos=grafo.circular_layout(G)
		grafo.draw_networkx_nodes(G,pos,node_size=700,node_color='red')
		grafo.draw_networkx_edges(G,pos,edgelist=elarge,width=3,edge_color='k',style='solid')
		grafo.draw_networkx_edges(G,pos,edgelist=esmall,width=4,alpha=0.5,edge_color='k',style='dashed')
		grafo.draw_networkx_labels(G,pos,font_size=15,font_family='sans-serif',label_color='white')
		plt.axis('off')
		plt.show() # display

    def gradoGrafo(self):
		return G.number_of_nodes()

    def combinacion(self,combinar,lista,listanueva,mitad,conjunto):
		new_comb=[]
		for x in combinar:
		    tamano = len(x)
		    if tamano<mitad:
		        pto=lista.index(x[len(x)-1]) #Hace que el nuevo elemento agregado de "Lista", sea el siguiente en posicion del ultimo caracter del elemento "combinar"
		        for j in range(pto,len(lista)): # para cada elemento de 'lista' desde el elemento "lista" que hace parte del ultimo caracter del elemento de "combinar" hasta el ultimo elemento de'lista'
		            aux=[]
		            if lista[j] not in x and lista[len(lista)-1] not in x:  #Si el elemento de "lista" no esta en el elemento "combinar" y ademas el elemento "lista" no es el ultimo caracter del elemento "combinar"
		                aux.append(x+lista[j])
		                new_comb.append(x+lista[j]) #Agrega a una nueva lista la combinacion
		                conjunto.append(x+','+lista[j])               
		        listanueva=new_comb
		        pass
		return new_comb #Esta nueva lista se utilizara como parametro al llamar de nuevo la funcion...

    def disjunto(self, conjunto,lados):
		conjuntos = conjunto
		conjunto_disjunto = []
		for x in conjunto: #Recorrido de todos los sub-conjuntos de conjunto
			tamano_conjunto = len(x)
			cont = 0
			comb_final=x
			listanueva=[]
			conjunto=[]
			encontrado = False
			while cont<1:    #Un bucle que llama la funcion hasta que esten todas las combinaciones posibles de cada sub-conjunto
				comb_final=self.combinacion(comb_final,x,listanueva,2,conjunto)
				cont = cont +1
				pass
			encontrado = False
			for i in comb_final: #Recorre cada sub-conjunto del conjunto para verificar si es disconjunto
				for k in lados:
					if (i[0]==k[0] and i[1]==k[1]):
						encontrado = True
						k=lados
						break
				pass
			if encontrado==False:
				conjunto_disjunto.append(x)
		return conjunto_disjunto

    def comparar(self,conjunto,lados):
		for x in conjunto: #Recorrido de todos los sub-conjuntos de conjunto
			for l in conjunto:
				encontrado_dis=False
				for j in l:
					if j in x:
						encontrado_dis = True
						pass
					pass
				if encontrado_dis ==False:
					#print chr(27)+"[0;36m"+"Conjuntos Excluyentes",chr(27)+"[0;50m"+""
					#print "Conjunto A: ",l ," Conjunto B: ",x
					cont = 0
					bipartito = True
					#print lados						
					for a in l:
						if G.neighbors(a)==[]:
							bipartito = False
					pass
					for a in x:
						if G.neighbors(a)==[]:
							bipartito = False
					pass
					if bipartito==False:
						print "No bipartito"
						pass
					else:
						print "bipartito"
						self.conjuntoA=l
						self.conjuntoB=x
						print self.conjuntoA
						print self.conjuntoB
						hamiltoniano = self.conjuntosIndependiente(l,x,lados)
						if hamiltoniano==True:
							print "Si"
							return True
							pass
						else:
							print "No"
							return False
				pass
	 	pass

    def conjuntosIndependiente(self,conjuntoA,conjuntoB,edges):
 		minimoGrado=self.miniGrado
 		print minimoGrado
 		cant = 0
		if minimoGrado%2==0:
			cant = minimoGrado
		else:
			cant = minimoGrado + 1
		cant = cant/2
		tamano_l = len(conjuntoA)
		tamano_x = len(conjuntoB)
		cont = 0
		comb_a=conjuntoA
		comb_b=conjuntoB
		lista_a=[] 
		conjunto_a=[]
		lista_b=[] 
		conjunto_b=[]
		encontrado = False
		while cont<cant-1:
			comb_a=self.combinacion(comb_a,conjuntoA,lista_a,cant,conjunto_a)
			comb_b=self.combinacion(comb_b,conjuntoB,lista_b,cant,conjunto_b)
			cont = cont +1												
			pass
		for v in comb_a:
			vecinos = []
			for f in comb_b:
				for i in v:
					var=G.neighbors(i)	
					for k in var:
						if k not in vecinos:
							vecinos.append(k)
							pass
						pass
					pass
				pass
				for i in f:
					var=G.neighbors(i)	
					for k in var:
						if k not in vecinos:
							vecinos.append(k)
							pass
						pass
					pass
				pass
				Hamiltoniano = True
				s = len(vecinos)
				cantv = len (v)
				cantf = len (f)
				N = cantv+cantf
				#print "vecinos " , f
				#print "vecinos" , v
				if s<N+1:
					print "El grafo es de minio grado", minimoGrado
					print "Grafo No Hamiltoniano ya que el vertice ", v , "tiene " ,cantv , "vecinos"
					print "Grafo No Hamiltoniano ya que el vertice ", f , "tiene " ,cantf , "vecinos"
					print "y la suma de ambos", N+1," mas 1 es mayor a : ",s
					Hamiltoniano = False
					return False						
					pass												
			pass
			if Hamiltoniano==True:
				print "El numero de vecinos", s , "es al menos" , N+3
				return True
				pass


class Historial(models.Model):
    ide = models.ForeignKey(Grafo)
    pub_date = models.DateTimeField('date oublished')
    def _unicode_(self):
		return self.pub_date
G=grafo.Graph()
