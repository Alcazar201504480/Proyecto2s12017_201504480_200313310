from ArbolB import _Carpeta

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
        self.raizDrive.agregarCarpeta(_Carpeta("ODFADF"))
        self.raizDrive.agregarCarpeta(_Carpeta("PDFADF"))
        self.raizDrive.agregarCarpeta(_Carpeta("ADFDAF"))
        self.raizDrive.agregarCarpeta(_Carpeta("ADFAD"))
        self.raizDrive.agregarCarpeta(_Carpeta("QDAFDFA"))
        self.raizDrive.agregarCarpeta(_Carpeta("MAFDAF"))
        self.raizDrive.agregarCarpeta(_Carpeta("ZAFADF"))
        self.raizDrive.agregarCarpeta(_Carpeta("BWWEREH"))
        self.raizDrive.agregarCarpeta(_Carpeta("DLJDFOIE"))
        self.raizDrive.agregarCarpeta(_Carpeta("YEIUROI"))
        self.raizDrive.agregarCarpeta(_Carpeta("DLJDFOIDFEWERE"))
        self.raizDrive.agregarCarpeta(_Carpeta("YEIUROIDFEWER"))
        self.raizDrive.agregarCarpeta(_Carpeta("DLJDFOSFDAIE"))
        self.raizDrive.agregarCarpeta(_Carpeta("YEIURODFADSFI"))
        self.raizDrive.agregarCarpeta(_Carpeta("MJKDIF"))
        self.raizDrive.renombrarCarpeta("MJKDIF","A")
        self.raizDrive.agregarCarpeta(_Carpeta("HEI;SI"))
        self.raizDrive.agregarCarpeta(_Carpeta("TIEURIW"))
        self.raizDrive.agregarCarpeta(_Carpeta("FFA"))

        self.raizDrive.agregarCarpeta(_Carpeta("TIWREWRWEEURIW"))
        self.raizDrive.agregarCarpeta(_Carpeta("FWERFA"))

        self.raizDrive.agregarCarpeta(_Carpeta("TIEERWERWURIW"))
        self.raizDrive.agregarCarpeta(_Carpeta("FFDAWERFA"))

        self.raizDrive.agregarCarpeta(_Carpeta("WOJDFK"))
        self.raizDrive.agregarCarpeta(_Carpeta("FDLSG"))
        self.raizDrive.agregarCarpeta(_Carpeta("KDDFA"))
        self.raizDrive.agregarCarpeta(_Carpeta("X"))
        self.raizDrive.agregarCarpeta(_Carpeta("XSEEEWEEEEE"))

        self.raizDrive.renombrarCarpeta("FFA","CASA")
        self.raizDrive.renombrarCarpeta("FFA","CASA")
        self.raizDrive.agregarCarpeta(_Carpeta("EDD"))
        self.raizDrive.renombrarCarpeta("EDD","CASAD")
        self.raizDrive.renombrarCarpeta("FDLSG","CASAD2")
        self.raizDrive.renombrarCarpeta("TIEERWERWURIW","PIRRURI")
        self.raizDrive.renombrarCarpeta("BWWEREH","hdha")

        print(self.raizDrive.graficarArbolB())

