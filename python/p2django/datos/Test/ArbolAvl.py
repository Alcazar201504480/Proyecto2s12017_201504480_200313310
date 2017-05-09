#from archivo import archivo
import sys
import subprocess
from Cmd import cmd


class archivo:
    nombre=None
    desc=None
    codigo=None

    def __init__(self, nombre_archivo):
        self.codigo=str(nombre_archivo)

    def obtenerdato(self):
        return str(self.codigo)

    def obtenernombre(self):
        return self.nombre

    def obtenerdesc(self):
        return self.desc

    def igualQue(self, op2):
        #    return int(''.join(str(ord(c)) for c in self.codigo)) == int(''.join(str(ord(c)) for c in op2.codigo))
        return self.codigo == op2.codigo

    def menorQue(self, op2):
        return self.codigo < op2.codigo

    def menorIgualQue(self, op2):
        return self.codigo <= op2.codigo

    def mayorQue(self, op2):
        return self.codigo > op2.codigo

    def mayorIgualQue(self, op2):
        return self.codigo >= op2.codigo



class NodoAvl:

    def __init__(self, ramaIzdo, valor, ramaDcho):
        self.dato=valor
        self.izdo=ramaIzdo
        self.dcho=ramaDcho
        self.fe = 0

    def __init__(self, valor):
        # super(Nodo, self).__init__()
        self.dato = valor
        self.izdo=None
        self.dcho=None
        self.fe = 0

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

    def visitar(self):
        r= self.dato
        print(str(r.obtenerdato()) + "") 
        h =  r.obtenerdato()
        return h
      


