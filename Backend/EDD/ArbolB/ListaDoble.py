from NodoDoble import nodoDoble
class listaDoble:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.cuenta=0

    def vacio(self):
        return self.primero == None

    def insertarNodoD(self,codigoC, nombre, nCreditos, prerrequisitos, obligatorio):
        nuevo=nodoDoble(codigoC, nombre, nCreditos, prerrequisitos, obligatorio)
        if self.cuenta < 4:
            if self.vacio():
                self.primero=nuevo
                self.ultimo=self.primero
            else:
                self.ultimo.siguiente=nuevo
                nuevo.anterior=self.ultimo
                self.ultimo=nuevo
        else:
            print("El tamaño esta al maximo")

    def insertarDato(self, codigoC, posicion):
        aux=self.primero
        while posicion != 0:
            posicion-=1
            aux=aux.siguiente
        aux.codigoC=codigoC

    def devolverDato(self,posicion):
        aux=self.primero
        while posicion is not 0:
            posicion-=1
            aux=aux.siguiente
        return aux

    def mostrarDatos(self):
        aux=self.primero
        while aux is not None:
            print("Dato: "+aux.codigoC)
            aux=aux.siguiente

