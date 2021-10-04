import json
import time

import EDD.avl
from analyzers.Syntactic import parser
from analyzers.Syntactic import user_list, task_list
from flask import Flask, json, request, jsonify
from EDD.avl import AVL
from EDD.ListaDobleGeneral import listaDoble
from EDD.ArbolB.ArbolB import arbolB
from EDD.matrizDispersa import matrizD


# Press the green button in the gutter to run the script.

app = Flask(__name__)
BtreeCursosGene = arbolB()
arbolAVL = AVL()
f = open("Estudiantes.txt", "r", encoding="utf-8")
mensaje = f.read()
f.close()
parser.parse(mensaje)
aux = user_list.First
while aux is not None:
    arbolAVL.insert(int(aux.Carnet), aux.DPI, aux.Nombre, aux.Carrera, aux.Correo, aux.Password, int(aux.Creditos), int(aux.Edad),None)
    aux = aux.Next

#arbolAVL.preorden()






@app.route('/carga',methods=['POST'])
def carga():

    ruta=request.json['path']
    tipo=request.json['tipo']
    if tipo == "estudiante":
        with open(ruta,encoding="utf-8") as file:
            info=json.load(file)
            for estudiante in info['Estudiantes']:
                if arbolAVL.seek(arbolAVL.root,int(estudiante['Carnet'])):
                    print("--------------------------------------")
                    print( "Estudiante: " + arbolAVL.seek(arbolAVL.root,int(estudiante['Carnet'])).nombre)
                    listaAños = listaDoble()
                    for año in estudiante['Años']:
                        print("Estamos en año: " + año['Año'])
                        listaSemes = listaDoble()
                        listaMeses = listaDoble()

                        for semes in año['Semestres']:
                            matrizDx = matrizD()
                            BtreeCursosEstu = arbolB()
                            listaTareas=listaDoble()
                            print("Estamos en semestre: " + semes['Semestre'])
                            for cursos in semes['Cursos']:
                                BtreeCursosEstu.insertarDatos(int(cursos['Codigo']),cursos['Nombre'],cursos['Creditos'],cursos['Prerequisitos'],cursos['Obligatorio'])
                                aux2 = task_list.First
                                while aux2 is not None:
                                    if int(aux2.Carnet) == int(estudiante['Carnet']):
                                        listaTareas.add_Tareas(int(aux2.Carnet),aux2.Nombre,aux2.Descripcion,aux2.Materia,aux2.Fecha,aux2.Hora,aux2.Estado)
                                    matrizDx.insertar(listaTareas,aux2.Fecha[0:2],aux2.Hora)
                                    aux2=aux2.Next


                            print("Se va agregar en semestre: "+ str(semes['Semestre']))
                            listaSemes.add_Semestres(semes['Semestre'], BtreeCursosEstu)
                        listaAños.add_Años(año['Año'], listaSemes, None)
                    arbolAVL.seek(arbolAVL.root, int(estudiante['Carnet'])).listAños = listaAños
                else:
                    print ("Carnet no encontrado en los estudiantes cargados en .txt, revisa tus datos por favor.")
            return "¡Estudiantes cargados exitosamente!"



    elif tipo=="recordatorio":
        f = open(ruta, "r", encoding="utf-8")
        mensaje = f.read()
        f.close()
        parser.parse(mensaje)

    elif tipo == "curso":
        with open(ruta,encoding="utf-8") as file:
            info=json.load(file)
            for cursos in info['Cursos']:
                BtreeCursosGene.insertarDatos(int(cursos['Codigo']), cursos['Nombre'], cursos['Creditos'],cursos['Prerequisitos'], cursos['Obligatorio'])
        return "¡Cursos del pensum cargados exitosamente!"
    return ""