class Avl:
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
        n2=n1.subarbolDcho()
        n.ramaIzdo(n2.subarbolDcho())
        n2.ramaDcho(n)
        n1.ramaDcho(n2.subarbolIzdo())
        n2.ramaIzdo(n1)
        if n2.fe == +1:
            n1.fe = -1
        else:
            n1.fe = 0
        if n2.fe == -1:
            n.fe = 1
        else:
            n.fe = 0
        n2.fe = 0
        return n2
    
    def rotacionDI(self, n, n1):
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
        if raiz is None:
            raiz = NodoAvl(dt)
            h.setLogical(True)
            pass
        elif dt.menorQue(raiz.valorNodo()):
            iz=None
            iz = self.insertarAvl(raiz.subarbolIzdo(), dt, h)
            raiz.ramaIzdo(iz)  
            if h.booleanValue():
                if raiz.fe==1:       
                    raiz.fe = 0
                    h.setLogical(False)     
                    pass      
                elif raiz.fe == 0:
                    raiz.fe = -1    
                    pass
                elif raiz.fe == -1:
                    n1 = raiz.subarbolIzdo()    
                    if n1.fe == -1:
                        raiz = self.rotacionII(raiz, n1)
                    else:     
                        raiz = self.rotacionID(raiz, n1)
                        pass
                    h.setLogical(False)

        elif dt.mayorQue(raiz.valorNodo()):
            dr=None
            dr = self.insertarAvl(raiz.subarbolDcho(), dt, h) 
            raiz.ramaDcho(dr)
            if h.booleanValue():
                if raiz.fe==1:        
                    n1 = raiz.subarbolDcho()    
                    if n1.fe == +1:
                        raiz = self.rotacionDD(raiz, n1)
                    else:      
                        raiz = self.rotacionDI(raiz,n1)     
                    h.setLogical(False)
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
            print ("Unexpected error:", sys.exc_info()[0])
            raise
        try:
            if self.raiz.dcho!=None:
                q = self.raiz.dcho.dato
                print("RAIZ-NODO DER= "+str(q.obtenerdato()))
                pass
        except:
            print ("Unexpected error:", sys.exc_info()[0])
            raise        
        self.grafo()
        return self.cadena
        
    def borrarAvl(self, r, clave, cambiaAltura):
        if r is None:
            print(" Nodo no encontrado ")
        elif clave.menorQue(r.valorNodo()):
            iz = None
            iz = self.borrarAvl(r.subarbolIzdo(),clave,cambiaAltura)  
            r.ramaIzdo(iz)
            if cambiaAltura.booleanValue():
                r = self.equilibrar1(r, cambiaAltura) 
        elif clave.mayorQue(r.valorNodo()):
            dr=None   
            dr = self.borrarAvl(r.subarbolDcho(), clave, cambiaAltura)  
            r.ramaDcho(dr)  
            if cambiaAltura.booleanValue():
                r = self.equilibrar2(r, cambiaAltura) 
        else:  # Nodo encontrado    
            q=None
            q = r   # nodo a quitar del arbol
            if q.subarbolIzdo()is None:
                r = q.subarbolDcho()  
                cambiaAltura.setLogical(True)  
            elif q.subarbolDcho() is None:
                r = q.subarbolIzdo()
                cambiaAltura.setLogical(True)
            else:  
              # tiene rama izquierda y derecha 
                iz=None   
                iz = self.reemplazar(r, r.subarbolIzdo(),cambiaAltura)   
                r.ramaIzdo(iz)  
                if cambiaAltura.booleanValue():
                    r = self.equilibrar1(r, cambiaAltura)  
            q = None    
        return r
    
    def reemplazar(self, n, act, cambiaAltura): 
        if act.subarbolDcho() is not None:
            d=None
            d = self.reemplazar(n, act.subarbolDcho(), cambiaAltura) 
            act.ramaDcho(d)  
            if cambiaAltura.booleanValue():
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
        if n.fe==-1:
            n.fe = 0
            pass
        elif n.fe==0:
            n.fe = 1      
            cambiaAltura.setLogical(False)      
            pass
        elif n.fe==+1:  #se aplicar un tipo de rotacin derecha
            n1 = n.subarbolDcho()      
            if n1.fe >= 0:
                if n1.fe == 0:  # la altura no vuelve a disminuir
                    cambiaAltura.setLogical(False)      
                n = self.rotacionDD(n, n1)            
            else:
                n = self.rotacionDI(n, n1)    
            pass
        return n 
    def equilibrar2(self, n, cambiaAltura):
        n1=None
        if n.fe==-1:
            n1 = n.subarbolIzdo()      
            if n1.fe <= 0:
                if n1.fe == 0:
                    cambiaAltura.setLogical(False)
                n = self.rotacionII(n, n1)        
            else:
                n = self.rotacionID(n,n1)
            pass  
        elif n.fe==0:
            n.fe = -1      
            cambiaAltura.setLogical(False)      
            pass
        elif n.fe==+1:
            n.fe = 0 
            pass 
        return n
    
    def recorrer(self):  
        self.raiz = self.raizArbol()
        o = self.raiz.dato
        print("RAIZ="+str(o.obtenerdato()))
        try:
            if self.raiz.izdo is not None:
                p = self.raiz.izdo.dato
                print("RAIZ-NODO IZQ= "+str(p.obtenerdato()))
                pass
        except:
           # print "Unexpected error:", sys.exc_info()[0]
            raise
        try:
            if self.raiz.dcho is not None:
                q = self.raiz.dcho.dato
                print("RAIZ-NODO DER= "+str(q.obtenerdato()))
                pass
        except:
           # print "Unexpected error:", sys.exc_info()[0]
            raise        
        self.grafo()
        return self.cadena

    def reemplazar_con_objeto(self, valor, nombrereemp, descreemp):
        dato=None
        dato = valor
        self.raiz = self.reemplazo_datos(self.raiz, dato, nombrereemp, descreemp)
        return self.raiz

    def reemplazo_datos(self, r, clave, nombre, desc):
        if r is None:
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

    def localizar(self, raizSub, buscado):
        if raizSub is None:
            return None
        elif buscado.igualQue(raizSub.valorNodo()):
            print("encontrado-<-")
            return raizSub
        elif buscado.menorQue(raizSub.valorNodo()):
            return self.localizar(raizSub.subarbolIzdo(), buscado)
        else:
            return self.localizar(raizSub.subarbolDcho(), buscado)

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
            aux=aux+("t"+str(r1)+"[label=\""+str(r1)+"\"];")
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

    def grafo(self):
        self.cadena="digraph g{\n"
        self.inorden(self.raiz)
        return self.cadena + "\n}"

    def graficar_imagen(self):
        c=cmd()
        g= self.grafo()
        c.escribir_dot(g, "AVL")
        c.ejecutar_cmd("AVL")

    def buscar(self, clave):
        dato = archivo(clave)
        if self.raiz is None:
            return None
        else:
            return self.localizar(self.raiz, dato)

    def agregar(self, codigo):
        prueba=archivo(codigo)
        self.insertar(prueba)

    def agregar_objeto(self, obj):
        self.insertar(obj)

    def renombrar(self, codigo, nuevo_codigo):
        self.borrar(codigo)

    def reemplazo(self, codigo, nombre2, desc2):
        temp=archivo(codigo)
        self.reemplazar_con_objeto(temp, nombre2, desc2)

    def borrar(self, codigo):
        temp=archivo(codigo)
        self.eliminar(temp)

    def renombrar(self, codigo, nuevo):
        temp=self.buscar(codigo)
        if temp is not None:
            sacardatos = temp.valorNodo()
            self.borrar(codigo)
            n = archivo(nuevo)
            n.desc = sacardatos.desc
            n.nombre = sacardatos.nombre
            self.agregar_objeto(n)


class Logical:
    def __init__(self, f):
        self.v = f

    def setLogical(self, f):
        self.v = f

    def booleanValue(self):
        return self.v

if __name__ == '__main__':
    avl = Avl()
    #nombre, descripcion, clave
    avl.agregar("a")
    avl.agregar("alagran")
    avl.agregar("abaco")
    avl.agregar("archivo")
    avl.agregar("b")
    avl.agregar("bread")
    avl.agregar("f")
    avl.agregar("fopop")
    avl.agregar("c")
    avl.agregar("ggg")
    avl.agregar("gato")
    avl.agregar("hhh")
    avl.agregar("12")
    avl.agregar("22")
    avl.agregar("3")
    avl.agregar("52")
    avl.agregar("1")

    #si queres reemplazar el nombre y descripcion del archivo
    avl.reemplazo("32", "NO2", "DO2")
    #si queres agregar mas atributos a la clase archivo, tene cuidado con este metodo
    #tenes que copiar cada atributo nuevo a una nueva instancia archivo
    avl.renombrar("a", 'zeta')

    print("----------------------------------")
    avl.borrar("archivo")
    avl.borrar("gato")
    avl.borrar("b")
    print("----------------------------------")


    t=avl.buscar('52')

    print(str(t))

    if t is not None:
        print(t.dato.codigo)
        print(t.dato.nombre)
    print("-----------<<<<<<<<>>>>>>>>-----------------------")
    print("----------------------------------")
    avl.graficar_imagen()
    print("----------------------------------")
