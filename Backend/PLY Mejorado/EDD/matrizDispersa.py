import os


class nodoMatriz:
    def __init__(self,listadTareas, x,y):
        self.listadTareas=listadTareas
        self.x=x
        self.y=y
        self.siguiente=None
        self.anterior=None
        self.arriba=None
        self.abajo=None
        self.izquierda=None
        self.derecha=None

class nodoEncabeza:
    def __init__(self,valor, x,y):
        self.valor=valor
        self.x=x
        self.y=y
        self.siguiente=None
        self.anterior=None
        self.arriba=None
        self.abajo=None
        self.izquierda=None
        self.derecha=None


class lista:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def ordenar(self, nodo):
        aux = self.primero
        while (aux is not None):
            if aux.valor < nodo.valor:
                aux=aux.siguiente
            else:
                if aux == self.primero:
                    nodo.siguiente=aux
                    aux.anterior=nodo
                    self.primero=nodo
                    return
                else:
                    nodo.anterior=aux.anterior
                    aux.anterior.siguiente=nodo
                    nodo.siguiente=aux
                    aux.anterior=nodo
                    return
        self.ultimo.siguiente=nodo
        nodo.anterior=self.ultimo
        self.ultimo=nodo
        return

    def insertar(self,valor):
        nodo = nodoEncabeza(valor,None,None)
        if self.primero==None:
            self.primero=self.ultimo = nodo
            return
        self.ordenar(nodo)

    def busqueda(self,valor):
        temp=self.primero
        while(temp is not None):
            if temp.valor == valor:
                return temp
            temp=temp.siguiente
        return None

