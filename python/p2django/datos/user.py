from datos.ArbolB import _Carpeta

class User:
    nombre = None
    apellido = None
    email = None
    contra = None
    naci = None
    raizDrive = None

    def __init__(self):
        self.email= None
        self.contra= None
        self.nombre = None
        self.apellido = None
        self.naci = None
        self.raizDrive = _Carpeta("/")
