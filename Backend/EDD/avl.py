import os
from typing import no_type_check_decorator


class nodoAVL:
    def __init__(self, nCarnet, dpi, nombre, carrera, correo, password, creditos, edad, listAños):
        self.nCarnet=nCarnet
        self.dpi=dpi
        self.nombre=nombre
        self.carrera=carrera
        self.correo=correo
        self.password=password
        self.creditos=creditos
        self.edad=edad
        self.listAños=listAños
        self.left = None
        self.right=None
        self.altura=0


class AVL:
    def __init__(self):
        self.root = None
        self.cadena = ""
    
    def max(self, val1,val2):
        if val1>val2:
            return val1
        else:
            return val2

    def height(self, nodo):
        if nodo is not None:
            return nodo.altura
        return -1


    def insert(self, nCarnet, dpi, nombre, carrera, correo, password, creditos, edad, listAños):
        self.root=self.insert_intern(nCarnet, dpi, nombre, carrera, correo, password, creditos, edad, listAños, self.root)

    def insert_intern(self,nCarnet, dpi, nombre, carrera, correo, password, creditos, edad, listAños, root):
        if root is None:
            return nodoAVL(nCarnet, dpi, nombre, carrera, correo, password, creditos, edad, listAños)
        else:
            if nCarnet < root.nCarnet:
                root.left = self.insert_intern(nCarnet, dpi, nombre, carrera, correo, password, creditos, edad, listAños,root.left)
                if self.height(root.right) - self.height(root.left) == -2:
                    if nCarnet < root.left.nCarnet:
                        root=self.RI(root)
                    else:
                        root=self.RDI(root)
            elif nCarnet>root.nCarnet:
                root.right = self.insert_intern(nCarnet, dpi, nombre, carrera, correo, password, creditos, edad, listAños,root.right)
                if self.height(root.right) - self.height(root.left) == 2:
                    if nCarnet > root.right.nCarnet:
                        root=self.RD(root)
                    else:
                        root=self.RID(root)
            else:
                root.nCarnet = nCarnet

        root.altura = self.max(self.height(root.left),self.height(root.right))+1
        return root

    def RI(self, nodo):
        aux=nodo.left
        nodo.left=aux.right
        aux.right=nodo
        nodo.altura=self.max(self.height(nodo.left),self.height(nodo.right))+1
        aux.altura=self.max(self.height(aux.left),self.height(aux.right))+1
        return aux
    
    def RD(self,nodo):
        aux=nodo.right
        nodo.right=aux.left
        aux.left=nodo
        nodo.altura=self.max(self.height(nodo.left),self.height(nodo.right))+1
        aux.altura=self.max(self.height(aux.left),self.height(aux.right))+1
        return aux

    def RDI(self, nodo):
        nodo.left=self.RD(nodo.left)
        return self.RI(nodo)
    
    def RID(self,nodo):
        nodo.right=self.RI(nodo.right)
        return self.RD(nodo)


    def preorden(self):
        self.preorden_intern(self.root)

    def preorden_intern(self, root):
        if root is not None:
            print(root.nCarnet)
            self.preorden_intern(root.left)
            self.preorden_intern(root.right)

    def generar(self):
        f = open('dotArbolAVL.dot', 'w', encoding='utf-8')
        self.cadena+="digraph G{\n"
        self.cadena+="node[color=\"blue\",style=\"rounded,filled\",fillcolor=lightyellow, shape=record];\n"
        if self.root is not None:
            self.cadena+="node"+str(id(self.root))+"[label=\"<f0>|<f1> Carnet: "+ str(self.root.nCarnet)+ "\\nNombre: "+self.root.nombre+ "\\nCarrera: "+self.root.carrera+ "|<f2>\"];\n"
            self.generar2( self.root, self.root.left, True)
            self.generar2( self.root, self.root.right, False)
        self.cadena+="}\n"
        f.write(self.cadena)
        f.close()
        os.system('dot -Tpng dotArbolAVL.dot -o sArbolAVL.png')

    def generar2(self, padre, actual, izquierda):
        if actual is not None:
            self.cadena += "node" + str(id(actual)) +"[label=\"<f0>|<f1>Carnet: "+ str(actual.nCarnet)+ "\\nNombre: "+actual.nombre+ "\\nCarrera: "+actual.carrera+ "|<f2>\"];\n"
            if izquierda:
                self.cadena +="node"+str(id(padre))+":f0->node"+str(id(actual))+":<f1>\n"
            else:
                self.cadena += "node" + str(id(padre)) + ":f2->node" + str(id(actual)) + ":<f1>\n"
            self.generar2(actual,actual.left,True)
            self.generar2(actual,actual.right,False)


def pruebas():
    arbol = AVL()
    arbol.insert( 1, "000000", "nombre", "carrera", "correo", "password", 30, 20, None)
    arbol.insert( 2, "000000", "nombre", "carrera", "correo", "password", 30, 20, None)
    arbol.insert( 3, "000000", "nombre", "carrera", "correo", "password", 30, 20, None)
    arbol.insert( 4, "000000", "nombre", "carrera", "correo", "password", 30, 20, None)
    arbol.insert( 5, "000000", "nombre", "carrera", "correo", "password", 30, 20, None)
    arbol.insert( 6, "000000", "nombre", "carrera", "correo", "password", 30, 20, None)
    arbol.preorden()
    arbol.generar()

pruebas()