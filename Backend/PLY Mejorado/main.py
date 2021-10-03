import json
import time

import EDD.avl
from analyzers.Syntactic import parser
from analyzers.Syntactic import user_list, task_list
from flask import Flask, request
from EDD.avl import AVL
from EDD.ListaDobleGeneral import listaDoble
from EDD.ArbolB.ArbolB import arbolB


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
    arbolAVL.insert(int(aux.Carnet), aux.DPI, aux.Nombre, aux.Carrera, aux.Correo, aux.Password, int(aux.Creditos), aux.Edad,None)
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
                        for semes in año['Semestres']:
                            BtreeCursosEstu = arbolB()
                            print("Estamos en semestre: " + semes['Semestre'])
                            for cursos in semes['Cursos']:
                                BtreeCursosEstu.insertarDatos(int(cursos['Codigo']),cursos['Nombre'],cursos['Creditos'],cursos['Prerequisitos'],cursos['Obligatorio'])
                            print("Pre orden datos de arbol B")
                            BtreeCursosEstu.preOrden()
                            print("Se va agregar en semestre: "+ str(semes['Semestre']))
                            listaSemes.add_Semestres(semes['Semestre'], BtreeCursosEstu)
                        listaAños.add_Años(año['Año'], listaSemes, None)
                    arbolAVL.seek(arbolAVL.root, int(estudiante['Carnet'])).listAños = listaAños

        """   for estudiante in info['Estudiantes']:
                if arbolAVL.seek(arbolAVL.root, estudiante['Carnet']):
                    aux = arbolAVL.seek(arbolAVL.root, estudiante['Carnet']).listAños.cabeza
                    print("**********************************")
                    while (aux is not None):
                        print("Estamos en año: " + aux.año)
                        aux2 = aux.listaSemes.cabeza
                        while aux2 is not None:
                            print("Estamos en Semestre: " + aux2.nSemestre)
                            aux2.arbolCursos.preOrden()
                            aux2 = aux2.siguiente
                        aux = aux.siguiente  """
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

    return ""

@app.route ('/prueba')
def canche():
    print("aaaaaaaaaaa2backend")
    return "Probando el flask"



if __name__ == '__main__':
    app.run(debug=True, port=5000)


