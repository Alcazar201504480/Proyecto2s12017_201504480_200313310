from Nodo import Nodo as nodo

class NodoAvl(nodo):
    fe=0
    dato = None
    izdo = None
    dcho = None

    def __init__(self, ramaIzdo, valor, ramaDcho):
        self.dato=valor
        self.izdo=ramaIzdo
        self.dcho=ramaDcho
        fe = 0

    def __init__(self, valor):
#        super(Nodo, self).__init__()
        self.dato = valor
        self.izdo=None
        self.dcho=None
        fe = 0

    def valorNodo(self):
        return self.dato
    def setValor(self, dato):
    	self.dato=dato
    def subarbolIzdo(self):
        return self.izdo
    def subarbolDcho(self):
        return self.dcho
    def nuevoValor(self, d):
        self.dato=d
    def ramaIzdo(self, n):
        self.izdo=n
    def ramaDcho(self, n):
        self.dcho=n
    def visitar_data(self):
        r= self.dato
        print(str(r.obtenernombre()) + str(r.obtenerdesc())+" ") 
        h =  "\n"+r.obtenernombre()+"\n"+r.obtenerdesc()
        return h
    def visitar_data2(self):
        r= self.dato
        print(str(r.obtenernombre()) + str(r.obtenerdesc())+" ") 
        h =  "\n"+r.obtenernombre()+","+r.obtenerdesc()
        return h
    def visitar(self):
        r= self.dato
        print(str(r.obtenerdato()) + "") 
        h =  r.obtenerdato()
        return h
      

  