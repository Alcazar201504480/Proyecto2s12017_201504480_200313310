import os
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import mimetypes
from urllib.request import pathname2url
# Create your views here.
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, FileUploadParser, FormParser, MultiPartParser
from datos.ArbolB import _Carpeta
from datos.listadoble import ManejoUsuario

manejador = ManejoUsuario()

@api_view(['GET'])
def index(request):
    return Response({"funcionando": "todo funcionando sin problema"})

@api_view(['POST'])
def login(request):
    usuario = request.data['usuario']
    password = request.data['password']
    auth = manejador.verificar_login(usuario, password)
    if auth == 'ingreso':
        u = manejador.obtenerUsuario(usuario)
        return Response(UsuarioSerializer(u.usuario).data)  #({"usuario": ""+ UsuarioSerializer(u.usuario).data +"", "data": request.data})
    else:
        return Response({"error": ""+ auth + "", "data": request.data})


@api_view(['GET'])
def obtener_dot_carpetas(request):
    raizDrive.agregarCarpeta(_Carpeta("O"))
    rs = IndexResponse(raizDrive.graficarArbolB())
    serializer = IndexResponseSerializer(rs)
    return Response(serializer.data)

@api_view(['POST'])
def obtener_directorio_usuario(request):
    # manejador = ManejoUsuario()
    usuario = request.data['usuario']
    password = request.data['password']
    path = request.data['path']
    auth = manejador.verificar_login(usuario, password)
    if auth == 'ingreso':
        u = manejador.obtenerUsuario(usuario)
        carpetaRaiz = u.usuario.raizDrive
        if path == "/": #insertar en la raiz
            carpetaRaiz = u.usuario.raizDrive
        else:
            carpetaRaiz = u.usuario.raizDrive.buscarCarpetaPorPath(path)

        if carpetaRaiz is not None:
            clist = carpetaRaiz.obtenerListaCarpetas()
            uCarpetas = {}
            if (len(clist)):
                i = 0
                for carpeta in clist:
                    uCarpetas[i] = CarpetaArchivo(carpeta.nombre)
                    i += 1

            alist = carpetaRaiz.archivos.listarActivos()
            uArchivos = {}
            if (len(alist)):
                i = 0
                for archivo in alist:
                    uArchivos[i] = CarpetaArchivo(archivo.codigo)
                    i += 1

            serializer = DirectorioSerializer({ "carpetas" : uCarpetas.values(), "archivos" : uArchivos.values() })
            return Response(serializer.data)
        else:
            serializer = DirectorioSerializer({ "carpetas" : None, "archivos" : None })
            return Response(serializer.data)
    else:
        return Response({"error": ""+ auth + "", "data": request.data})


@api_view(['POST'])
def crear_carpeta_usuario(request):
    # manejador = ManejoUsuario()
    usuario = request.data['usuario']
    password = request.data['password']
    path = request.data['path']
    nombreCarpeta = request.data['nombreCarpeta']
    auth = manejador.verificar_login(usuario, password)
    if auth == 'ingreso':
        u = manejador.obtenerUsuario(usuario)
        carpeta = None
        if path == "/": #insertar en la raiz
            carpeta = u.usuario.raizDrive
        else:
            carpeta = u.usuario.raizDrive.buscarCarpetaPorPath(path)

        if carpeta is not None:
            carpeta.agregarCarpeta(_Carpeta(nombreCarpeta))
            return Response({"success": 1})
        else:
            return Response({"error": "Path no encontrado", "data": request.data})
    else:
        return Response({"error": ""+ auth + "", "data": request.data})

@api_view(['POST'])
def renombrar_carpeta_usuario(request):
    # manejador = ManejoUsuario()
    usuario = request.data['usuario']
    password = request.data['password']
    path = request.data['path']
    nombreCarpeta = request.data['nombreCarpeta']
    nuevoNombre = request.data['nuevoNombre']
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
                return Response({"success": 1})
            else:
                return Response({"error": "Carpeta no encontrada", "data": request.data})
        else:
            return Response({"error": "Path no encontrado", "data": request.data})
    else:
        return Response({"error": ""+ auth + "", "data": request.data})

@api_view(['POST'])
def eliminar_carpeta_usuario(request):
    # manejador = ManejoUsuario()
    usuario = request.data['usuario']
    password = request.data['password']
    path = request.data['path']
    nombreCarpeta = request.data['nombreCarpeta']
    auth = manejador.verificar_login(usuario, password)
    if auth == 'ingreso':
        u = manejador.obtenerUsuario(usuario)
        carpeta = None
        if path == "/": #insertar en la raiz
            carpeta = u.usuario.raizDrive
        else:
            carpeta = u.usuario.raizDrive.buscarCarpetaPorPath(path)

        if carpeta is not None:
            if carpeta.eliminarCarpeta(nombreCarpeta):
                return Response({"success": 1})
            else:
                return Response({"error": "Carpeta no encontrada", "data": request.data})
        else:
            return Response({"error": "Path no encontrado", "data": request.data})
    else:
        return Response({"error": ""+ auth + "", "data": request.data})



