from ArbolAvl import ArbolAvl
from activo import activo
from Cmd import cmd
from subprocess import check_output
from random import choice
avl= ArbolAvl()
avl.agregar("mesa", "mesagrande", "a51")
avl.agregar("mesa", "mesagrande", "a74")
avl.agregar("silla", "silla" ,"b42")
avl.agregar("telefono", "cellular", "a17")
avl.agregar("cuaderno", "cua", "s60")
avl.agregar("desodo", "desodo", "a48")
avl.agregar("lampara", "lampara", "a98")
avl.agregar("carpa","carpa", "a90")
avl.agregar("adorno", "adorno", "a7")
avl.agregar("lapic", "b12", "A9")
avl.agregar("lana", "lana", "z10")
avl.agregar("lana", "lana", "z11")
avl.agregar("lana", "lana", "g10")
avl.agregar("holttta", "piedrareemprlazo", "a45")
avl.agregar("hola", "piedrareemplazo", "p90")

avl.reemplazo("piedrareemplazo", "hojas reemplazo","a51")
avl.reemplazo("ho", "ho","a74")
avl.reemplazo("ho", "ho","b42")
avl.borrar("lapic", "b12", "A9")
avl.borrar("lana", "lana", "z10")
print("----------------------------------")
#l=avl.listarActivos()
ll=avl.obter_activos()
print(ll)
print("----------------------------------")
#print (l.lista_comas())
