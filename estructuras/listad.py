import nodosd
import listasimple
import os
from random import choice
from subprocess import check_output
from ArbolAvl import ArbolAvl
from activo import activo
class listad1:

	def __init__(self):
		self.cl =None
		self.cdir = None

	def agregar (self,usuario,contra,nombrec,empresa,dep):

		nombre = dep
		tipo = empresa
		nodoinfo = nodosd.nodosd1()
		nodoinfo.setinfo(usuario)
		nodoinfo.setcontra(contra)
		nodoinfo.setcompleto(nombrec)
		if (self.cl ==None and self.cdir ==None):
			print("ENtro a no existe ninguna")
			nodoletra= nodosd.nodosd1()
			nodoletra.setinfo(nombre)
			nododir = nodosd.nodosd1()
			nododir.setinfo(tipo)
			#LETRA CON INFO 
			nodoletra.setsig(nodoinfo)
			nodoinfo.setante(nodoletra)
			#INFO CON DIR
			nodoinfo.setarriba(nododir)
			nododir.setabajo(nodoinfo)
			#agreagamos
			self.cl=nodoletra
			self.cdir=nododir
		else:
			condl =False
			nodotemletra = self.cl
			
			while (nodotemletra!=None):
				if (str(nodotemletra.getinfo())==nombre):
					nodoletraen = nodotemletra

					condl = True
				nodotemletra = nodotemletra.getabajo()
			condl2 =False
			nodotemdir= self.cdir
			while (nodotemdir!=None):
				if (nodotemdir.getinfo()==tipo):
					nodotemdiren = nodotemdir
					condl2 = True
				nodotemdir = nodotemdir.getsig()

			if (condl==False and condl2==False):
					print("cond1 false condl2 false")
					nodoletra= nodosd.nodosd1()
					nodoletra.setinfo(nombre)
					#metodo de la posicion a agregar letra
					#nodoletratemanteriorm(nombre,nodoletra)
					letra = nombre
					nodotem = self.cl
					while (nodotem!=None):
						if ((letra) < (str(nodotem.getinfo()))): 
							print ("menor")
							if (nodotem.getarriba()==None):
								#print ("arriba none")
								nodoletra.setarriba(None)
								nodoletra.setabajo(nodotem)
								nodotem.setarriba(nodoletra)
								if (self.cl == nodotem):
									self.cl = nodoletra
								
							else:
								nodoletra.setarriba(nodotem.getarriba())
								nodoletra.setabajo(nodotem)
								nodotem.getarriba().setabajo(nodoletra)
								nodotem.setarriba(nodoletra)
							break
						elif (nodotem.getabajo()==None):
							print("ultiminodo")
							nodotem.setabajo(nodoletra)
							nodoletra.setarriba(nodotem)
							nodoletra.setabajo(None)
							break
						nodotem = nodotem.getabajo()
				#agregar dir enada
					nododirn= nodosd.nodosd1()
					nododirn.setinfo(tipo)
					#metodo de la posicion a agregar letra
					#nodoletratemanteriorm(nombre,nodoletra)
					letra = nombre
					nodotemd = self.cdir
					while (nodotemd!=None):
						if (tipo < nodotemd.getinfo()):
							print ("menor")
							if (nodotemd.getante()==None):
								#print ("arriba none")
								nododirn.setante(None)
								nododirn.setsig(nodotemd)
								nodotemd.setante(nododirn)
								if (self.cdir == nodotemd):
									self.cdir = nododirn
								
							else:
								nododirn.setante(nodotemd.getante())
								nododirn.setsig(nodotemd)
								nodotemd.getante().setsig(nododirn)
								nodotemd.setante(nododirn)
							break
						elif (nodotemd.getsig()==None):
							print("ultiminodo1")
							nodotemd.setsig(nododirn)
							nododirn.setante(nodotemd)
							nododirn.setsig(None)
							break
						nodotemd = nodotemd.getsig()
					nodoletra.setsig(nodoinfo)
					nodoinfo.setante(nodoletra)
					#INFO CON DIR
					nodoinfo.setarriba(nododirn)
					nododirn.setabajo(nodoinfo)

			if(condl==True and condl2==False):
					print("cond1 true condl2 false")
					#agregar nuevo nodo
				#agregar dir enada
					nododirn= nodosd.nodosd1()
					nododirn.setinfo(tipo)
					#metodo de la posicion a agregar letra
					#nodoletratemanteriorm(nombre,nodoletra)
					letra = nombre 
					nodotemd = self.cdir
					while (nodotemd!=None):
						if (tipo < nodotemd.getinfo()):
							print ("menor")
							if (nodotemd.getante()==None):
								#print ("arriba none")
								nododirn.setante(None)
								nododirn.setsig(nodotemd)
								nodotemd.setante(nododirn)
								if (self.cdir == nodotemd):
									self.cdir = nododirn
								
							else:
								nododirn.setante(nodotemd.getante())
								nododirn.setsig(nodotemd)
								nodotemd.getante().setsig(nododirn)
								nodotemd.setante(nododirn)
							break
						elif (nodotemd.getsig()==None):
							print("ultiminodo")
							nodotemd.setsig(nododirn)
							nododirn.setante(nodotemd)
							nododirn.setsig(None)
							break
						nodotemd = nodotemd.getsig()

					#metodo encontrar la letra ya existente
					letra = nombre
					nodotem = self.cl
					while (nodotem!=None):
						if ((letra) ==(str(nodotem.getinfo()))):
							print ("letra repetida",str(nodotem.getinfo()))
							break
						nodotem = nodotem.getabajo()

					nodoinfo.setarriba(nododirn)
					nododirn.setabajo(nodoinfo)
					#buscar nodo exacto de letra a enlazar
					nodocolumnaa = nodocolumnadir(nodotem,tipo) 
					if (nodocolumnaa.getsig()==None and cabeceral(nodocolumnaa).getinfo()<tipo ):

						nodocolumnaa = nodocolumnadir(nodotem,tipo)
						print (nodoinfo.getinfo(),"columa a enlazar principio",nodocolumnaa.getinfo(),"cabeceral",cabeceral(nodocolumnaa).getinfo())
						
						nodocolumnaa.setsig(nodoinfo)
						nodoinfo.setante(nodocolumnaa)
					else:
						nodocolumnaa = nodocolumnadir(nodotem,tipo)
						print (nodoinfo.getinfo(),"columa a enlazar lado lado ",nodocolumnaa.getinfo())
						nodoinfo.setsig(nodocolumnaa)
						nodoinfo.setante(nodocolumnaa.getante())
						nodocolumnaa.getante().setsig(nodoinfo)
						nodocolumnaa.setante(nodoinfo)
			if (condl==False and condl2==True):
					print("cond1 false condl2 true")
					nodoletra= nodosd.nodosd1()
					nodoletra.setinfo(nombre)
					#metodo de la posicion a agregar letra
					#nodoletratemanteriorm(nombrenodoletra)

					letra = nombre
					nodotem = self.cl



					while (nodotem!=None):
						print ("menor:    -",nodotem.getinfo())
						if ((letra) < (str(nodotem.getinfo()))):
							print ("menor")
							if (nodotem.getarriba()==None):
								#print ("arriba none")
								nodoletra.setarriba(None)
								nodoletra.setabajo(nodotem)
								nodotem.setarriba(nodoletra)
								if (self.cl == nodotem):
									self.cl = nodoletra
								
							else:
								nodoletra.setarriba(nodotem.getarriba())
								nodoletra.setabajo(nodotem)
								nodotem.getarriba().setabajo(nodoletra)
								nodotem.setarriba(nodoletra)
							break
						elif (nodotem.getabajo()==None):
							print("ultiminodo")
							nodotem.setabajo(nodoletra)
							nodoletra.setarriba(nodotem)
							nodoletra.setabajo(None)
							break
						nodotem = nodotem.getabajo()
					nodoletra.setsig(nodoinfo)
					nodoinfo.setante(nodoletra)

					#buscar nodo exacto de letra a enlazar
					nodotem = self.cdir
					while (nodotem!=None):
						if (tipo ==(str(nodotem.getinfo()))):
							print ("tipo repetido",str(nodotem.getinfo()))
							break
						nodotem = nodotem.getsig()

					nodocolumnaa = nodofilaletra(nodotem,nombre)

					if (nodocolumnaa.getabajo()==None and cabeceradir(nodocolumnaa).getinfo()<nombre):
						print (nodoinfo.getinfo(),"columa a enlazar principiofilaletra",nodocolumnaa.getinfo())
						nodoinfo.setabajo(None)
						nodocolumnaa.setabajo(nodoinfo)
						nodoinfo.setarriba(nodocolumnaa)
					else:
						print (nodoinfo.getinfo(),"columa a doble",nodocolumnaa.getinfo())
						nodoinfo.setabajo(nodocolumnaa)
						nodoinfo.setarriba(nodocolumnaa.getarriba())

						nodocolumnaa.getarriba().setabajo(nodoinfo)
						nodocolumnaa.setarriba(nodoinfo)

			if (condl==True and condl2==True):
				print("cond1 true condl2 true")
				nodotem = self.cdir
				nodotemdir = nodosd.nodosd1()
				while (nodotem!=None):
					if (tipo ==(str(nodotem.getinfo()))):
						print ("tipo repetido",str(nodotem.getinfo()))
						nodotemdir = nodotem
						break
					nodotem = nodotem.getsig()

					#nodocolumnaa = nodofilaletra(nodotem,nombre)
				letra = nombre
				nodotem = self.cl
				nodotemletra = nodosd.nodosd1()
				while (nodotem!=None):
					if ((letra) ==(str(nodotem.getinfo()))):
						print ("letra repetida",str(nodotem.getinfo()))
						nodotemletra=nodotem
						break
					nodotem = nodotem.getabajo()

				#print (nodotemletra.getinfo(),"-@-",nodotemdir.getinfo())
				#buscar nodo exacto de letra a enlazar
				#nodocolumnaa = nodocolumnadir(nodotem,tipo)
				ttp = nodotemdir.getabajo()
				condi=False

				while (ttp!=None):
					print ("dentro del while",ttp.getinfo())
					if(encontrarcabletra(ttp).getinfo()==nombre):
						condi=True 
						break

					ttp = ttp.getabajo()

				if (condi==True):
					print ("interno antes del while",ttp.getinfo())
					while (ttp!=None and ttp.getatras()!=None):
			 			print ("interno",ttp.getinfo())
			 			ttp = ttp.getatras()

					ttp.setatras(nodoinfo)
					nodoinfo.setadelante(ttp)
					nodoinfo.setatras(None)
					print(nodoinfo.getadelante().getinfo())



				#
				else:
					temp =nodotemdir.getabajo()
					while (temp!=None):
						print(nodotemdir.getinfo(),"--ENTROE A repetida ALGO4 afuera--",temp.getinfo())
						try:
							print(nodotemdir.getinfo(),"--ENTROE A repetida ALGO4 afuera--",temp.getinfo())
							print("comparar",nombre)
							if (nombre< encontrarcabletra(temp).getinfo()):
								print("ENTROE A repetida ALGO4")
								
								nodoinfo.setabajo(temp)
								nodoinfo.setarriba(temp.getarriba())

								temp.getarriba().setabajo(nodoinfo)

								temp.setarriba(nodoinfo)

								print("ENTROE A repetida ALGO5")
								################
								nodotem = self.cl
								while (nodotem!=None):
									if ((letra) ==(str(nodotem.getinfo()))):
										print ("letra repetida",str(nodotem.getinfo()))
										break
									nodotem = nodotem.getabajo()

								#buscar nodo exacto de letra a enlazar
								nodocolumnaa = nodocolumnadir(nodotem,tipo) 
								if (nodocolumnaa.getsig()==None and cabeceral(nodocolumnaa).getinfo()< tipo ):

									nodocolumnaa = nodocolumnadir(nodotem,tipo)
									print (nodoinfo.getinfo(),"columa a enlazar principio",nodocolumnaa.getinfo())
									nodoinfo.setsig(None)
									nodocolumnaa.setsig(nodoinfo)
									nodoinfo.setante(nodocolumnaa)
								else:
									nodocolumnaa = nodocolumnadir(nodotem,tipo)
									print (nodoinfo.getinfo(),"columa a enlazar lado lado ",nodocolumnaa.getinfo())
									nodoinfo.setsig(nodocolumnaa)
									nodoinfo.setante(nodocolumnaa.getante())
									nodocolumnaa.getante().setsig(nodoinfo)
									nodocolumnaa.setante(nodoinfo)




								################
								print ("lelgo break")
								break
							elif (nombre== temp.getinfo()):
								print ("letra igual algo true true break")
								break
							else:
								print ("nada")
								
								

						except Exception:
							print (Exception)
							
						print ("interno",temp.getinfo())
						temp= temp.getabajo()

					if (temp == None):
						print ("entro a none trur true",nodotemdir.getinfo())
						tempp =nodotemdir.getabajo()
						while (tempp!=None):
							if (tempp.getabajo()==None):
					
								nodoinfo.setarriba(tempp)
								tempp.setabajo(nodoinfo)
																################
								nodotem = self.cl
								while (nodotem!=None):
									if ((letra) ==(str(nodotem.getinfo()))):
										print ("letra repetida",str(nodotem.getinfo()))
										break
									nodotem = nodotem.getabajo()

								#buscar nodo exacto de letra a enlazar
								nodocolumnaa = nodocolumnadir(nodotem,tipo) 
								if (nodocolumnaa.getsig()==None and cabeceral(nodocolumnaa).getinfo()< tipo ):

									nodocolumnaa = nodocolumnadir(nodotem,tipo)
									print (nodoinfo.getinfo(),"columa a enlazar principio",nodocolumnaa.getinfo())
									nodoinfo.setsig(None)
									nodocolumnaa.setsig(nodoinfo)
									nodoinfo.setante(nodocolumnaa)
								else:
									nodocolumnaa = nodocolumnadir(nodotem,tipo)
									print (nodoinfo.getinfo(),"columa a enlazar lado lado ",nodocolumnaa.getinfo())
									nodoinfo.setsig(nodocolumnaa)
									nodoinfo.setante(nodocolumnaa.getante())
									nodocolumnaa.getante().setsig(nodoinfo)
									nodocolumnaa.setante(nodoinfo)




								################
								break

							tempp = tempp.getabajo() 


					
	def comprobar_inicio (self, user,contra,emp,dep):
		nodotem= self.cl
		nodotemdep = self.cdir

		while (nodotem!=None):
			if ((dep) ==(str(nodotem.getinfo()))):
				break
			nodotem = nodotem.getabajo()

		nododotemub = nodosd.nodosd1()
		while (nodotem!=None):
			if (cabeceral(nodotem)!=None): 
				if (emp == cabeceral(nodotem).getinfo()):
					nododd = nodotem
					if (user ==(str(nodotem.getinfo())) and emp == cabeceral(nodotem).getinfo()):
						nododotemub =nodotem
						print("comparar contrasena1",nododotemub.getcontra(),"contra",contra)
						if(str(nododotemub.getcontra())==str(contra)):
							print("comparar contrasena1",nododotemub.getcontra(),"contra",contra,"verdader")
							return True
							break
						else:
							return False
							break
					while (nododd!=None):


						if (user == nododd.getinfo()):
							nododotemub =nododd
							print("comparar contrasena2",nododotemub.getinfo())
							if(str(nododotemub.getcontra())==str(contra)):
								return True
								break
							else:
								return False
								break
						nododd = nododd.getatras()

			nodotem = nodotem.getsig()
		if (nodotem==None):
			print("No encontrado")




	def buscar_user(self,user,emp,dep):
		nodotem= self.cl
		nodotemdep = self.cdir

		while (nodotem!=None):
			if ((dep) ==(str(nodotem.getinfo()))):
				break
			nodotem = nodotem.getabajo()

		nododotemub = nodosd.nodosd1()
		while (nodotem!=None):
			if (cabeceral(nodotem)!=None):
				print ("nodo del cabeceral",nodotem.getinfo(),"cabeceral",cabeceral(nodotem).getinfo())
				print ("nodo del cabeceral2",user,"cabeceral2",emp)
				if (emp == cabeceral(nodotem).getinfo()):
					nododd = nodotem
					if (user ==(str(nodotem.getinfo())) and emp == cabeceral(nodotem).getinfo()):
						nododotemub =nodotem
						print ("entrp")
						print("Encontrado")
						print("usuario",nododotemub.getinfo())
						print("contra",nododotemub.getcontra())
						print("nombre completo",nododotemub.getinfo())
						print("avl",nododotemub.getavl())
						break
					while (nododd!=None):


						if (user == nododd.getinfo()):
							nododotemub =nododd
							print ("entrp")
							print("Encontrado")
							print("usuario",nododotemub.getinfo())
							print("contra",nododotemub.getcontra())
							print("nombre completo",nododotemub.getinfo())
							print("avl",nododotemub.getavl())
							break
						nododd = nododd.getatras()

			nodotem = nodotem.getsig()
		if (nodotem==None):
			print("No encontrado")


	def buscar_user_agregar_activo(self,user,emp,dep,activo,desc):
		nodotem= self.cl
		nodotemdep = self.cdir

		while (nodotem!=None):
			if ((dep) ==(str(nodotem.getinfo()))):
				break
			nodotem = nodotem.getabajo()

		nododotemub = nodosd.nodosd1()
		while (nodotem!=None):
			if (cabeceral(nodotem)!=None):
				print ("nodo del cabeceral",nodotem.getinfo(),"cabeceral",cabeceral(nodotem).getinfo())
				print ("nodo del cabeceral2",user,"cabeceral2",emp)
				if (emp == cabeceral(nodotem).getinfo()):
					nododd = nodotem
					if (user ==(str(nodotem.getinfo())) and emp == cabeceral(nodotem).getinfo()):
						nododotemub =nodotem
						numram = generar_random()
						if(nododotemub.getavl()==None):
							avl= ArbolAvl()
							avl.agregar(activo,desc, numram)
							nododotemub.setavl(avl)
							break
						else:
							avltemp = nododotemub.getavl()
							avltemp.agregar(activo,desc, numram)
							break
					while (nododd!=None):

						if (user == nododd.getinfo()):
							nododotemub =nododd
							numram = generar_random()
							if(nododotemub.getavl()==None):
								avl= ArbolAvl()
								avl.agregar(activo,desc, numram)
								nododotemub.setavl(avl)
								break
							else:
								avltemp = nododotemub.getavl()
								avltemp.agregar(activo,desc, numram)
								break
						nododd = nododd.getatras()

			nodotem = nodotem.getsig()

	def avl_pos(self,user,emp,dep):
		nodotem= self.cl
		nodotemdep = self.cdir
		mandat=""
		while (nodotem!=None):
			if ((dep) ==(str(nodotem.getinfo()))):
				break
			nodotem = nodotem.getabajo()

		nododotemub = nodosd.nodosd1()
		while (nodotem!=None):
			if (cabeceral(nodotem)!=None):
				if (emp == cabeceral(nodotem).getinfo()):
					nododd = nodotem
					if (user ==(str(nodotem.getinfo())) and emp == cabeceral(nodotem).getinfo()):
						nododotemub =nodotem
						if(nododotemub.getavl()==None):
							break
						else:
							avltemp = nododotemub.getavl()
							mandat=avltemp.recorrer()
							break
					while (nododd!=None):

						if (user == nododd.getinfo()):
							nododotemub =nododd
							numram = generar_random()
							if(nododotemub.getavl()==None):
								break
							else:
								avltemp = nododotemub.getavl()
								mandat=avltemp.recorrer()
								break
						nododd = nododd.getatras()

			nodotem = nodotem.getsig()

		return mandat






	def buscar_user_modificar_activo(self,user,emp,dep,numr,activo,desc):

		nodotem= self.cl
		nodotemdep = self.cdir

		while (nodotem!=None):
			if ((dep) ==(str(nodotem.getinfo()))):
				break
			nodotem = nodotem.getabajo()

		nododotemub = nodosd.nodosd1()
		while (nodotem!=None):
			if (cabeceral(nodotem)!=None):
				if (emp == cabeceral(nodotem).getinfo()):
					nododd = nodotem
					if (user ==(str(nodotem.getinfo())) and emp == cabeceral(nodotem).getinfo()):
						nododotemub =nodotem
						if(nododotemub.getavl()==None):
							break
						else:
							avltemp = nododotemub.getavl()
							avltemp.reemplazo(activo,desc, numr)
							break
					while (nododd!=None):

						if (user == nododd.getinfo()):
							nododotemub =nododd
							numram = generar_random()
							if(nododotemub.getavl()==None):
								break
							else:
								avltemp = nododotemub.getavl()
								avltemp.reemplazo(activo,desc, numr)
								break
						nododd = nododd.getatras()

			nodotem = nodotem.getsig()


	def todos_activos(self):
		todos=""
		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh
				avlrr =nodotemh.getavl()
				if(avlrr!=None):
					
					k = avlrr.listarActivos()
					todos =todos+ k.lista_comas()


				

				while( nodoadentro!=None ):		
					#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					#print ("cabecera dentro",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh

				print ("cabecera afurea",nodoadentro.getinfo())

				while( nodoadentro!=None ):	
					if(nodoadentro.getatras()!=None):	
						avlrr =nodoadentro.getavl()
						if(avlrr!=None):
							if(todos==""):
								k = avlrr.listarActivos()
								todos =todos+ k.lista_comas()
							else:
								k = avlrr.listarActivos()
								todos =todos+ ","+k.lista_comas()


					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		return todos

	def todos_activos2(self):
		todos=""
		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh
				avlrr =nodotemh.getavl()
				if(avlrr!=None):
					
					k = avlrr.ob
					todos =todos+ k


				

				while( nodoadentro!=None ):		
					#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					#print ("cabecera dentro",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh

				print ("cabecera afurea",nodoadentro.getinfo())

				while( nodoadentro!=None ):	
					if(nodoadentro.getatras()!=None):	
						avlrr =nodoadentro.getavl()
						if(avlrr!=None):
							if(todos==""):
								k = avlrr.listarActivos()
								todos =todos+ k.lista_comas()
							else:
								k = avlrr.listarActivos()
								todos =todos+ ","+k.lista_comas()


					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		return todos

	def ver_por_user(self,user,emp,dep):
		todos=""
		nodotem= self.cl
		nodotemdep = self.cdir

		while (nodotem!=None):
			if ((dep) ==(str(nodotem.getinfo()))):
				break
			nodotem = nodotem.getabajo()

		nododotemub = nodosd.nodosd1()
		while (nodotem!=None):
			if (cabeceral(nodotem)!=None):
				print ("nodo del cabeceral",nodotem.getinfo(),"cabeceral",cabeceral(nodotem).getinfo())
				print ("nodo del cabeceral2",user,"cabeceral2",emp)
				if (emp == cabeceral(nodotem).getinfo()):
					nododd = nodotem
					if (user ==(str(nodotem.getinfo())) and emp == cabeceral(nodotem).getinfo()):
						nododotemub =nodotem
						if(nododotemub.getavl()==None):
							break
						else:
							avltemp = nododotemub.getavl()
							k = avltemp.obter_activos()
							todos =todos+ k
							break
					while (nododd!=None):

						if (user == nododd.getinfo()):
							nododotemub =nododd
							numram = generar_random()
							if(nododotemub.getavl()==None):
								break
							else:
								avltemp = nododotemub.getavl()
								if(todos==""):
									k = avltemp.obter_activos()
									todos =todos+ k
								else:
									k = avltemp.obter_activos()
									todos =todos+k
									break
						nododd = nododd.getatras()

			nodotem = nodotem.getsig()

		return todos


	def ver_por_user_todos(self):
		todos=""
		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh
				avlrr =nodotemh.getavl()
				if(avlrr!=None):
					
					k = avlrr.obter_activos()
					todos =todos+""+nodotemh.getinfo()+"?"+ k



				

				while( nodoadentro!=None ):		
					#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					#print ("cabecera dentro",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh

				print ("cabecera afurea",nodoadentro.getinfo())

				while( nodoadentro!=None ):	
					if(nodoadentro.getatras()!=None):	
						avlrr =nodoadentro.getavl()
						
						if(avlrr!=None):
							k = avlrr.obter_activos()
							todos =todos+""+nodotemh.getinfo()+"?"+ k
						
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		return todos

	def ver_por_user2(self,user,emp,dep):
		todos=""
		otros=""
		nodotem= self.cl
		nodotemdep = self.cdir

		while (nodotem!=None):
			if ((dep) ==(str(nodotem.getinfo()))):
				break
			nodotem = nodotem.getabajo()

		nododotemub = nodosd.nodosd1()
		while (nodotem!=None):
			if (cabeceral(nodotem)!=None):
				print ("nodo del cabeceral",nodotem.getinfo(),"cabeceral",cabeceral(nodotem).getinfo())
				print ("nodo del cabeceral2",user,"cabeceral2",emp)
				if (emp == cabeceral(nodotem).getinfo()):
					nododd = nodotem
					if (user ==(str(nodotem.getinfo())) and emp == cabeceral(nodotem).getinfo()):
						nododotemub =nodotem
						if(nododotemub.getavl()==None):
							break
						else:
							avltemp = nododotemub.getavl()
							return avltemp.obter_activos()
							k = avltemp.listarActivos()
							todos =todos+ k.lista_comas()
							break
					while (nododd!=None):

						if (user == nododd.getinfo()):
							nododotemub =nododd
							numram = generar_random()
							if(nododotemub.getavl()==None):
								break
							else:
								avltemp = nododotemub.getavl()
								if(todos==""):
									k = avltemp.listarActivos()
									todos =todos+ k.lista_comas()
								else:
									k = avltemp.listarActivos()
									todos =todos+ ","+k.lista_comas()
									break
						nododd = nododd.getatras()

			nodotem = nodotem.getsig()

		return otros

	def eliminar_activo(self,user,emp,dep,numr,activo,desc):
		nodotem= self.cl
		nodotemdep = self.cdir

		while (nodotem!=None):
			if ((dep) ==(str(nodotem.getinfo()))):
				break
			nodotem = nodotem.getabajo()

		nododotemub = nodosd.nodosd1()
		while (nodotem!=None):
			if (cabeceral(nodotem)!=None):
				print ("nodo del cabeceral",nodotem.getinfo(),"cabeceral",cabeceral(nodotem).getinfo())
				print ("nodo del cabeceral2",user,"cabeceral2",emp)
				if (emp == cabeceral(nodotem).getinfo()):
					nododd = nodotem
					if (user ==(str(nodotem.getinfo())) and emp == cabeceral(nodotem).getinfo()):
						nododotemub =nodotem
						if(nododotemub.getavl()==None):
							break
						else:
							avltemp = nododotemub.getavl()
							avltemp.borrar(activo,desc, numr)
							break
					while (nododd!=None):

						if (user == nododd.getinfo()):
							nododotemub =nododd
							numram = generar_random()
							if(nododotemub.getavl()==None):
								break
							else:
								avltemp = nododotemub.getavl()
								avltemp.borrar(activo,desc, numr)
								break
						nododd = nododd.getatras()

			nodotem = nodotem.getsig()
		


	def obtener_dep(self):
		nodoen = self.cl
		mandar =""
		while (nodoen!=None):
			if (nodoen.getabajo()!=None):
				mandar = mandar+str(nodoen.getinfo())+","
			else:
				mandar = mandar+str(nodoen.getinfo())
			nodoen = nodoen.getabajo()
		return mandar

	def obtener_emp(self):	
		nodoen = self.cdir
		mandar =""
		while (nodoen!=None):
			if (nodoen.getsig()!=None):
				mandar = mandar+str(nodoen.getinfo())+","
			else:
				mandar = mandar+str(nodoen.getinfo())
			nodoen = nodoen.getsig()
		return mandar


	def obtener_user(self):	
		todos=""
		f =0;
		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh
				avlrr =nodotemh.getavl()
				if (f ==0):
					nodotemh=nodotemh.getsig()
					f=f+1
				
				if(nodotemh.getsig()!=None):
					todos =todos+ nodotemh.getinfo()+","

				else:
					todos =todos+ nodotemh.getinfo()+","




				

				while( nodoadentro!=None ):		
					#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					#print ("cabecera dentro",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		nodotem = self.cl

		f =0
		while (nodotem!=None):
			nodotemh = nodotem

			while (nodotemh!=None ):
				nodoadentro = nodotemh

				print ("cabecera afurea",nodoadentro.getinfo())
				f=0
				while( nodoadentro!=None ):

					if(nodoadentro.getatras()!=None):	
						avlrr =nodoadentro.getavl()
						if(todos==""):
							todos =todos+ nodoadentro.getinfo()
						else:
							todos =todos+ ","+nodoadentro.getinfo()


					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		return todos









				




					
	def bletral (self, parametro):
		nodotem = self.cl
		listenv = listasimple.ListaS()
		fc =0
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None):
				nodoadentro = nodotemh
				while(nodoadentro!=None):
					if(parametro==nodoadentro.getinfo()):

						print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
						fc=fc+1
						listenv.enlistar(nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()
		#listenv.mostrar()
		#gk =str(listenv.tam())
		return str(fc)
	def bletral1 (self, parametro,con):
		nodotem = self.cl
		listenv = listasimple.ListaS()
		fc =0
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None):
				nodoadentro = nodotemh
				while(nodoadentro!=None):
					if(parametro==nodoadentro.getinfo()):

						#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
						fc=fc+1
						listenv.enlistar(nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()
		gk =str(listenv.buscarp(con))
		return gk

###
	def bletraldir (self, parametro):
		nodotem = self.cdir
		listenv = listasimple.ListaS()
		fc =0
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None):
				nodoadentro = nodotemh
				while(nodoadentro!=None):
					if(parametro==nodotem.getinfo()):
						#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
						fc=fc+1
						listenv.enlistar(nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getabajo()
			nodotem = nodotem.getsig()	
		#listenv.mostrar()
		#gk =str(listenv.tam())
		return str(fc)
	def bletraldir1 (self, parametro,con):
		nodotem = self.cdir
		listenv = listasimple.ListaS()
		fc =0
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None):
				nodoadentro = nodotemh
				while(nodoadentro!=None):
					if(parametro==nodotem.getinfo()):
						#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
						fc=fc+1
						listenv.enlistar(nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getabajo()
			nodotem = nodotem.getsig()
		gk =str(listenv.buscarp(con))
		return gk



##3
	def mostrarl(self):
		nodotem = self.cl
		while (nodotem!=None):
			print (nodotem.getinfo())
			#print (nodotem.getinfo(),"----",nodotem.getsig().getinfo())
			nodotem= nodotem.getabajo()

	def mostrardir(self):
		nodotem = self.cdir
		while (nodotem!=None):
			print (nodotem.getinfo())
			nodotem= nodotem.getsig()
	def mostrartvarl(self):
		nodotem = self.cl
		while (nodotem!=None):
			dm = nodotem
			dm = dm.getsig()
			while (dm!=None):
				print (nodotem.getinfo(),"...",dm.getinfo())
				dm = dm.getsig()
				
			nodotem = nodotem.getabajo()
	def mostrartvarl2(self):
		nodotem = self.cdir
		while (nodotem!=None):
			dm = nodotem
			dm = dm.getabajo()
			while (dm!=None):
				print (nodotem.getinfo(),"...",dm.getinfo())
				dm = dm.getabajo()
				
			nodotem= nodotem.getsig()

	def mostrartodoh(self):
		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None):
				nodoadentro = nodotemh
				while(nodoadentro!=None):
					print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()
				

	def mostrartodov(self):
		nodotem = self.cdir
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None):
				nodoadentro = nodotemh
				while(nodoadentro!=None):
					print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getabajo()
			nodotem = nodotem.getsig()	
	def graficar(self):
  #doctest: +ELLIPSIS
		archi=open('datosm.txt','w')
		archi.close()
		archi=open('datosm.txt','a')
		nodoteml = self.cl
		nodotemd =self.cdir
		archi.write("digraph algo{\nnode [shape=box] \n ")

		while (nodoteml!=None):

			nodoteml=nodoteml.getabajo()
		
		archi.write("{\n ")
		archi.write("rank=same\n ")
		archi.write("INICIO\n ")
		while (nodotemd!=None):
			archi.write("\""+str(nodotemd.getinfo())+"\"")
			archi.write("[rankdir=LR]\n ")
			nodotemd=nodotemd.getsig()
		archi.write("}\n ")
		archi.write(str("INICIO"))
		archi.write(str("->"))
		archi.write("\""+str(self.cl.getinfo())+"\"")
		archi.write("\n")
		archi.write("INICIO")
		archi.write(str("->"))
		archi.write("\""+self.cdir.getinfo()+"\"")
		archi.write("\n")

		
		nodoteml = self.cl
		nodotemd =self.cdir
		while (nodoteml!=None and nodoteml.getabajo()!=None):
			archi.write("\""+str(nodoteml.getinfo())+"\"")
			archi.write(str("->"))
			archi.write("\""+str(nodoteml.getabajo().getinfo())+"\"")
			archi.write("\n")
			archi.write("\""+str(nodoteml.getabajo().getinfo())+"\"")
			archi.write(str("->"))
			archi.write("\""+str(nodoteml.getinfo())+"\"")
			archi.write("\n")
			nodoteml=nodoteml.getabajo()
		
		while (nodotemd!=None and nodotemd.getsig()!=None):
			archi.write("\""+str(nodotemd.getinfo())+"\"")
			archi.write(str("->"))
			archi.write("\""+str(str(nodotemd.getsig().getinfo()))+"\"")
			archi.write("\n")
			archi.write("\""+str(nodotemd.getsig().getinfo())+"\"")
			archi.write(str("->"))
			archi.write("\""+str(nodotemd.getinfo())+"\"")
			archi.write("\n")

			nodotemd=nodotemd.getsig()
			#recien agregado
		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			archi.write("{\n ")
			archi.write("rank=same\n ")
			while (nodotemh!=None ):
				nodoadentro = nodotemh
				print ("cabecera afurea--------",str(nodotemh.getinfo()),"")
				archi.write("\""+str(nodotemh.getinfo())+"\"\n ")
					

			
				nodotemh = nodotemh.getsig()
			archi.write("}\n ")
			nodotem = nodotem.getabajo()


			#ffffff

		#agregar nodos superiosres
		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh
				print ("cabecera afurea--------",str(nodotemh.getinfo()),"")
				try:
					archi.write("\""+str(nodotemh.getante().getinfo())+"\"")
					archi.write(str("->"))
					archi.write("\""+str(nodotemh.getinfo())+"\"")
					archi.write("[constraint=false]")
					archi.write("\n")
					archi.write("\""+str(nodotemh.getinfo())+"\"")
					archi.write(str("->"))
					archi.write("\""+str(nodotemh.getante().getinfo())+"\"")
					archi.write("[constraint=false]")
					archi.write("\n")



					
				except Exception:
					print("error grafo ageegar letra")
					

				

				while( nodoadentro!=None ):		
					#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					#print ("cabecera dentro",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh

				print ("cabecera afurea",nodoadentro.getinfo())

				while( nodoadentro!=None ):	
					if(nodoadentro.getatras()!=None):	
						print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
						print ("cabecera dentro",nodoadentro.getinfo())
					try :
						archi.write("\""+str(nodoadentro.getadelante().getinfo())+"\"")
						archi.write(str("->"))
						archi.write("\""+str(nodoadentro.getinfo())+"\"")
						archi.write("\n")
						archi.write("\n")
						archi.write("\""+str(nodoadentro.getinfo())+"\"")
						archi.write(str("->"))
						archi.write("\""+str(nodoadentro.getadelante().getinfo())+"\"")
						archi.write("\n")


					except :
						pass
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		#agregar columnas
		nodotem = self.cdir
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				if (nodotemh.getarriba()!=None):
					archi.write("\n")
					archi.write("\""+str(nodotemh.getarriba().getinfo())+"\"")
					archi.write(str("->"))
					archi.write("\""+str(nodotemh.getinfo())+"\"")
					archi.write("\n")
					archi.write("\""+str(nodotemh.getinfo())+"\"")
					archi.write(str("->"))
					archi.write("\""+str(nodotemh.getarriba().getinfo())+"\"")
					archi.write("\n")

				nodoadentro = nodotemh
				while(nodoadentro!=None and nodoadentro.getatras()!=None):
					#dot.edge(str(nodoadentro.getinfo()), str(nodoadentro.getatras().getinfo()))
					#dot.edge(str(nodoadentro.getatras().getinfo()), str(nodoadentro.getinfo()))
					#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getabajo()
			nodotem = nodotem.getsig()	


		archi.write("\n ")
		archi.write("}")
		archi.close()
		#cambiar la direccion del archivo txt creado y a del dot
		check_output('"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg C:\\Users\\HP\\datosm.txt -o C:\\Users\\HP\\Documents\\1.1\\grafom1.jpg', shell=True)


	def graficarcompleto(self):
  #doctest: +ELLIPSIS
		archi=open('datosm.txt','w')
		archi.close()
		archi=open('datosm.txt','a')
		nodoteml = self.cl
		nodotemd =self.cdir
		archi.write("digraph algo{\nnode [shape=box] \n ")

		while (nodoteml!=None):

			nodoteml=nodoteml.getabajo()
		
		archi.write("{\n ")
		archi.write("rank=same\n ")
		archi.write("INICIO\n ")
		while (nodotemd!=None):
			archi.write("\""+str(nodotemd.getinfo())+"\"")
			archi.write("[rankdir=LR]\n ")
			nodotemd=nodotemd.getsig()
		archi.write("}\n ")
		archi.write(str("INICIO"))
		archi.write(str("->"))
		archi.write("\""+str(self.cl.getinfo())+"\"")
		archi.write("\n")
		archi.write("INICIO")
		archi.write(str("->"))
		archi.write("\""+self.cdir.getinfo()+"\"")
		archi.write("\n")

		
		nodoteml = self.cl
		nodotemd =self.cdir
		while (nodoteml!=None and nodoteml.getabajo()!=None):
			archi.write("\""+str(nodoteml.getinfo())+"\"")
			archi.write(str("->"))
			archi.write("\""+str(nodoteml.getabajo().getinfo())+"\"")
			archi.write("\n")
			archi.write("\""+str(nodoteml.getabajo().getinfo())+"\"")
			archi.write(str("->"))
			archi.write("\""+str(nodoteml.getinfo())+"\"")
			archi.write("\n")
			nodoteml=nodoteml.getabajo()
		
		while (nodotemd!=None and nodotemd.getsig()!=None):
			archi.write("\""+str(nodotemd.getinfo())+"\"")
			archi.write(str("->"))
			archi.write("\""+str(str(nodotemd.getsig().getinfo()))+"\"")
			archi.write("\n")
			archi.write("\""+str(nodotemd.getsig().getinfo())+"\"")
			archi.write(str("->"))
			archi.write("\""+str(nodotemd.getinfo())+"\"")
			archi.write("\n")

			nodotemd=nodotemd.getsig()
			#recien agregado
		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			archi.write("{\n ")
			archi.write("rank=same\n ")
			while (nodotemh!=None ):
				nodoadentro = nodotemh
				print ("cabecera afurea--------",str(nodotemh.getinfo()),"")
				archi.write("\""+str(nodotemh.getinfo())+"\"\n ")
					

			
				nodotemh = nodotemh.getsig()
			archi.write("}\n ")
			nodotem = nodotem.getabajo()


			#ffffff

		#agregar nodos superiosres
		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh
				print ("cabecera afurea--------",str(nodotemh.getinfo()),"")
				try:
					archi.write("\""+str(nodotemh.getante().getinfo())+"\"")
					archi.write(str("->"))
					archi.write("\""+str(nodotemh.getinfo())+"\"")
					archi.write("[constraint=false]")
					archi.write("\n")
					archi.write("\""+str(nodotemh.getinfo())+"\"")
					archi.write(str("->"))
					archi.write("\""+str(nodotemh.getante().getinfo())+"\"")
					archi.write("[constraint=false]")
					archi.write("\n")
					avlr = nodotemh.getavl()
					if (avlr!=None):
						
						parametro=avlr.recorrer()
						archi.write(parametro)
						
						archi.write("\""+str(nodotemh.getinfo())+"\"")
						archi.write(str("->"))
						archi.write("\""+str("t"+avlr.obtenerRaiz())+"\"")
						archi.write("\n")


					
				except Exception:
					print("error grafo ageegar letra")
					

				

				while( nodoadentro!=None ):		
					#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					#print ("cabecera dentro",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh

				print ("cabecera afurea",nodoadentro.getinfo())

				while( nodoadentro!=None ):	
					if(nodoadentro.getatras()!=None):	
						print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
						print ("cabecera dentro",nodoadentro.getinfo())
					try :
						archi.write("\""+str(nodoadentro.getadelante().getinfo())+"\"")
						archi.write(str("->"))
						archi.write("\""+str(nodoadentro.getinfo())+"\"")
						archi.write("\n")
						archi.write("\n")
						archi.write("\""+str(nodoadentro.getinfo())+"\"")
						archi.write(str("->"))
						archi.write("\""+str(nodoadentro.getadelante().getinfo())+"\"")
						archi.write("\n")
						
						avlr = nodoadentro.getavl()
						if(avlr!=None):
							
							parametro=avlr.recorrer()
							archi.write(parametro)
							
							archi.write("\""+str(nodoadentro.getinfo())+"\"")
							archi.write(str("->"))
							archi.write("\""+str("t"+avlr.obtenerRaiz())+"\"")
							archi.write("\n")


					except :
						pass
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		#agregar columnas
		nodotem = self.cdir
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				if (nodotemh.getarriba()!=None):
					archi.write("\n")
					archi.write("\""+str(nodotemh.getarriba().getinfo())+"\"")
					archi.write(str("->"))
					archi.write("\""+str(nodotemh.getinfo())+"\"")
					archi.write("\n")
					archi.write("\""+str(nodotemh.getinfo())+"\"")
					archi.write(str("->"))
					archi.write("\""+str(nodotemh.getarriba().getinfo())+"\"")
					archi.write("\n")

				nodoadentro = nodotemh
				while(nodoadentro!=None and nodoadentro.getatras()!=None):
					#dot.edge(str(nodoadentro.getinfo()), str(nodoadentro.getatras().getinfo()))
					#dot.edge(str(nodoadentro.getatras().getinfo()), str(nodoadentro.getinfo()))
					#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getabajo()
			nodotem = nodotem.getsig()	


		archi.write("\n ")
		archi.write("}")
		
		archi.close()
		archivo = open("datosm.txt", "r") 
		contenido = archivo.read()
		mng  = str(contenido)
		#cambiar la direccion del archivo txt creado y a del dot
		print('"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg datosm.txt -o "'+os.getcwd()+'\\grafom1.jpg"')
		check_output('"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg datosm.txt -o "'+os.getcwd()+'\\grafom1.jpg"', shell=True)
		return str(mng)



	def graficar_2(self):
		pass


	def  ver_por_dep(self,emp):
		todos=""
		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh
				avlrr =nodotemh.getavl()
				if(cabevertical(nodotemh)!=None):
					if (str(cabevertical(nodotemh).getinfo())==str(emp)):
						if(avlrr!=None):
							
							k = avlrr.listarActivos()
							todos =todos+ k.lista_comas()


				

				while( nodoadentro!=None ):		
					#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					#print ("cabecera dentro",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh

				print ("cabecera afurea",nodoadentro.getinfo())
				if(cabevertical(nodotemh)!=None):
					if (str(cabevertical(nodoadentro).getinfo())==str(emp)):
						nodoadentro=nodoadentro.getatras()
						while( nodoadentro!=None ):	
							if(nodoadentro.getatras()!=None):	
								avlrr =nodoadentro.getavl()
								if(avlrr!=None):
									if(todos==""):
										k = avlrr.listarActivos()
										todos =todos+ k.lista_comas()
									else:
										k = avlrr.listarActivos()
										todos =todos+ ","+k.lista_comas()


							nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		return (todos)

	def  ver_por_emp(self,emp):
		todos=""
		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh
				avlrr =nodotemh.getavl()
				if(cabeceral(nodotemh)!=None):
					if (str(cabeceral(nodotemh).getinfo())==str(emp)):
						if(avlrr!=None):
							
							k = avlrr.listarActivos()
							todos =todos+ k.lista_comas()


				

				while( nodoadentro!=None ):		
					#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					#print ("cabecera dentro",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None ):
				nodoadentro = nodotemh

				print ("cabecera afurea",nodoadentro.getinfo())
				if(cabevertical(nodotemh)!=None):
					if (str(cabevertical(nodoadentro).getinfo())==str(emp)):
						nodoadentro=nodoadentro.getatras()
						while( nodoadentro!=None ):	
							if(nodoadentro.getatras()!=None):	
								avlrr =nodoadentro.getavl()
								if(avlrr!=None):
									if(todos==""):
										k = avlrr.listarActivos()
										todos =todos+ k.lista_comas()
									else:
										k = avlrr.listarActivos()
										todos =todos+ ","+k.lista_comas()


							nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()

		return (todos)


	def eliminarnosirve(self,nombre,tipo ):
		print("...................................................Eliminar...........................................")

			#nodocolumnaa = nodofilaletra(nodotem,nombre)
		letra = nombre
		nodotem = self.cl
		nodotemletra = nodosd.nodosd1()
		while (nodotem!=None):
			if ((letra) ==(str(nodotem.getinfo()))):
				
				nodotemletra=nodotem
				break
			nodotem = nodotem.getabajo()

		nododotemub = nodosd.nodosd1()
		while (nodotem!=None):
			if (cabeceral(nodotem)!=None):
				print ("cabeceral",cabeceral(nodotem).getinfo())
				if (nombre ==(str(nodotem.getinfo())) and tipo == cabeceral(nodotem).getinfo()):
					
					nododotemub =nodotem
					break

			nodotem = nodotem.getsig()


		print ("encontrado",str(nododotemub.getinfo()))

		if (nododotemub.getinfo()==nombre):
			print ("iguales nodo adelante eliminar")
			if (nododotemub.getatras()!=None):
				print ("iguales nodo adelante eliminar con atras")
				infoo = nododotemub.getatras().getinfo()
				nododotemub.getatras().setnuevoinfo(nododotemub.getinfo())
				nododotemub.setnuevoinfo(infoo)
				temi = nododotemub
				while (temi!=None):
					if (temi.getinfo()==nombre):
						if (temi.getatras()!=None):
							print ("distintos eliminar",temi.getinfo())
							temitem = temi.getatras()
							temicab = temi.getadelante()
							temicab.setatras(temi.getatras())
							temitem.setadelante(temicab)
							temi.setadelante(None)
							temi.setatras(None)

						else:
							print ("distintos eliminar",temi.getinfo())
							temitem = temi.getatras()
							temicab = temi.getadelante()
							temicab.setatras(temi.getatras())
							temi.setadelante(None)
							temi.setatras(None)

							
					temi = temi.getatras()
			else:
				print ("iguales nodo adelante eliminar sin atras")

				if (nododotemub.getsig()==None and nododotemub.getante().getinfo()==nombre):
					print ("iguales nodo adelante eliminar sin atras para eliminar letra")
					if (nombre== self.cl.getinfo()):
						self.cl = self.cl.getabajo()
					try:
						nododotemub.getante().getarriba().setabajo(nododotemub.getante().getabajo())
					except:
						print ("iguales nodo adelante eliminar sin atras para eliminar letra error para set abajo")
						
					try:
						nodotemfinol=nododotemub.getante().getarriba()
						nododotemub.getante().getabajo().setarriba(nodotemfinol)
					except:
						print ("iguales nodo adelante eliminar sin atras para eliminar letra error para set arriba")
						
					nododotemub.setante(None)
				else:
					nododotemub.getante().setsig(nododotemub.getsig())
					if (nododotemub.getsig()!=None):
						nododotemub.getsig().setante(nododotemub.getante())



				if (nododotemub.getabajo()==None and nododotemub.getarriba().getinfo()==tipo):
					if (tipo== self.cdir.getinfo()):
						self.cdir = self.cdir.getsig()
					try:
						nododotemub.getarriba().getante().setsig(nododotemub.getarriba().getsig())
					except:
						print ("iguales nodo adelante eliminar sin atras para eliminar dir error para set sig")

					try:
						nododotemub.getarriba().getsig().setante(nododotemub.getarriba().getante())
					except:
						print ("iguales nodo adelante eliminar sin atras para eliminar dir error para set ante")


					nododotemub.setarriba(None)
				else:
					nododotemub.getarriba().setabajo(nododotemub.getabajo())
					if (nododotemub.getabajo()!=None):
						nododotemub.getabajo().setarriba(nododotemub.getarriba())



				


		else:
			print ("distintos nodo addelante eliminar")
			temi = nododotemub
			while (temi!=None):
				if (temi.getinfo()==nombre):
					if (temi.getatras()!=None):
						print ("distintos eliminar",temi.getinfo())
						temitem = temi.getatras()
						temicab = temi.getadelante()
						temicab.setatras(temi.getatras())
						temitem.setadelante(temicab)
						temi.setadelante(None)
						temi.setatras(None)

					else:
						print ("distintos eliminar",temi.getinfo())
						temitem = temi.getatras()
						temicab = temi.getadelante()
						temicab.setatras(temi.getatras())
						temi.setadelante(None)
						temi.setatras(None)

						
				temi = temi.getatras()



		#print (nodotemletra.getinfo(),"-@-",nodotemdir.getinfo())
		#buscar nodo exacto de letra a enlazar
		#nodocolumnaa = nodocolumnadir(nodotem,tipo)
		"""
		ttp = nodotemdir.getabajo()
		condi=False

		while (ttp!=None):
			if(ttp.getinfo()==nombre):
				condi=True
				break

			ttp = ttp.getabajo()

		if (condi==True):
			print ("interno antes del while",ttp.getinfo())
			while (ttp!=None and ttp.getatras()!=None):
	 			print ("interno",ttp.getinfo())
	 			ttp = ttp.getatras()
"""




		#

		






