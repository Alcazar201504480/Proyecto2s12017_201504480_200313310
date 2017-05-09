import subprocess
from os.path import expanduser
from subprocess import check_output

class cmd:
    def __init__(self):
        dato=None

    def escribir_dot(self, entrada, nombre_archivo):
        home = expanduser("~")
        f=open(home + "/" + nombre_archivo+".txt","wb")
        entrada += "\n"
        # print(entrada)
        entrada = entrada.encode()
        newFileByteArray = bytearray(entrada)
        f.write(newFileByteArray)

    def ejecutar_cmd(self, nombre_archivo):
        home = expanduser("~")
        lista = ["dot", "-Tpng", home + "/" + nombre_archivo+".txt", "-o", home + "/" + nombre_archivo+".png"]
        proc = subprocess.Popen(lista, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
        check_output("cd ~", shell=True).decode()
