import nodos_doble
from graphviz import Digraph
from subprocess import check_output
class ListasD:

	def __init__(self):
		self.cabeza=None
		self.primer_n=None
		self.tam = 0

	def enlistar(self,informa):
		nodotem = nodos_doble.nodo()
		nodotem.setinfo(informa)
		if (self.cabeza==None):
			nodotem.setsig(nodotem)
			nodotem.setante(nodotem)
			self.tam=0
			self.cabeza=nodotem
			self.primer_n= nodotem
			self.tam=self.tam+1
		else:
			self.cabeza.setante(nodotem)
			self.primer_n.setsig(nodotem)



			nodotem.setsig(self.cabeza)
			nodotem.setante(self.primer_n)
			self.cabeza=nodotem
			self.tam=self.tam+1

	def tam(self):
		tt = str (self.tam)
		return tt

	def mostrar1(self):
		nodomost = self.primer_n
		print ("valor: ",nodomost.getinfo())
		while (nodomost!= self.primer_n.getante()):

			nodomost = nodomost.getsig()
			print ("valor: ",nodomost.getinfo())

	def mostrar1(self):
		nodomost = self.primer_n
		print ("valor: ",nodomost.getinfo())
		while (nodomost!= self.primer_n.getsig()):

			nodomost = nodomost.getante()
			print ("valor: ",nodomost.getinfo())

	def mostrarActivos(self):
		nodomost = self.cabeza
		while (nodomost!= None):
			print ("valor: ",nodomost.getinfo().obtenerdato())
			nodomost = nodomost.getsig()
	#no sirve
	def borrar_indece_ (self,indice):
 		nodomost = self.cabeza
 		cont =0
 		if (indice==self.tam-1):
 			nodoeliminar= nodomost
 			self.cabeza = nodomost.getsig()
 			nodoeliminar.setsig (None)
 		else:
 			j = self.tam- indice -2
 			while (cont!= j):
 			
 				nodomost = nodomost.getsig()
 				cont=cont+1
 			nodoeliminar = nodomost.getsig()
 			print ("",indice," self: ", self.tam-2)
 			nodomost.setsig(nodomost.getsig().getsig())
 			nodoeliminar.setsig=  None
 		self.tam = self.tam-1


	def buscar(self, cadena):
 		a = 0
 		g = False
 		nodomost = self.cabeza

 		while (nodomost!= None):
 			print ("cad",cadena,"getinfo",nodomost.getinfo())
 			if (str(cadena) == str(nodomost.getinfo())):
 				return ("Encontrado en posicion: ",self.tam- a-1)
 				g=True

 			nodomost = nodomost.getsig()
 			a= a+1
 		if (g==False):
 			return ("NO 	Encontrado")

	def buscarp(self, con):
 		a = ""
 		g = False
 		nodomost = self.cabeza
 		t =0;
 		while (nodomost!= None):

 			if(t==con):
 				a=nodomost.getinfo()
 				break
 			t= t+1
 			nodomost = nodomost.getsig()
 		return a
	def lista_comas(self):
		env =""
		tem = self.cabeza
		while (tem!=None):
			if(tem.getsig()!=None):
				env =env+ str(tem.getinfo().obtenerdato())+","
			else:
				env =env+ str(tem.getinfo().obtenerdato())

			tem= tem.getsig()
		return env


	def grafica (self):
		
		dot = Digraph(comment='lista simple')
		dot  #doctest: +ELLIPSIS
		
		nodomost = self.primer_n
		dot.node(str(nodomost.getinfo()))
		dot.edge(str(nodomost.getinfo()), str(nodomost.getsig().getinfo()))
		while (nodomost!= self.primer_n.getante()):

			nodomost = nodomost.getsig()
			dot.node(str(nodomost.getinfo()))
			dot.edge(str(nodomost.getinfo()), str(nodomost.getsig().getinfo()))

		

		print(str(dot.source)) 
		archi=open('datos.txt','w')
		archi.close()
		archi=open('datos.txt','a')
		archi.write(str(dot.source))

		archi.close()

		check_output('"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg datos.txt -o grafo_doble.jpg', shell=True)


