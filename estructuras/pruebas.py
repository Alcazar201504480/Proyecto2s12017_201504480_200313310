import matriz
import tabla_hash
listad = matriz.matriz()
#listad.agregar(g[0],g[1])
anno ="2003"
mes ="1"
dia="11"
#listad.agregar(anno,mes,dia)
listad.agregar_cor(anno,mes,dia,"nombre56","descripcion","fecha","hora")

anno ="2003"
mes ="1"
dia ="11"
#listad.agregar(anno,mes,dia)
listad.agregar_cor(anno,mes,dia,"nombre12","descripcion12","fecha12","hora1")
listad.agregar_cor(anno,mes,dia,"nombre13","descripcion13","fecha13","hora12")
listad.agregar_cor(anno,mes,dia,"nombre14","descripcion14","fecha14","hora14")
listad.agregar_cor(anno,mes,dia,"nombre15","descripcion15","fecha15","hora15")
listad.agregar_cor(anno,mes,dia,"nombre16","descripcion16","fecha16","hora16")

#listad.eliminar_arbol_b(anno,mes,dia,"nombre1")

anno ="2003"
mes ="1"
dia ="11"
#listad.modificar_arbol_b("anno_viejo","mes__viejo","dia_viejo","nombre_viejo","anno_n","mes_n","dia_n","nombre_n","descripcion","fecha","hora")
listad.modificar_arbol_b(anno,mes,dia,"nombre1","anno_n","mes_n","dia_n","nombre_n","descripcion","fecha","hora")
print ("---"+listad.consultar_eventos_dia(anno,mes,dia))



"""
anno ="Agosto"
mes ="10"
dia ="15"
listad.agregar(anno,mes,dia)

t = tabla_hash.TablaHash(1000)

if (listad.buscar_dia_agregar_hash("dia","mes","año","nombre","descripcion","fecha","hora")):
	pass
else:	
	anno ="ato"
	mes ="mes"
	dia ="dia"
	listad.agregar(anno,mes,dia)	"""





#comprobar la contrasena debulve true o false (usuario,contra,empresa,dep)
print("contrasena:",listad.comprobar_inicio("mariogmailcom","1dffa d343","united fruit","social"))

listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")

listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")


listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")
listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")


listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")
listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")


listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")
listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")


listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")
listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")


listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")
listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")


listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")
listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")

"""listad.graficarcompleto()
listad.buscar_user_modificar_activo("mariaogmail.com","united fruitt","sociales","777","Nombre","descripcion")
listad.eliminar_activo("mariaogmail.com","united fruitt","sociales","777","Nombre","descripcion")
print(listad.todos_activos())
print(listad.ver_por_user("marifogmail.com","united fruitt","sociales"))"""
#listad.buscar_user("mariaogmail.com","united fruitt","sociales")

print(listad.ver_por_user("marifogmail.com","united fruitt","sociales"))

print (listad.obtener_dep())
listad.buscar_user_modificar_activo("mariogmail.com","united fruit","social","777","Nombmihugrre","mihurldescripcion")
listad.graficarcompleto()

#print("-------------------")
#print(listad.ver_por_user_todos())

#listad.agregar(g[0],g[1])



"""
ñ

#comprobar la contrasena debulve true o false (usuario,contra,empresa,dep)
print("contrasena:",listad.comprobar_inicio("mariogmail.com","1dffa d343","united fruit","social"))

listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")

listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")


listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")
listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")


listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")
listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")


listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")
listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")


listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")
listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")


listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")
listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo1","descripcion1")


listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")
listad.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo3","descripcion3")

"""
"""listad.graficarcompleto()
listad.buscar_user_modificar_activo("mariaogmail.com","united fruitt","sociales","777","Nombre","descripcion")
listad.eliminar_activo("mariaogmail.com","united fruitt","sociales","777","Nombre","descripcion")
print(listad.todos_activos())
print(listad.ver_por_user("marifogmail.com","united fruitt","sociales"))"""
#listad.buscar_user("mariaogmail.com","united fruitt","sociales")

#print(listad.ver_por_user("marifogmail.com","united fruitt","sociales"))

#print (listad.obtener_dep())
#listad.buscar_user_modificar_activo("mariogmail.com","united fruit","social","777","Nombmihugrre","mihurldescripcion")
#listad.graficarcompleto()
"""
print("-------------------")
print(listad.ver_por_user_todos())
"""