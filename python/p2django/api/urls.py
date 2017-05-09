from django.conf.urls import url

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dot/', views.obtener_dot_carpetas, name='obtener_dot_carpetas'),
    url(r'^login/', views.login, name='login'),
    url(r'^directorio_usuario/', views.obtener_directorio_usuario, name='directorio_usuario'),
    url(r'^crear_carpeta_usuario/', views.crear_carpeta_usuario, name='crear_carpeta_usuario'),
    url(r'^renombrar_carpeta_usuario/', views.renombrar_carpeta_usuario, name='renombrar_carpeta_usuario'),
    url(r'^eliminar_carpeta_usuario/', views.eliminar_carpeta_usuario, name='eliminar_carpeta_usuario'),
    url(r'^crear_archivo_usuario/', views.crear_archivo_usuario, name='crear_archivo_usuario'),
    url(r'^renombrar_archivo_usuario/', views.renombrar_archivo_usuario, name='renombrar_archivo_usuario'),
    url(r'^eliminar_archivo_usuario/', views.eliminar_archivo_usuario, name='eliminar_archivo_usuario'),
    url(r'^descargar_archivo_usuario/', views.descargar_archivo_usuario, name='descargar_archivo_usuario'),

    #url(r'^upload/(?P<filename>[^/]+)$', views.FileUploadView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)