def nodocolumnadir(nodotem,tipo):
	nodoenviar = nodosd.nodosd1()
	nodoenviar = nodotem
	tem = nodotem.getsig()
	while (tem!=None):
		temcolum = tem
		print ("valor arriba tem",temcolum.getinfo())
		while (temcolum.getarriba()!=None):
			temcolum = temcolum.getarriba()
			print ("valor arriba temcolum",temcolum.getinfo())
		if(tipo < temcolum.getinfo()):
			nodoenviar= tem
			break
		if (tem.getsig()==None):
			print("nonoe","--",tem.getinfo())
			nodoenviar = tem


		tem=tem.getsig()
		try:
			print ("NODOENVIAR",nodoenviarb.getinfo())
		except Exception as e:
			pass

		
	return nodoenviar

def encontrarcabletra(nodo):
	nodoenviar = nodosd.nodosd1()
	tem =nodo
	nodoenviar = tem
	while (tem!=None):
		nodoenviar = tem
		if(tem.getante()==None):
			break
		
		tem = tem.getante()
	return nodoenviar
def cabeceral(nodotem):
	nodoenviar = nodosd.nodosd1()
	tem =nodotem.getarriba()
	nodoenviar = tem
	while (tem!=None):
		nodoenviar = tem
		tem = tem.getarriba()
	return nodoenviar