@app.route('/reporte',methods=['GET'])
def generarReportes():
    tipo=request.json['tipo']
    if tipo == "0":
        arbolAVL.generar()
        return "¡Reporte de estudiantes generado con exito!"
    elif tipo == "1":
        pass
    elif tipo == "2":
        pass
    elif tipo == "3":
        BtreeCursosGene.graficar("GENERAL")
        return "¡Reporte general de cursos de pensum generado con exito!"
    elif tipo == "4":
        carnet=request.json['carnet']
        año = request.json['año']
        semestre = request.json['semestre']
        if arbolAVL.seek(arbolAVL.root, int(carnet)):
            aux = arbolAVL.seek(arbolAVL.root, int(carnet)).listAños.cabeza
            while (aux is not None):
                if año == aux.año:
                    print("Estamos en año: " + aux.año)
                    aux2 = aux.listaSemes.cabeza
                    while aux2 is not None:
                        if semestre == aux2.nSemestre:
                            print("Estamos en Semestre: " + aux2.nSemestre)
                            aux2.arbolCursos.graficar("_SEMESTRE_"+semestre+"_AÑO_"+año)
                            return "¡Reporte de cursos de estudiante especifico generado con exito!"
                        aux2 = aux2.siguiente
                aux = aux.siguiente
        else:
            return "Carnet no encontrado, revisa tus datos por favor."

    return ""

@app.route('/estudiante',methods=['GET','POST','PUT'])
def manualEstudiante():
    if request.method == 'POST':
        carnet = request.json['carnet']
        dpi = request.json['DPI']
        nombre = request.json["nombre"]
        carrera = request.json["carrera"]
        correo = request.json["correo"]
        passw = request.json["password"]
        creditos = request.json["creditos"]
        edad = request.json["edad"]
        arbolAVL.insert(int(carnet),dpi,nombre,carrera,correo,passw,int(creditos),int(edad))
        return "¡Estudiante agregado de manera manual exitosamente!"
    elif request.method == 'GET':
        carnet = request.json['carnet']
        encontrado=arbolAVL.seek(arbolAVL.root,int(carnet))
        if encontrado:
            return jsonify({
                'carnet':encontrado.nCarnet,
                'DPI':encontrado.dpi,
                'nombre': encontrado.nombre,
                'carrera': encontrado.carrera,
                'correo': encontrado.correo,
                'password': encontrado.password,
                'creditos': encontrado.creditos,
                'edad': encontrado.edad
            })
        else:
            return "Estudiante no encontrado, revisa tus datos por favor."
    else:
        carnet = request.json['carnet']
        dpi = request.json['DPI']
        nombre = request.json["nombre"]
        carrera = request.json["carrera"]
        correo = request.json["correo"]
        passw = request.json["password"]
        creditos = request.json["creditos"]
        edad = request.json["edad"]
        if arbolAVL.seek(arbolAVL.root, int(carnet)):
            arbolAVL.seek(arbolAVL.root, int(carnet)).nCarnet = int(carnet)
            arbolAVL.seek(arbolAVL.root,int(carnet)).dpi=dpi
            arbolAVL.seek(arbolAVL.root, int(carnet)).nombre = nombre
            arbolAVL.seek(arbolAVL.root, int(carnet)).carrera = carrera
            arbolAVL.seek(arbolAVL.root, int(carnet)).correo = correo
            arbolAVL.seek(arbolAVL.root, int(carnet)).password = passw
            arbolAVL.seek(arbolAVL.root, int(carnet)).creditos = int(creditos)
            arbolAVL.seek(arbolAVL.root, int(carnet)).edad = int(edad)
            return "¡Estudiante actualizado con exito!"
        else:
            return "Estudiante no encontrado, revisa tus datos por favor."

@app.route('/cursosPensum',methods=['POST'])
def manualCursosPensum():
    arregloCursos = request.json['Cursos']
    for i in arregloCursos:
        BtreeCursosGene.insertarDatos(int(i['Codigo']),i['Nombre'],int(i['Creditos']),i['Prerequisitos'],str(i['Obligatorio']))
    return "¡Curso agregado con exito al arbol B general de cursos!"



@app.route ('/prueba')
def canche():
    print("aaaaaaaaaaa2backend")
    return "Probando el flask"



if __name__ == '__main__':
    app.run(debug=True, port=5000)


