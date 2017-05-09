from NodoAvl import NodoAvl
from activo import activo
from listasimple import ListaS
import sys

class Logical:
    def __init__(self, f):
        self.v = f
    def setLogical(self, f):
        self.v = f
    def booleanValue(self):
        return self.v

class ArbolAvl:
    global raiz
    global listaAct
    cadena=""
    
    def __init__(self):
        self.raiz=None
        self.cadena=""

    def raizArbol(self):
        return self.raiz
    
    def obtenerRaiz(self):
        return self.raizArbol().visitar()

    def rotacionII(self, n, n1):
        n.ramaIzdo(n1.subarbolDcho())
        n1.ramaDcho(n)
        if n1.fe==-1:
            n.fe=0
            n1.fe=0
        else:
            n.fe=-1
            n1.fe=1
        return n1
    
    def rotacionDD(self, n, n1):
        n.ramaDcho(n1.subarbolIzdo())
        n1.ramaIzdo(n)
        if n1.fe==+1:
            n.fe=0
            n1.fe=0
        else:
            n.fe=+1
            n1.fe=-1
        return n1
    
    def rotacionID(self, n, n1):
        n2=None
        n2=n1.subarbolDcho()
        n.ramaIzdo(n2.subarbolDcho())
        n2.ramaDcho(n)
        n1.ramaDcho(n2.subarbolIzdo())
        n2.ramaIzdo(n1)
        if n2.fe==+1:
            n1.fe=-1
        else:
            n1.fe=0
        if n2.fe==-1:
            n.fe=1
        else:
            n.fe=0 
            n2.fe=0
        return n2
    
    def rotacionDI(self, n, n1):
        n2=None
        n2=n1.subarbolIzdo()
        n.ramaDcho(n2.subarbolIzdo())
        n2.ramaIzdo(n)
        n1.ramaIzdo(n2.subarbolDcho())
        n2.ramaDcho(n1)
        if n2.fe == +1: 
            n.fe = -1 
        else:
            n.fe = 0 
        if n2.fe == -1:
            n1.fe = 1 
        else:
            n1.fe = 0 
            n2.fe = 0 
        return n2
    
    def insertarAvl(self, raiz, dt, h): 
        n1=None
        if (raiz == None): 
            raiz = NodoAvl(dt)
            h.setLogical(True)
            pass
        elif dt.menorQue(raiz.valorNodo()): 
            iz=None
            iz = self.insertarAvl(raiz.subarbolIzdo(), dt, h)
            raiz.ramaIzdo(iz)  
            if (h.booleanValue()):  
                if raiz.fe==1:       
                    raiz.fe = 0
                    h.setLogical(False)     
                    pass      
                elif  raiz.fe==0:      
                    raiz.fe = -1    
                    pass
                elif  raiz.fe==-1: 
                    n1 = raiz.subarbolIzdo()    
                    if (n1.fe == -1):     
                        raiz = self.rotacionII(raiz, n1)  
                    else:     
                        raiz = self.rotacionID(raiz, n1)    
                    h.setLogical(False)
            pass
        elif dt.mayorQue(raiz.valorNodo()):
            dr=None
            dr = self.insertarAvl(raiz.subarbolDcho(), dt, h) 
            raiz.ramaDcho(dr)
            if (h.booleanValue()):
                if raiz.fe==1:        
                    n1 = raiz.subarbolDcho()    
                    if (n1.fe == +1):    
                        raiz = self.rotacionDD(raiz, n1)
                    else:      
                        raiz = self.rotacionDI(raiz,n1)     
                        h.setLogical(False);     
                        pass
                elif raiz.fe==0:      
                        raiz.fe = +1    
                        pass 
                elif raiz.fe==-1:      
                        raiz.fe = 0     
                        h.setLogical(False)
            pass  
        else:
            print("No puede haber claves repetidas " ) 
            pass
        return raiz
    
    def insertar(self, valor):
        h=Logical(False)
        dato=valor
        self.raiz=self.insertarAvl(self.raiz, dato, h)
        print("insertado"+str(dato.obtenerdato()))

    def eliminar (self, valor):
        dato=None
        dato = valor
        flag = Logical(False) 
        self.raiz = self.borrarAvl(self.raiz, dato, flag)

    def obtenerdato(self):  
        self.raiz=self.raizArbol()
        o = self.raiz.dato
        print("RAIZ="+str(o.obtenerdato()))
        try:
            if self.raiz.izdo!=None:
                p = self.raiz.izdo.dato
                print("RAIZ-NODO IZQ= "+str(p.obtenerdato()))
                pass
        except:
           # print "Unexpected error:", sys.exc_info()[0]
            raise
        try:
            if self.raiz.dcho!=None:
                q = self.raiz.dcho.dato
                print("RAIZ-NODO DER= "+str(q.obtenerdato()))
                pass
        except:
           # print "Unexpected error:", sys.exc_info()[0]
            raise        
        self.grafo()
        return self.cadena
        
    def borrarAvl(self, r, clave, cambiaAltura):
        if (r == None): 
            print(" Nodo no encontrado ")
        elif (clave.menorQue(r.valorNodo())): 
            iz=None
            iz = self.borrarAvl(r.subarbolIzdo(),clave,cambiaAltura)  
            r.ramaIzdo(iz)
            if (cambiaAltura.booleanValue()):  
                r = self.equilibrar1(r, cambiaAltura) 
        elif (clave.mayorQue(r.valorNodo())):
            dr=None   
            dr = self.borrarAvl(r.subarbolDcho(), clave, cambiaAltura)  
            r.ramaDcho(dr)  
            if (cambiaAltura.booleanValue()):
                r = self.equilibrar2(r, cambiaAltura) 
        else:  # Nodo encontrado    
            q=None
            q = r   # nodo a quitar del 
            if (q.subarbolIzdo()== None):
                r = q.subarbolDcho()  
                cambiaAltura.setLogical(True)  
            elif (q.subarbolDcho() == None):    
                r = q.subarbolIzdo()
                cambiaAltura.setLogical(True)
            else:  
              # tiene rama izquierda y derecha 
                iz=None   
                iz = self.reemplazar(r, r.subarbolIzdo(),cambiaAltura)   
                r.ramaIzdo(iz)  
                if (cambiaAltura.booleanValue()):
                    r = self.equilibrar1(r, cambiaAltura)  
            q = None    
        return r
    
    def reemplazar(self, n, act, cambiaAltura): 
        if (act.subarbolDcho() != None): 
            d=None
            d = self.reemplazar(n, act.subarbolDcho(), cambiaAltura) 
            act.ramaDcho(d)  
            if (cambiaAltura.booleanValue()):   
                act = self.equilibrar2(act, cambiaAltura)
        else:
            n.nuevoValor(act.valorNodo())
            n = act 
            act = act.subarbolIzdo()
            n = None  
            cambiaAltura.setLogical(True) 
        return act
        
    def equilibrar1(self, n, cambiaAltura):
        n1=None
        if(n.fe==-1):  
            n.fe = 0
            pass
        elif(n.fe==0):
            n.fe = 1      
            cambiaAltura.setLogical(False)      
            pass
        elif(n.fe==+1):  #se aplicar un tipo de rotacin derecha       
            n1 = n.subarbolDcho()      
            if (n1.fe >= 0):     
                if (n1.fe == 0):  # la altura no vuelve a disminuir          
                    cambiaAltura.setLogical(False)      
                n = self.rotacionDD(n, n1)            
            else:
                n = self.rotacionDI(n, n1)    
            pass
        return n 
    def equilibrar2(self, n, cambiaAltura):
        n1=None
        if(n.fe==-1): 
            n1 = n.subarbolIzdo()      
            if (n1.fe <= 0):      
                if (n1.fe == 0):         
                    cambiaAltura.setLogical(False)
                n = self.rotacionII(n, n1)        
            else:
                n = self.rotacionID(n,n1);      
            pass  
        elif(n.fe==0): 
            n.fe = -1      
            cambiaAltura.setLogical(False)      
            pass
        elif(n.fe==+1): 
            n.fe = 0 
            pass 
        return n
    
    def recorrer(self):  
        self.raiz=self.raizArbol()
        o = self.raiz.dato
        print("RAIZ="+str(o.obtenerdato()))
        try:
            if self.raiz.izdo!=None:
                p = self.raiz.izdo.dato
                print("RAIZ-NODO IZQ= "+str(p.obtenerdato()))
                pass
        except:
           # print "Unexpected error:", sys.exc_info()[0]
            raise
        try:
            if self.raiz.dcho!=None:
                q = self.raiz.dcho.dato
                print("RAIZ-NODO DER= "+str(q.obtenerdato()))
                pass
        except:
           # print "Unexpected error:", sys.exc_info()[0]
            raise        
        self.grafo()
        return self.cadena

    def reemplazar_solo_dato(self, valor, nombre, desc):
        dato=None
        dato = valor
        self.raiz = self.reemplazo_datos(self.raiz, dato, nombre, desc)
    
    def reemplazo_datos(self, r, clave, nombre, desc):
        if (r == None): 
            print(" Nodo no encontrado ")
        elif (clave.menorQue(r.valorNodo())): 
            iz = self.reemplazo_datos(r.subarbolIzdo(),clave, nombre, desc)
        elif (clave.mayorQue(r.valorNodo())):
            dr=None   
            dr = self.reemplazo_datos(r.subarbolDcho(), clave, nombre, desc)  
        else:  # Nodo encontrado    
            act=r.valorNodo()
            act.nombre=nombre
            act.desc=desc
            r.setValor(act)
        return r

    def inorden(self, r): 
        if(r != None):  
            r1=""
            aux=""
            aux2=""
            aux3=""
            self.inorden(r.subarbolIzdo())  
            try:
                if r.izdo!=None:
                    r2= r.izdo.visitar()
                    aux2=aux2+("-> t"+str(r2))
            except:
           # print "Unexpected error:", sys.exc_info()[0]
                raise
            r1= r.visitar()
            aux=aux+("t"+str(r1)+"[label=\""+str(r1)+str(r.visitar_data())+"\"];")
            self.inorden (r.subarbolDcho())
            try:
                if r.dcho!=None:
                    r3= r.dcho.visitar()
                    aux3=aux3+("-> t"+str(r3)) 
            except:
           # print "Unexpected error:", sys.exc_info()[0]
                raise
            self.cadena=self.cadena+"\n"+aux+"\n t"+str(r1)+aux2+";"+"t"+str(r1)+aux3+";"

    def listarActivos(self):
        self.listaAct=ListaS()
        self.preorden(self.raiz)
        return self.listaAct

    def preorden(self, r): 
        if(r != None):
            r.visitar()  
            self.listaAct.enlistar(r.valorNodo())
            self.preorden(r.subarbolIzdo())  
            self.preorden(r.subarbolDcho())

    def preorden2(self, r): 
        if(r != None):
            r.visitar()
            self.cadena=self.cadena+(r.valorNodo().obtenerdato()+",")
            self.cadena=self.cadena+(r.valorNodo().obtenernombre()+",")
            self.cadena=self.cadena+(r.valorNodo().obtenerdesc()+"")
            self.cadena=self.cadena+"$"  
            self.preorden2(r.subarbolIzdo())  
            self.preorden2(r.subarbolDcho())
            
    def grafo(self):
        self.cadena=""
        self.inorden(self.raiz)
        self.cadena=self.cadena+""
        print(self.cadena)

    def obter_activos(self):
        self.cadena=""
        self.preorden2(self.raiz)
        self.cadena=self.cadena+""
        return (self.cadena)

    def agregar(self, nombre, desc, codigo):
        prueba=None
        prueba=activo(nombre, desc, codigo)
        self.insertar(prueba)

    def reemplazo(self, nombre, desc, codigo):
        temp=None
        temp=activo(nombre, desc, codigo)
        self.reemplazar_solo_dato(temp, nombre, desc)

    def borrar(self, nombre, desc, codigo):
        temp=None
        temp=activo(nombre, desc, codigo)
        self.eliminar(temp)