def cabeceradir(nodotem):
	nodoenviar = nodosd.nodosd1()
	tem =nodotem.getante()
	nodoenviar = tem
	while (tem!=None):
		nodoenviar = tem
		tem = tem.getante()
	return nodoenviar




def nodofilaletra(nodotem,letra):
	nodoenviar = nodosd.nodosd1()
	nodoenviar = nodotem
	tem = nodotem.getabajo()
	while (tem!=None):
		temcolum = tem
		print ("valor arriba tem",temcolum.getinfo())
		while (temcolum.getante()!=None):
			temcolum = temcolum.getante()
			#
			print ("valor letra abajo",temcolum.getinfo())
		if(letra< str(temcolum.getinfo())):
			nodoenviar= tem
			break
		if (tem.getabajo()==None):
			nodoenviar = tem


		tem=tem.getabajo()
	return nodoenviar

def nodoactualcondir(nodotemdir,nombre):
	temp = nodotemdir
	while (temp!=None and temp.getabajo()!=None):
		print("copiado",temp.getinfo(),"-- nombre:--- ",nombre)
		if(temp.getinfo() ==nombre):
			break
		temp = temp.getabajo()

	return temp
def generar_random():
	longitud = 15
	valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	p = ""
	p = p.join([choice(valores) for i in range(longitud)])
	return p
def cabevertical(nodo):
	nodoenviar = nodosd.nodosd1()
	tem =nodo.getante()
	nodoenviar = tem
	while (tem!=None):
		nodoenviar = tem
		tem = tem.getante()
	return nodoenviar












