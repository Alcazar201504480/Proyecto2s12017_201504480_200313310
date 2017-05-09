import json
import listad
from flask import Flask, request, Response
app = Flask("EDD_Proyecto1")


class Usuario():
	global jj 
	global matriz_dispersa

	matriz_dispersa = listad.listad1()
	def algoUI():
		usuario= "mario"
		contra ="33"
		nombre ="dff df afdf  df a"
		empresa ="un"
		dep ="so"
		matriz_dispersa.agregar(usuario,contra,nombre,empresa,dep)

		usuario= "raul"
		contra ="22"
		nombre ="dff df afdf  df a"
		empresa ="u"
		dep ="soc"
		matriz_dispersa.agregar(usuario,contra,nombre,empresa,dep)

		usuario= "mariaogmail.com"
		contra ="1dffa d343"
		nombre ="2dff df afdf  eeef a"
		empresa ="united fruitt"
		dep ="sociales"
		matriz_dispersa.agregar(usuario,contra,nombre,empresa,dep)
		"matriz_dispersa.eliminar(gg[0],gg[1])"


		usuario= "agoariaogmail.com"
		contra ="dffa d343"
		nombre ="dff df afdf  df a"
		empresa ="united fruit"
		dep ="sociales"
		matriz_dispersa.agregar(usuario,contra,nombre,empresa,dep)
		"matriz_dispersa.eliminar(gg[0],gg[1])"


		usuario= "aa.com"
		contra ="dffa d343"
		nombre ="dff df afdf  df a"
		empresa ="united fruitt"
		dep ="social"
		matriz_dispersa.agregar(usuario,contra,nombre,empresa,dep)
		"matriz_dispersa.eliminar(gg[0],gg[1])"



		usuario= "zzz.com"
		contra ="dffa d343"
		nombre ="dff df afdf  df a"
		empresa ="united fruit"
		dep ="algo"
		matriz_dispersa.agregar(usuario,contra,nombre,empresa,dep)
		"matriz_dispersa.eliminar(gg[0],gg[1])"


		usuario= "df.com"
		contra ="dffa d343"
		nombre ="dff df afdf  df a"
		empresa ="zero"
		dep ="algo"
		matriz_dispersa.agregar(usuario,contra,nombre,empresa,dep)
		"matriz_dispersa.eliminar(gg[0],gg[1])"

		usuario= "fffrgrf"
		contra ="dffa d343"
		nombre ="dff df afdf  df a"
		empresa ="united fruitt"
		dep ="algo"
		matriz_dispersa.agregar(usuario,contra,nombre,empresa,dep)
		"matriz_dispersa.eliminar(gg[0],gg[1])"

		matriz_dispersa.buscar_user_agregar_activo("df.com","zero","algo","Nombre activo1","descripcion1")
		matriz_dispersa.buscar_user_agregar_activo("df.com","zero","algo","Nombre activo2","descripcion2")

		matriz_dispersa.buscar_user_agregar_activo("mario","un","so","Nombre activo3","descripcion3")
		matriz_dispersa.buscar_user_agregar_activo("marifogmail.com","united fruitt","sociales","Nombre activo4","descripcion4")

		matriz_dispersa.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo5","descripcion5")
		matriz_dispersa.buscar_user_agregar_activo("marifogmail.com","united fruitt","sociales","Nombre activo6","descripcion6")
		matriz_dispersa.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo7","descripcion7")
		matriz_dispersa.buscar_user_agregar_activo("marifogmail.com","united fruitt","sociales","Nombre activo8","descripcion8")
		matriz_dispersa.buscar_user_agregar_activo("mariogmail.com","united fruit","social","Nombre activo9","descripcion9")
		matriz_dispersa.buscar_user_agregar_activo("marifogmail.com","united fruitt","sociales","Nombre activo10","descripcion10")
		matriz_dispersa.buscar_user_agregar_activo("marifogmail.com","united fruitt","sociales","Nombre activo10","descripcion10")




	algoUI()	
	@app.route('/lista_agregar',methods=['POST'])
	def darvalor():
		usuario = str(request.form['usuario'])
		contra = str(request.form['contrasena']) 
		nombre = str(request.form['nombre'])
		empresa= str(request.form['empresa'])
		dep = str(request.form['departamento'])
		
		matriz_dispersa.agregar(usuario,contra,nombre,empresa,dep)
		return "Agregado usuario"

	@app.route('/lista_agregar_activo',methods=['POST'])
	def darvaloractivo():
		usuario = str(request.form['usuario'])
		empresa= str(request.form['empresa'])
		dep = str(request.form['departamento'])
		nombre_activo = str(request.form['activo'])
		descripcion = str(request.form['descripcion'])
		matriz_dispersa.buscar_user_agregar_activo(usuario,empresa,dep,nombre_activo,descripcion)
		return "Agregado activo"

	@app.route('/lista_comprobar',methods=['POST'])
	def darvalo():
		usuario = str(request.form['usuario'])
		contra= str(request.form['contra'])
		empre = str(request.form['empre'])
		depto = str(request.form['depto'])
		r=matriz_dispersa.comprobar_inicio(usuario,contra,empre,depto)
		return str(r)

	@app.route('/lista_modificar',methods=['POST'])
	def mod():
		usuario = str(request.form['usuario'])
		empresa= str(request.form['empresa'])
		dep = str(request.form['departamento'])
		num_unico =str(request.form['id_producto'])
		nombre =str(request.form['nombre_producto'])
		descripcion=str(request.form['descripcion_producto'])
		matriz_dispersa.buscar_user_modificar_activo(usuario,empresa,dep,num_unico,nombre,descripcion)
		return 	"editado"

	@app.route('/lista_eliminar',methods=['POST'])
	def elim():
		usuario = str(request.form['usuario'])
		empresa= str(request.form['empresa'])
		dep = str(request.form['departamento'])
		num_unico =str(request.form['id_producto'])
		nombre =str(request.form['nombre_producto'])
		descripcion=str(request.form['descripcion_producto'])
		matriz_dispersa.eliminar_activo(usuario,empresa,dep,num_unico,nombre,descripcion)
		return 	"eliminado"

	@app.route('/listar_activos',methods=['POST'])
	def todos():
		return 	matriz_dispersa.todos_activos()

	@app.route('/lista_activos_user',methods=['POST'])
	def algunos():
		usuario = str(request.form['usuario'])
		empresa= str(request.form['empresa'])
		dep = str(request.form['departamento'])

		return 	matriz_dispersa.ver_por_user2(usuario,empresa,dep)

	@app.route('/ver_grafica',methods=['POST'])
	def grafi():
		nada= str(request.form['dato1'])
		mandar = str(matriz_dispersa.graficarcompleto())
		return 	str(mandar)

	@app.route('/obtener_activos_datos',methods=['POST'])
	def obtt():
		return 	matriz_dispersa.todos_activos2()


	@app.route('/ver_grafica_dep',methods=['POST'])
	def grafi1(): 
		nada= str(request.form['dato1'])
		mandar = str(matriz_dispersa.ver_por_dep(nada))
		return 	str(mandar)

	@app.route('/ver_grafica_emp',methods=['POST'])
	def grafi11(): 
		nada= str(request.form['dato1'])
		mandar = str(matriz_dispersa.ver_por_emp(nada))
		return 	str(mandar)

	@app.route('/mandar_dep',methods=['POST'])
	def grafi112(): 
		nada= str(request.form['dato1'])
		mandar = str(matriz_dispersa.obtener_dep())
		return 	str(mandar)

	@app.route('/mandar_emp',methods=['POST'])
	def grafi1125(): 
		nada= str(request.form['dato1'])
		mandar = str(matriz_dispersa.obtener_emp())
		return 	str(mandar)

	@app.route('/mandar_user',methods=['POST'])
	def grafi11256(): 
		nada= str(request.form['dato1'])
		mandar = str(matriz_dispersa.obtener_user())
		return 	str(mandar)


	@app.route('/lista_comprobar_android',methods=['POST'])
	def darvaloracandroid():
		usuario = str(request.form['usuario'])
		contra= str(request.form['contra'])
		empre = str(request.form['empre'])
		depto = str(request.form['depto'])
		r=matriz_dispersa.comprobar_inicio(usuario, contra, empre, depto)
		return json.dumps({"usuario": r})

	@app.route('/listar_activos_android',methods=['POST'])
	def todosandroid():
		return 	json.dumps({"activos": matriz_dispersa.ver_por_user_todos()})

	@app.route('/obtener_avl',methods=['POST'])
	def algunos3():
		usuario = str(request.form['usuario'])
		empresa= str(request.form['empresa'])
		dep = str(request.form['departamento'])

		return 	matriz_dispersa.avl_pos(usuario,empresa,dep)

	@app.route('/lista_eliminar_1',methods=['POST'])
	def elsim():
		usuario = str(request.form['usuario'])
		empresa= str(request.form['empresa'])
		dep = str(request.form['departamento'])
		num_unico =str(request.form['id_producto'])
		nombre =str(request.form['nombre_producto'])
		descripcion=str(request.form['descripcion_producto'])
		matriz_dispersa.eliminar_activo(usuario,empresa,dep,num_unico,nombre,descripcion)
		return 	json.dumps({"success": 1})

	@app.route('/lista_agregar_activo_1',methods=['POST'])
	def darvaloractivo2():
		usuario = str(request.form['usuario'])
		empresa= str(request.form['empresa'])
		dep = str(request.form['departamento'])
		nombre_activo = str(request.form['activo'])
		descripcion = str(request.form['descripcion'])
		matriz_dispersa.buscar_user_agregar_activo(usuario,empresa,dep,nombre_activo,descripcion)
		return json.dumps({"success": 1})


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')