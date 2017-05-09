import bisect
from ArbolAvl import Avl
from Cmd import cmd

class _Carpeta(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.carpetas = ArbolB(5)
        self.archivos = Avl()

    def renombrarCarpeta(self, nombre_actual, nombre_nuevo):
        return self.carpetas.renombrar(nombre_actual, nombre_nuevo)

    def renombrarArchivo(self, nombre_actual, nombre_nuevo):
        self.archivos.renombrar(nombre_actual, nombre_nuevo)

    def agregarCarpeta(self, nombre):
        self.carpetas.insertar(nombre)

    def agregarArchivo(self, nombre):
        self.archivos.agregar(nombre)

    def eliminarCarpeta(self, nombre_actual):
        carpeta = _Carpeta(nombre_actual)
        return self.carpetas.eliminar(carpeta)

    def buscarCarpeta(self, carpeta):
        return self.carpetas.buscarCarpeta(carpeta)

    def buscarArchivoPorNombre(self, nombre):
        return self.archivos.buscar(nombre)

    def buscarCarpetaPorNombre(self, nombre):
        carpeta = _Carpeta(nombre)
        return self.carpetas.buscarCarpeta(carpeta)

    # buscar una carpeta por path
    # debe estar en formato /nombrecarpeta/carpeta/otracarpeta
    def buscarCarpetaPorPath(self, path):
        nombre_carpeta = ""
        carpeta_final = None
        if path.find("/") == 0:
            path = path[1:]

        if path.find("/") > 0:
            nombre_carpeta = path[:path.find("/")]
            path = path[path.find("/")+1:]
        else:
            nombre_carpeta = path
            path = None

        carpeta_final = self.buscarCarpetaPorNombre(nombre_carpeta)
        if carpeta_final is None:
            print("carpeta " + nombre_carpeta + " no encontrada")
        else:
            if path is not None:
                carpeta_final = carpeta_final.buscarCarpetaPorPath(path)
        return carpeta_final

    # buscar un archivo por path completo
    # debe estar en formato /nombrecarpeta/carpeta/miarchivo.gif
    def buscarArchivoPorPath(self, path):
        nombre_archivo = None
        archivo_final = None
        print(path)
        if path.rfind("/") < 0:
            nombre_archivo = path
            path = None
        else:
            nombre_archivo = path[path.rfind("/")+1:]
            path = path[:path.rfind("/")]

        print(path)
        print(nombre_archivo)
        if path is None:
            carpeta = self
        else:
            carpeta = self.buscarCarpetaPorPath(path)

        # buscar el archivo
        if carpeta is not None:
            archivo_final = carpeta.buscarArchivoPorNombre(nombre_archivo)

        if archivo_final is None:
            print("archivo " + nombre_archivo + " no encontrado")

        return archivo_final

    def obtenerListaCarpetas(self):
        return self.carpetas.obtenerListaCarpetas()

    def obtenerListaArchivos(self):
        return self.archivos.listarActivos()

    def graficarArbolB(self):
        return self.carpetas.generarGraphviz()

    def graficarArbolAvl(self):
        return self.archivos.graficar_imagen()

    def __str__(self):
        return '%s' % (self.nombre)

    def __repr__(self):
        return str(self)

    def __eq__( self, other ):
        return self.nombre == other.nombre

    def __lt__( self, other ):
        return self.nombre < other.nombre

    def __le__( self, other ):
        return self.nombre <= other.nombre

    def __gt__( self, other ):
        return self.nombre > other.nombre

    def __ge__( self, other ):
        return self.nombre >= other.nombre

    def __ne__( self, other ):
        return self.nombre != other.nombre

class _NodoArbol(object):
    def __init__(self, carpetas=None, hijos=None):
        self.padre = None
        self.carpetas = carpetas or []
        self.hijos = hijos
        # actualizar el nodo padre dentro de todos los hijos,
        # en caso este haya cambiado
        if self.hijos:
            for i in self.hijos:
                i.padre = self

    def __str__(self):
        return 'Nodo(%r, %d)' % (
                #id(self),
                #id(self.padre),
                self.carpetas,
                len(self.hijos) if self.hijos else 0)

    def pretty_print(self, tab=''):
        print('%s%s' % (tab, self))
        if self.hijos:
            for i in self.hijos:
                i.pretty_print(tab + '   ')

    # Revisar recursivamente la integridad del arbol
    # segun las reglas, esto se usa para verificar que los
    # algoritmos estan correctamente implementados
    def validarIntegridad(self, arbol):
        tieneHijos = self.hijos is not None
        nodoRaiz = self.padre is None

        assert(self.carpetas is not None)

        # a exepcion de la raiz, todo nodo debe tener al menos "m/2-1" claves (carpetas)
        if not nodoRaiz and tieneHijos:
            assert(arbol.minimoCarpetas <= len(self.carpetas))

        # un nodo no puede tener mas de "m-1" claves (carpetas)
        assert(len(self.carpetas) <= arbol.maximoCarpetas)

        # la raiz debe tener al menos 2 hijos, a excepcion de que sea una hoja
        if nodoRaiz and tieneHijos:
            assert(len(self.hijos) >= 2)

        # un nodo con k hijos debe contener k-1 claves
        if tieneHijos:
            assert((len(self.carpetas) + 1) == len(self.hijos))

        # revisar que las claves (carpetas) esten ordenadas
        prev = None
        for i in self.carpetas:
            if prev is not None:
                assert(i > prev)
            prev = i

        # hacer la revision de forma recursiva por cada sub-arbol
        if self.hijos:
            for i in self.hijos:
                assert(i.padre is self)
                i.validarIntegridad(arbol)

    # Buscar una carpeta de forma recursiva
    #
    # Retorna el Nodo y la posicion donde se encuentra la carpeta
    # dentro del nodo, si no se encuentra devolvera la posicion donde
    # debe ser insertada la carpeta
    #
    # Retorna:
    # (False, nodo, pos) - Si la carpeta no existe
    # (True, nodo, pos) - Si la carpeta existe
    def buscar(self, carpeta):
        i = bisect.bisect_left(self.carpetas, carpeta)
        #print("%r %s - index = %d" % (self.carpetas, carpeta, i))
        if (i != len(self.carpetas) and not carpeta < self.carpetas[i]):
            # la clave (carpeta) ha sido encontrada
            assert(str(self.carpetas[i]) == str(carpeta))
            return (True, self, i)

        if self.hijos is not None:
            assert(len(self.hijos) >= i and self.hijos[i])
            # Buscar de forma recursiva
            return self.hijos[i].buscar(carpeta)
        else:
            return (False, self, i)


    # Dividir un Nodo en 2
    #
    # Si se envia el valor de "carpeta" y "slot" se insertara al arbol luego
    # de hacer el split.  Si adicionalmente se envia una lista de nodos hijos
    # se divide recursivamente, la lista de nodos hijos representa los nodos
    # que fueron separados por la "carpeta" para que estos se inserten 
    # nuevamente al arbol
    def _dividirNodo(self, arbol, carpeta=None, slot=None, listaNodosHijos=None):
        assert(carpeta is None or (slot is not None))

        midList = [] if carpeta is None else [ carpeta ]
        if slot is None:
            slot = 0

        # get the median of self.carpetas and val
        splitCarpetas = self.carpetas[0:slot] + midList + self.carpetas[slot:]
        indiceMitad = len(splitCarpetas) // 2

        carpetasIzquierda = splitCarpetas[0:indiceMitad]
        carpetaMitad = splitCarpetas[indiceMitad]
        carpetasDerecha = splitCarpetas[indiceMitad + 1:]

        tieneHijos = self.hijos is not None

        if tieneHijos:
            if listaNodosHijos is not None:
                splithijos = (self.hijos[0:slot] +
                                 list(listaNodosHijos) +
                                 self.hijos[slot + 1:])
            else:
                splithijos = self.hijos
            hijosIzquierda = splithijos[0:len(carpetasIzquierda) + 1]
            hijosDerecha = splithijos[len(carpetasIzquierda) + 1:]
        else:
            hijosIzquierda = None
            hijosDerecha = None

        nodoIzquierdo = _NodoArbol(carpetasIzquierda, hijosIzquierda)
        nodoDerecho = _NodoArbol(carpetasDerecha, hijosDerecha)

        if self.padre:
            self.padre.insertar(arbol,
                            carpetaMitad,
                            None,
                            (nodoIzquierdo, nodoDerecho))
        else:
            # crear la nueva raiz e incrementar la altura y tamano del arbol 
            nuevaRaiz = _NodoArbol([ carpetaMitad ], [nodoIzquierdo, nodoDerecho])
            nodoIzquierdo.padre = nuevaRaiz
            nodoDerecho.padre = nuevaRaiz
            arbol.raiz = nuevaRaiz
            arbol.altura += 1
            arbol.tamano += 1

    # Agregar una nueva clave (carpeta) al arbol B
    # la carpeta no debe de existir previamente
    def insertar(self, arbol, carpeta, slot=None, listaNodosHijos=None):
        # todas las inserciones empiezan en un nodo hoja,
        # a menos que se este agregando recursivamente en el padre
        # debido a una division (split) del nodo. 
        assert(self.hijos is None or listaNodosHijos)

        # validar si es un nodo interno y no es una hoja y no es la raiz
        # entonces este nodo si debe tener hijos, asi que esta funcion tuvo
        # que llamarse de forma recursiva con una listaNodosHijos y una
        # carpeta definida y con un len(listaNodosHijos) == 2
        tieneHijos = self.hijos is not None
        if tieneHijos:
            assert(listaNodosHijos and len(listaNodosHijos) == 2)
        else:
            assert(listaNodosHijos is None)

        # Si no ha sido encontrado, encontrar la posicion para insertar
        # dentro del nodo 
        if slot is None:
            slot = bisect.bisect_left(self.carpetas, carpeta)

        # insertamos solo si en el nodo actual aun existe espacio
        if len(self.carpetas) < arbol.maximoCarpetas:
            self.carpetas.insert(slot, carpeta)
            arbol.tamano += 1
            if listaNodosHijos:
                # actualizar la referencia al padre en los nodos que insertaremos
                for i in listaNodosHijos:
                    i.padre = self
                self.hijos[slot:slot + 1] = listaNodosHijos
            # we're done
            return True

        # si llegamos hasta aqui es poquer el nodo esta lleno y tenemos
        # que dividir el nodo
        self._dividirNodo(arbol, carpeta, slot, listaNodosHijos)
        return True

    def carpetaMenor(self, slot=0):
        if self.hijos:
            return self.hijos[slot].carpetaMenor()
        return self.carpetas[0], self, 0

    def carpetaMayor(self, slot=None):
        if slot is None:
            slot = len(self.carpetas) - 1
        if self.hijos:
            return self.hijos[slot + 1].carpetaMayor()
        return self.carpetas[-1], self, len(self.carpetas) - 1


    # eliminar una carpeta del arbol
    # la carpeta debe existir
    def eliminar(self, arbol, carpeta, slot=None):
        tieneHijos = self.hijos is not None
        if slot is None:
            # assert(slot is not None)
            slot = bisect.bisect_left(self.carpetas, carpeta)

        assert(slot != len(self.carpetas) and self.carpetas[slot] == carpeta)

        if not tieneHijos:
            # Eliminar clave (carpeta) del nodo
            del self.carpetas[slot]
            arbol.tamano -= 1
            if len(self.carpetas) < arbol.minimoCarpetas:
                # se llego a minimo de clave que puede tener una hoja
                # rebalancemos el arbol empezando con este nodo
                self._rebalancear(arbol)
        else:
            # find the minimum carpeta in the right subarbol
            # and use it as the separator carpeta to replace val
            newSep, nodo, indice = self.carpetaMenor(slot + 1)
            self.carpetas[slot] = newSep
            del nodo.carpetas[indice]
            arbol.tamano -= 1
            if len(nodo.carpetas) < arbol.minimoCarpetas:
                nodo._rebalancear(arbol)

    # rebalancear el arbol empezando con este nodo
    def _rebalancear(self, arbol):
        hermanoIzquierdo, hermanoDerecho, indice = self.obtenerHermanos()

        # solo la raiz puede no tener hermanos
        assert(hermanoDerecho or hermanoIzquierdo or self.padre is None)

        if self.padre is None:
            # esta operacion no la aplicamos a la raiz
            return

        tieneHijos = self.hijos is not None
        if tieneHijos:
            assert(hermanoDerecho is None or hermanoDerecho.hijos is not None)
            assert(hermanoIzquierdo is None or hermanoIzquierdo.hijos is not None)
        else:
            assert(hermanoDerecho is None or hermanoDerecho.hijos is None)
            assert(hermanoIzquierdo is None or hermanoIzquierdo.hijos is None)

        if not tieneHijos:
            if hermanoDerecho and len(hermanoDerecho.carpetas) > arbol.minimoCarpetas:
                indiceSeparacion = indice
                carpetaSeparacion = self.padre.carpetas[indiceSeparacion]
                # tomar el nodo del hijo derecho para realizar una rotacion a la izquierda
                self.padre.carpetas[indiceSeparacion] = hermanoDerecho.carpetas[0]
                del hermanoDerecho.carpetas[0]
                self.carpetas.append(carpetaSeparacion)
                return
            elif hermanoIzquierdo and len(hermanoIzquierdo.carpetas) > arbol.minimoCarpetas:
                indiceSeparacion = indice - 1
                carpetaSeparacion = self.padre.carpetas[indiceSeparacion]
                # tomar el nodo del hijo izquierdo para realizar una rotacion a la derecha
                self.padre.carpetas[indiceSeparacion] = hermanoIzquierdo.carpetas[-1]
                del hermanoIzquierdo.carpetas[-1]
                self.carpetas.insert(0, carpetaSeparacion)
                return

        # ahora tenemos que unir los 2 nodos
        if hermanoIzquierdo is not None:
            indiceSeparacion = indice - 1
            nodoIzquierdo = hermanoIzquierdo
            nodoDerecho = self
        elif hermanoDerecho is not None:
            indiceSeparacion = indice
            nodoIzquierdo = self
            nodoDerecho = hermanoDerecho
        else:
            assert(False)

        carpetaSeparacion = self.padre.carpetas[indiceSeparacion]

        nodoIzquierdo.carpetas.append(carpetaSeparacion)
        nodoIzquierdo.carpetas.extend(nodoDerecho.carpetas)
        del nodoDerecho.carpetas[:]
        del self.padre.carpetas[indiceSeparacion]
        assert(self.padre.hijos[indiceSeparacion + 1] is nodoDerecho)
        del self.padre.hijos[indiceSeparacion + 1]
        if nodoDerecho.hijos:
            nodoIzquierdo.hijos.extend(nodoDerecho.hijos)
            for i in nodoDerecho.hijos:
                i.padre = nodoIzquierdo

        if len(nodoIzquierdo.carpetas) > arbol.maximoCarpetas:
            # we have to split the newly formed nodo
            # this situation can aris only when merging inner nodos
            assert(tieneHijos)
            nodoIzquierdo._dividirNodo(arbol)

        if len(self.padre.carpetas) < arbol.minimoCarpetas:
            # rebalancear el padre
            self.padre._rebalancear(arbol)

        if self.padre.padre is None and not self.padre.carpetas:
            arbol.raiz = nodoIzquierdo
            arbol.raiz.padre = None

    # Obtener los hermanos cercanos a este Nodo
    #
    # retorna una tupla
    # (hermano izquierdo, hermano derecho, indice de separacion)
    # si un hermano no existe, entonce se retorna None, el indice de
    # separacion representa el indice de este nodo respecto al la lista
    # de los hijos del nodo padre
    def obtenerHermanos(self):
        if not self.padre:
            # la raiz no tiene hermanos
            return (None, None, 0)

        assert(self.padre.hijos)

        hermanoIzquierdo = None
        hermanoDerecho = None
        indice = 0

        for i, j in enumerate(self.padre.hijos):
            if j is self:
                if i != 0:
                    hermanoIzquierdo = self.padre.hijos[i - 1]
                if (i + 1) < len(self.padre.hijos):
                    hermanoDerecho = self.padre.hijos[i + 1]
                indice = i
                break

        return (hermanoIzquierdo, hermanoDerecho, indice)

    def obtenerListaCarpetas(self):
        listaCarpetas = self.carpetas
        if self.hijos:
            for hijo in self.hijos:
                listaCarpetas.extend(hijo.obtenerListaCarpetas())
        return listaCarpetas

class ArbolB(object):
    def __init__(self, orden):
        if orden <= 2:
            raise ValueError("El orden del Arbol B debe ser por lo minimo de 3")
        self.raiz = _NodoArbol()
        self.orden = orden
        self.maximoCarpetas = orden - 1
        self.minimoCarpetas = self.maximoCarpetas // 2
        self.altura = 1
        self.tamano = 0

    def __str__(self):
        return 'altura: %d items: %d m: %d raiz: %x' % (
                                    self.altura, self.tamano,
                                    self.maximoCarpetas + 1,
                                    id(self.raiz))

    def insertar(self, carpeta):
        # buscar un nodo hoja donde podemos agregar la carpeta
        # verificando si ya existe previamente
        found, nodo, slot = self.raiz.buscar(carpeta)
        if found:
            # si la carpeta ya existe, no se puede agregar 2 veces
            return False
        return nodo.insertar(self, carpeta, slot, None)

    def eliminar(self, carpeta):
        # primero buscamos la carpeta a eliminar
        print ("Carpeta a eliminar " + str(carpeta))
        found, nodo, slot = self.raiz.buscar(_Carpeta(str(carpeta)))
        if found:
            nodo.eliminar(self, carpeta, None)
            return True
        else:
            # la carpeta no existe por lo que no se puede eliminar
            print('la carpeta no existe')
            return False

    def renombrar(self, nombre_actual, nombre_nuevo):
        carpeta = self.buscarCarpeta(_Carpeta(nombre_actual))
        if carpeta is None:
            print("la carpeta no existe")
            return False
        else:
            nueva_carpeta = _Carpeta(nombre_nuevo)
            nueva_carpeta.carpetas = carpeta.carpetas
            nueva_carpeta.archivos = carpeta.archivos
            self.eliminar(carpeta)
            self.insertar(nueva_carpeta)
            return True

    #retorna True o False si la carpeta ha sido encontrada
    def buscar(self, carpeta):
        return self.raiz.buscar(carpeta)[0]

    #retorna la carpeta si ha sido encontrada de lo contrario retorna None
    def buscarCarpeta(self, carpeta):
        found, nodo, slot = self.raiz.buscar(carpeta)
        if found:
            return nodo.carpetas[slot]
        else:
            return None

    def min(self):
        return self.raiz.carpetaMenor()[0]

    def max(self):
        return self.raiz.carpetaMayor()[0]

    def obtenerListaCarpetas(self):
        return self.raiz.obtenerListaCarpetas()

    def generarDotNodo(self, raiz):
        """
        digraph structs {
            node [shape=record];
            struct1 [shape=record,label="<f0> left|<f1> middle|<f2> right"];
            struct2 [shape=record,label="<f0> one|<f1> two"];
            struct3 [shape=record,label="hello\nworld |{ b |{c|<here> d|e}| f}| g | h"];
            struct1:f1 -> struct2:f0;
            struct1:f2 -> struct3:here;
        }
        """
        nombreNodo = "struct" + str(id(raiz))
        etiquetaNodo = ""
        i = 0
        for carpeta in raiz.carpetas:
            if etiquetaNodo != "":
                etiquetaNodo += " | "
            etiquetaNodo += "<f" + str(i) + "> | " + carpeta.nombre
            i += 1
        etiquetaNodo += " | <f" + str(i) + ">"

        conexiones = ""
        cuerpo = '%s [label=\"%s\", shape=record];\n' % (nombreNodo, etiquetaNodo)
        j = 0
        if raiz.hijos is not None:
            for hijo in raiz.hijos:
                nombreHijo, etiquetaHijo, conexionesHijo, cuerpoHijo = self.generarDotNodo(hijo)
                cuerpo += cuerpoHijo
                cuerpo += nombreNodo + ":f" + str(j) + " -> " + nombreHijo + ":f0;\n";
                j += 1

        return (nombreNodo, etiquetaNodo, conexiones, cuerpo)

    def generarGraphviz(self):
        c=cmd()
        dotString = "digraph structs { \n"
        dotString += "node [shape=record];\n"
        nombreNodo, etiquetaNodo, conexiones, cuerpo = self.generarDotNodo(self.raiz)
        dotString += cuerpo
        dotString += "}"
        c.escribir_dot(dotString, "ArbolB")
        c.ejecutar_cmd("ArbolB")
        return dotString


if __name__ == '__main__':
    # mini test
    raiz = _Carpeta("/")

    raiz.agregarCarpeta(_Carpeta("ODFADF"))
    raiz.agregarCarpeta(_Carpeta("PDFADF"))
    raiz.agregarCarpeta(_Carpeta("ADFDAF"))
    raiz.agregarCarpeta(_Carpeta("ADFAD"))
    raiz.agregarCarpeta(_Carpeta("QDAFDFA"))
    raiz.agregarCarpeta(_Carpeta("MAFDAF"))
    raiz.agregarCarpeta(_Carpeta("ZAFADF"))
    raiz.agregarCarpeta(_Carpeta("BWWEREH"))
    raiz.agregarCarpeta(_Carpeta("DLJDFOIE"))
    raiz.agregarCarpeta(_Carpeta("YEIUROI"))
    raiz.agregarCarpeta(_Carpeta("DLJDFOIDFEWERE"))
    raiz.agregarCarpeta(_Carpeta("YEIUROIDFEWER"))
    raiz.agregarCarpeta(_Carpeta("DLJDFOSFDAIE"))
    raiz.agregarCarpeta(_Carpeta("YEIURODFADSFI"))
    raiz.agregarCarpeta(_Carpeta("MJKDIF"))
    raiz.renombrarCarpeta("MJKDIF","A")
    raiz.agregarCarpeta(_Carpeta("HEI;SI"))
    raiz.agregarCarpeta(_Carpeta("TIEURIW"))
    raiz.agregarCarpeta(_Carpeta("FFA"))

    raiz.agregarCarpeta(_Carpeta("TIWREWRWEEURIW"))
    raiz.agregarCarpeta(_Carpeta("FWERFA"))

    raiz.agregarCarpeta(_Carpeta("TIEERWERWURIW"))
    raiz.agregarCarpeta(_Carpeta("FFDAWERFA"))

    raiz.agregarCarpeta(_Carpeta("WOJDFK"))
    raiz.agregarCarpeta(_Carpeta("FDLSG"))
    raiz.agregarCarpeta(_Carpeta("KDDFA"))
    raiz.agregarCarpeta(_Carpeta("X"))
    raiz.agregarCarpeta(_Carpeta("XSEEEWEEEEE"))

    raiz.renombrarCarpeta("FFA","CASA")
    raiz.renombrarCarpeta("FFA","CASA")
    raiz.agregarCarpeta(_Carpeta("EDD"))
    raiz.renombrarCarpeta("EDD","CASAD")
    raiz.renombrarCarpeta("FDLSG","CASAD2")
    raiz.renombrarCarpeta("TIEERWERWURIW","PIRRURI")
    raiz.renombrarCarpeta("BWWEREH","hdha")

    print("-------")
    print("-------")
    print("------- Graficar ArbolB de la Raiz")
    print(raiz.graficarArbolB() )
    print("-------")
    