class matrizD:
    def __init__(self):
        self.lista_horizontal = lista()
        self.lista_vertical = lista()

    def insertar(self, lista,x,y):
        nodo_x=self.lista_horizontal.busqueda(x)
        nodo_y=self.lista_vertical.busqueda(y)

        if nodo_x == None and nodo_y == None:
            self.caso1(lista,x,y)
        elif nodo_x == None and nodo_y is not None:
            self.caso2(lista, x, y)
        elif nodo_x is not None and nodo_y == None:
            self.caso3(lista, x, y)
        else:
            self.caso4(lista, x, y)

    def caso1(self, lista, x,y):
        self.lista_horizontal.insertar(x)
        self.lista_vertical.insertar(y)

        nodo_x=self.lista_horizontal.busqueda(x)
        nodo_y=self.lista_vertical.busqueda(y)
        nuevo = nodoMatriz(lista,x,y)
        nodo_x.abajo=nuevo
        nuevo.arriba=nodo_x
        nodo_y.derecha=nuevo
        nuevo.izquierda=nodo_y

    def caso2(self,lista,x,y):
        self.lista_horizontal.insertar(x)
        nodo_x=self.lista_horizontal.busqueda(x)
        nodo_y=self.lista_vertical.busqueda(y)
        agregado=False
        nuevo = nodoMatriz(lista,x,y)
        aux=nodo_y.derecha
        cabecera=0

        while aux is not None:
            cabecera=aux.x
            if cabecera < x:
                aux=aux.derecha
            else:
                nuevo.derecha=aux
                nuevo.izquierda=aux.izquierda
                aux.izquierda.derecha=nuevo
                aux.izquierda=nuevo
                agregado=True
                break

        if agregado == False:
            aux=nodo_y.derecha
            while aux.derecha is not None:
                aux=aux.derecha
            nuevo.izquierda=aux
            aux.derecha=nuevo

        nodo_x.abajo=nuevo
        nuevo.arriba=nodo_x

    def caso3(self,lista,x,y):
        self.lista_vertical.insertar(y)
        nodo_x=self.lista_horizontal.busqueda(x)
        nodo_y=self.lista_vertical.busqueda(y)
        agregado=False
        nuevo = nodoMatriz(lista,x,y)
        aux=nodo_x.abajo
        cabecera=0

        while (aux is not None and agregado != True):
            cabecera=aux.y
            if cabecera < y:
                aux=aux.abajo
            else:
                nuevo.abajo=aux
                nuevo.arriba=aux.arriba
                aux.arriba.abajo=nuevo
                aux.arriba=nuevo
                agregado=True

        if agregado is not True:
            aux=nodo_x.abajo
            while aux.abajo is not None:
                aux=aux.abajo
            aux.abajo=nuevo
            nuevo.arriba=aux

        nodo_y.derecha=nuevo
        nuevo.izquierda=nodo_y

    def caso4(self,lista,x,y):

        nodo_x = self.lista_horizontal.busqueda(x)
        nodo_y = self.lista_vertical.busqueda(y)
        agregado = False
        nuevo = nodoMatriz(lista, x, y)
        aux = nodo_y.derecha
        cabecera = 0

        while aux is not None:
            cabecera=aux.x
            if cabecera<x:
                aux=aux.derecha
            else:
                nuevo.derecha=aux
                nuevo.izquierda=aux.izquierda
                aux.izquierda.derecha=nuevo
                aux.izquierda=nuevo
                agregado=True
                break

        if agregado == False:
            aux=nodo_y.derecha
            while aux.derecha is not None:
                aux=aux.derecha
            nuevo.izquierda=aux
            aux.derecha=nuevo

        agregado=False
        aux=nodo_x.abajo
        cabecera=0

        while (aux is not None and agregado != True):
            cabecera = aux.y
            if cabecera < y:
                aux = aux.abajo
            else:
                nuevo.abajo = aux
                nuevo.arriba = aux.arriba
                aux.arriba.abajo = nuevo
                aux.arriba = nuevo
                agregado = True

        if agregado is not True:
            aux = nodo_x.abajo
            while aux.abajo is not None:
                aux = aux.abajo
            aux.abajo = nuevo
            nuevo.arriba = aux

    def buscar(self,x,y):
        cabecera = self.lista_vertical.primero
        while cabecera is not None:
            aux = cabecera.derecha
            while aux is not None:
                if aux.x == x and aux.y ==y:
                    print("Valor encontrado: " + aux.listadTareas)
                aux=aux.derecha
            cabecera=cabecera.siguiente
        print("Valor no encontrado")
        return

    def imprimir_horizontal(self):
        cabecera = self.lista_vertical.primero
        while(cabecera is not None):
            aux=cabecera.derecha
            while aux is not None:
                print("Valor:", aux.listadTareas, "X:", aux.x, "Y:", aux.y)
                aux=aux.derecha
            cabecera=cabecera.siguiente

    def imprimir_vertical(self):
        cabecera = self.lista_horizontal.primero
        while (cabecera is not None):
            aux = cabecera.abajo
            while aux is not None:
                print("Valor:", aux.listadTareas, "X:", aux.x, "Y:", aux.y)
                aux = aux.abajo
            cabecera = cabecera.siguiente


    def graficar(self):
        f = open('mDispersa.dot', 'w', encoding='utf-8')
        cadena=""
        linea=""
        cadena += "digraph G{\n"
        cadena += "node[color=\"blue\",style=\"filled\",fillcolor=lightyellow, shape=box];\n"
        cadena += "raiz[label=\"0,0" "\",group=1];\n"
        cadena += "edge[dir = both];\n"
        cabecerax = self.lista_horizontal.primero
        while (cabecerax is not None):
            cadena += "Col" + str(cabecerax.valor) + "[label=\"" + str(cabecerax.valor) + "\",group="+str(cabecerax.valor+1)+"];\n"
            cabecerax = cabecerax.siguiente
        cabecerax = self.lista_horizontal.primero
        while (cabecerax.siguiente is not None):
            cadena += "Col" + str(cabecerax.valor) + "->Col" + str(cabecerax.siguiente.valor) + ";\n"
            linea = linea + "Col" + str(cabecerax.valor)+ ";"
            cabecerax = cabecerax.siguiente
        linea = linea + "Col" + str(cabecerax.valor) + ";"

        cabeceray = self.lista_vertical.primero
        while (cabeceray is not None):
            cadena += "Fil" + str(cabeceray.valor) + "[label=\"" + str(cabeceray.valor) +"\",group=1];\n"
            cabeceray = cabeceray.siguiente
        cabeceray = self.lista_vertical.primero
        while (cabeceray.siguiente is not None):
            cadena += "Fil" + str(cabeceray.valor) + "->Fil" + str(cabeceray.siguiente.valor) + ";\n"
            cabeceray = cabeceray.siguiente
        cadena +="raiz->Fil"+str(self.lista_vertical.primero.valor)+";\n"
        cadena += "raiz->Col" + str(self.lista_horizontal.primero.valor) + ";\n"
        cadena+="{rank = same;raiz;"+linea+"};\n"
        linea=""

        cabecera = self.lista_vertical.primero
        while (cabecera is not None):
            aux = cabecera.derecha
            while aux is not None:
                print("Valor:", aux.listadTareas, "X:", aux.x, "Y:", aux.y)
                cadena += "Node" + str(aux.x) +"_"+str(aux.y)+"[label=\"" + aux.listadTareas.tamaño+ "\",group=" + str(aux.x + 1) + "];\n"
                aux = aux.derecha
            cabecera = cabecera.siguiente

        # Esto es para unir las filas--------------------------------------
        cabecera = self.lista_vertical.primero
        while (cabecera is not None):
            aux = cabecera.derecha
            otracabecera = self.lista_horizontal.primero
            primero = True
            while aux is not None:
                while otracabecera is not None:
                    if aux.derecha is not None:
                        if aux.x == otracabecera.valor and primero != True :
                            cadena += "Node" + str(aux.x) + "_" + str(aux.y) + "->Node" + str(aux.derecha.x) + "_" + str(aux.derecha.y) + ";\n"
                            cadena += "{rank = same;Node" + str(aux.x) + "_" + str(aux.y) + ";Node" + str(aux.derecha.x) + "_" + str(aux.derecha.y) + "};\n"
                            aux=aux.derecha
                        elif primero == True:
                            cadena += "Fil" + str(aux.y) + "->Node" + str(aux.x) + "_" + str(aux.y) + ";\n"
                            if aux.derecha is not None:
                                cadena += "Node" + str(aux.x) + "_" + str(aux.y) + "->Node" + str(
                                    aux.derecha.x) + "_" + str(
                                    aux.derecha.y) + ";\n"
                                cadena += "{rank = same;Node" + str(aux.x) + "_" + str(aux.y) + ";Node" + str(
                                    aux.derecha.x) + "_" + str(aux.derecha.y) + "};\n"
                            cadena += "{rank = same;Fil" + str(aux.y) + ";Node" + str(aux.x) + "_" + str(aux.y) + "};\n"
                            primero=False
                            aux=aux.derecha
                    else:
                        if aux.x == otracabecera.valor and primero == True:
                            cadena += "Fil" + str(aux.y) + "->Node" + str(aux.x) + "_" + str(aux.y) + ";\n"
                            cadena += "{rank = same;Fil" + str(aux.y) + ";Node" + str(aux.x) + "_" + str(aux.y) + "};\n"
                            break

                    otracabecera=otracabecera.siguiente
                aux=aux.derecha
            cabecera = cabecera.siguiente


        #Esto es para unir las columnas--------------------------------------
        cabecera = self.lista_horizontal.primero
        while (cabecera is not None):
            aux = cabecera.abajo
            otracabecera = self.lista_vertical.primero
            primero = True
            while aux is not None:
                while otracabecera is not None:
                    if aux.abajo is not None:
                        if aux.y == otracabecera.valor and primero != True:
                            cadena += "Node" + str(aux.x) + "_" + str(aux.y) + "->Node" + str(aux.abajo.x) + "_" + str(aux.abajo.y) + ";\n"
                            aux = aux.abajo
                        elif primero == True:
                            cadena += "Col" + str(aux.x) + "->Node" + str(aux.x) + "_" + str(aux.y) + ";\n"
                            if aux.abajo is not None:
                                cadena += "Node" + str(aux.x) + "_" + str(aux.y) + "->Node" + str(aux.abajo.x) + "_" + str(aux.abajo.y) + ";\n"
                            primero = False
                            aux = aux.abajo
                    else:
                        if aux.y == otracabecera.valor and primero == True:
                            cadena += "Col" + str(aux.x) + "->Node" + str(aux.x) + "_" + str(aux.y) + ";\n"
                            break

                    otracabecera = otracabecera.siguiente
                aux = aux.abajo
            cabecera = cabecera.siguiente

        f.write(cadena)
        f.write('}')
        f.close()
        os.system('dot -Tpng mDispersa.dot -o mDispersaSalida.png')


def pruebas():
    m=matrizD()
    m.insertar("2", 1, 2)
    m.insertar("3", 1, 4)
    m.insertar("5", 2, 5)
    m.insertar("9", 2, 90)
    m.insertar("8", 90, 2)
    m.insertar("7", 1, 1)
    m.insertar("7", 3, 4)
    m.insertar("p", 3, 5)
    m.insertar("7", 90, 50)
    m.insertar("43", 4, 2)
    m.graficar()
#pruebas()

