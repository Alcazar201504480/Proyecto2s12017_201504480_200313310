from user import User
from Cmd import cmd

class NodoD(object):
    def __init__(self, dato, ant, sig, usuario):
        self.dato = dato
        self.ant = ant
        self.sig = sig
        self.usuario=usuario


class ListaDoble(object):
    inicio = None
    fin = None
    size = 0

    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def esvacia(self):
        return self.inicio is None

    def getsize(self):
        return self.size

    def insertarinicio(self, val, user):
        n = NodoD(val, None, None, user)
        if self.inicio is None:
            self.inicio = n
            self.fin = self.inicio
        else:
            self.inicio.ant = n
            n.sig = self.inicio
            self.inicio = n

    def insertaralfin(self, val, user):
        n = NodoD(val, None, None, user)
        if self.inicio is None:
            self.inicio = n
            self.fin = self.inicio
        else:
            n.ant = self.fin
            self.fin.sig = n
            self.fin = n
        self.size += 1

    def eliminaval(self, valor):
        if self.inicio is not None:
            aux = self.inicio
            ant = None
            while aux is not None:
                if aux.dato == valor:
                    if ant is None:
                        self.inicio = self.inicio.sig
                        aux.sig = None
                        aux = self.inicio
                    else:
                        ant.sig = aux.sig
                        aux.sig = None
                        aux = ant.sig
                else:
                    ant = aux
                    aux = aux.sig

    def buscar(self, valor):
        existe = False
        aux = self.inicio
        while aux is not None and not existe:
            if aux.dato == valor:
                existe = True
            aux = aux.sig
        return existe

    def obtener(self, valor):
        existe = False
        temp = None
        aux = self.inicio
        while aux is not None and not existe:
            if aux.dato == valor:
                temp = aux
                existe = True
            aux = aux.sig
        return temp

    def verificar_login(self, email, contra):
        existe = ''
        user = self.obtener(email)
        if user is not None:
            if user.usuario.contra == contra:
                existe='ingreso'
            else:
                existe = 'La contrasena es incorrecta, intentelo de nuevo'
        else:
            existe = 'No existe el Usuario'
        return existe

    def modificar(self, valor, nombre, user):
        if self.inicio is not None:
            aux = self.inicio
            cont = 0
            while aux is not None:
                if aux.dato == valor:
                    aux.dato = nombre
                    aux.usuario=user
                    return
                else:
                    cont += 1
                    aux = aux.sig

    def mostrarhaciadelante(self):
        nodo_actual = self.inicio
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.sig
        print("*"*50)

    def mostrarhaciatras(self):
        nodo_actual = self.fin
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.ant
        print("*"*50)

    def grafico(self):
        cadena=""
        cadena=cadena + "digraph g{"
        aux=self.inicio
        valor = 1
        while aux is not None:
            if aux is not None and aux.sig is not None:
                cadena=cadena+("t"+str(valor)+"-> t"+str(valor+1)+";")
                cadena=cadena+("t"+str(valor+1)+"-> t"+str(valor)+";")
                cadena=cadena+("t"+str(valor)+"[label=\""+str(aux.dato)+"\"];")
                cadena=cadena+("t"+str(valor+1)+"[label=\""+str(aux.sig.dato)+"\"];")
            if aux==self.fin:
                cadena=cadena+("t"+str(valor)+"[label=\""+str(aux.dato)+"\"]")
            aux=aux.sig
            valor+=1
        cadena=cadena+"}"
        return cadena

    def graficar(self):
        c = cmd()
        cadena = self.grafico()
        c.escribir_dot(cadena, "doble")
        c.ejecutar_cmd("doble")



#from listadoble import ListaDoble
d = ListaDoble()

#insertar un usuario de pruebas
uk = User()
uk.email = "earevalo"
uk.contra = "earevalo"
uk.nombre = "Estuardo"
uk.apellido = "Arevalo"
uk.naci = "nop"
d.insertarinicio(uk.email, uk)

class ManejoUsuario:
    def agregar_usuario(self, nombre, apellido, email, contra, naci):
        u = User()
        u.email = email
        u.contra = contra
        u.nombre = nombre
        u.apellido = apellido
        u.naci = naci
        d.insertarinicio(email, u)
        print("Ingresado-> "+u.email)

    def verificar_login(self, email, pword):
        return d.verificar_login(email, pword)

    def listar_usuarios(self):
        d.mostrarhaciadelante()

    def graficar(self):
        d.graficar()

    def stringgraficar(self):
        print(d.grafico())

    def obtenerUsuario(self, email):
        return d.obtener(email)


class pruebas:
    def probartodo(self):
        print('?'+str(d.esvacia()))
        us = User()
        us.email = 'que bueno'
        us.contra = 'contra'
        d.insertarinicio(5, us)
        d.insertarinicio(6, us)
        d.insertarinicio(50, us)
        d.insertarinicio(30, us)

        print('---------------------------------')
        print(d.verificar_login(6, 'contra'))
        print(d.verificar_login(50, 'con'))
        print(d.verificar_login('53', 'con'))
        print('---------------------------------')
        print(str(d.obtener(5).usuario.email))
        print(str(d.buscar(6)))
        print(str(d.buscar(50)))
        print(str(d.buscar(30)))
        print(str(d.obtener(3)))
        d.mostrarhaciadelante()

        d.eliminaval(50)
        d.eliminaval(5)
        d.eliminaval(30)
        d.eliminaval(6)

        print(str(d.buscar(5)))
        print(str(d.buscar(6)))
        print(str(d.buscar(50)))
        print(str(d.buscar(30)))
        d.mostrarhaciadelante()

        d.insertaralfin(5, us)
        d.insertaralfin(6, us)
        d.insertaralfin(50, us)
        d.insertaralfin(30, us)

        d.mostrarhaciadelante()

        d.modificar(50, 45, us)
        d.mostrarhaciadelante()
        print(d.grafico())
        ma = ManejoUsuario()
        ma.agregar_usuario('Miguel', 'Ruano', 'miguelruano@gmail.com','hello', '2017')
        d.graficar()
        print('?'+str(d.esvacia()))

def ok():
    manejador = ManejoUsuario()
    usuario = "earevalo"
    password = "earevalo"
    path = "/"
    nombreCarpeta = "ADFDAF"
    nuevoNombre = "ggg"
    auth = manejador.verificar_login(usuario, password)
    if auth == 'ingreso':
        u = manejador.obtenerUsuario(usuario)
        carpeta = None
        if path == "/": #insertar en la raiz
            carpeta = u.usuario.raizDrive
        else:
            carpeta = u.usuario.raizDrive.buscarCarpetaPorPath(path)

        if carpeta is not None:
            print("Carpeta a buscar = " + str(carpeta))
            print("Nombre Actual = " + nombreCarpeta)
            print("Nuevo nombre = " + nuevoNombre)
            print(u.usuario.raizDrive.graficarArbolB())
            if carpeta.renombrarCarpeta(nombreCarpeta,nuevoNombre):
                print("success")
            else:
                print("Carpeta no encontrada")
        else:
            print("Path no encontrado")
    else:
        print(auth)

ok()