@api_view(['POST'])
def renombrar_archivo_usuario(request):
    # manejador = ManejoUsuario()
    usuario = request.data['usuario']
    password = request.data['password']
    path = request.data['path']
    nombreArchivo = request.data['nombreArchivo']
    nuevoNombre = request.data['nuevoNombre']
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
            print("Nombre Actual = " + nombreArchivo)
            print("Nuevo nombre = " + nuevoNombre)
            print(u.usuario.raizDrive.graficarArbolB())
            carpeta.renombrarArchivo(nombreArchivo,nuevoNombre)
            return Response({"success": 1})
            #else:
            #    return Response({"error": "Archivo no encontrado", "data": request.data})
        else:
            return Response({"error": "Path no encontrado", "data": request.data})
    else:
        return Response({"error": ""+ auth + "", "data": request.data})

@api_view(['POST'])
def eliminar_archivo_usuario(request):
    # manejador = ManejoUsuario()
    usuario = request.data['usuario']
    password = request.data['password']
    path = request.data['path']
    nombreArchivo = request.data['nombreArchivo']
    auth = manejador.verificar_login(usuario, password)
    if auth == 'ingreso':
        u = manejador.obtenerUsuario(usuario)
        carpeta = None
        if path == "/": #insertar en la raiz
            carpeta = u.usuario.raizDrive
        else:
            carpeta = u.usuario.raizDrive.buscarCarpetaPorPath(path)

        if carpeta is not None:
            carpeta.eliminarArchivo(nombreArchivo)
            return Response({"success": 1})
            # else:
            #     return Response({"error": "Archivo no encontrado", "data": request.data})
        else:
            return Response({"error": "Path no encontrado", "data": request.data})
    else:
        return Response({"error": ""+ auth + "", "data": request.data})


@api_view(['POST'])
def descargar_archivo_usuario(request):
    # manejador = ManejoUsuario()
    usuario = request.data['usuario']
    password = request.data['password']
    path = request.data['path']
    nombreArchivo = request.data['nombreArchivo']
    auth = manejador.verificar_login(usuario, password)
    if auth == 'ingreso':
        u = manejador.obtenerUsuario(usuario)
        carpeta = None
        if path == "/": #insertar en la raiz
            carpeta = u.usuario.raizDrive
        else:
            carpeta = u.usuario.raizDrive.buscarCarpetaPorPath(path)

        if carpeta is not None:
            f = carpeta.buscarArchivoPorNombre(nombreArchivo)
            if f is not None:
                if f.dato.file is not None:
                    print(len(f.dato.file))
                    url = pathname2url(f.dato.codigo)
                    internal_path = default_storage.save(f.dato.codigo, ContentFile(f.dato.file.read())) 
                    file_path = os.path.join(settings.MEDIA_ROOT, f.dato.codigo)
                    if os.path.exists(file_path):
                        with open(file_path, 'rb') as fh:
                            response = HttpResponse( fh.read() , content_type=mimetypes.guess_type(url)[0])
                            response['Content-Disposition'] = 'inline; filename=' + f.dato.codigo
                            return response
                    else:
                        return Response({"error": "No se pudo escribir a disco", "data": request.data})
                else:
                    return Response({"error": "No hay Archivo guardado", "data": request.data})
            else:
                return Response({"error": "Archivo no encontrado", "data": request.data})
        else:
            return Response({"error": "Path no encontrado", "data": request.data})
    else:
        return Response({"error": ""+ auth + "", "data": request.data})




@api_view(['PUT'])
@parser_classes((MultiPartParser,FileUploadParser,))
def crear_archivo_usuario(request):
    f = request.data['filed']
    print ('subir archivo')
    print(f.name)
    print(len(f))
    internal_path = default_storage.save(f.name, ContentFile(f.read())) 
    print(internal_path)
    usuario = request.data['usuario']
    password = request.data['password']
    print(password)
    path = request.data['path']
    nombreArchivo = f.name #request.data['nombreArchivo']
    auth = manejador.verificar_login(usuario, password)
    if auth == 'ingreso':
        u = manejador.obtenerUsuario(usuario)
        carpeta = None
        if path == "/": #insertar en la raiz
            carpeta = u.usuario.raizDrive
        else:
            carpeta = u.usuario.raizDrive.buscarCarpetaPorPath(path)

        if carpeta is not None:
            carpeta.agregarArchivo(nombreArchivo, f)
            return Response({"success": 1}, status=status.HTTP_201_CREATED, content_type = "application/json")
            #return Response({"success": 1}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Path no encontrado", "data": request.data}, content_type = "application/json")
    else:
        return Response({"error": ""+ auth + "", "data": request.data}, content_type = "application/json")


#modelView para respuestas
class CarpetaArchivo(object):
    nombre = None
    def __init__(self, nombre):
        self.nombre = nombre

#serializadores

class CarpetaArchivoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)

class DirectorioSerializer(serializers.Serializer):
    carpetas = CarpetaArchivoSerializer(many=True)  # A nested list of 'edit' items.
    archivos = CarpetaArchivoSerializer(many=True)  # A nested list of 'edit' items.

class UsuarioSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=200)
    apellido = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    contra = serializers.CharField(max_length=200)
    naci = serializers.CharField(max_length=200)
