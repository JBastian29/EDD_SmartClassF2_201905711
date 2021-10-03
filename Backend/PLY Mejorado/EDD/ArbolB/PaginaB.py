from EDD.ArbolB.ListaPuntero import listaPuntero
from EDD.ArbolB.ListaDoble import listaDoble

class paginaB:
    def __init__(self):
        self.cuenta=0
        self.maxClaves=0
        self.punteros=listaPuntero()
        self.datos=listaDoble()

        for i in range(5):
            if i != 4:
                self.datos.insertarNodoD(0,None,0,None,None)
            self.punteros.insertarPuntero(None)
        self.maxClaves=5

    def paginaLlena(self):
        return self.cuenta == self.maxClaves-1

    def paginaCasiLlena(self):
        return self.cuenta == self.maxClaves/2

    def getCodigo(self, posicion):
        return self.datos.devolverDato(posicion).codigoC

    def setCodigo(self, posicion, codigo):
        self.datos.insertarDato(codigo,posicion)

    def getNombre(self, posicion):
        return self.datos.devolverDato(posicion).nombre

    def setNombre(self, posicion, nombre):
        self.datos.devolverDato(posicion).nombre=nombre

    def getnCreditos(self, posicion):
        return self.datos.devolverDato(posicion).nCreditos

    def setnCreditos(self, posicion, creditos):
        self.datos.devolverDato(posicion).nCreditos = creditos

    def getPrerrequisitos(self, posicion):
        return self.datos.devolverDato(posicion).prerrequisitos

    def setPrerrequisitos(self, posicion, prerrequisitos):
        self.datos.devolverDato(posicion).prerrequisitos = prerrequisitos

    def getObligatorio(self, posicion):
        return self.datos.devolverDato(posicion).obligatorio

    def setObligatorio(self, posicion, obligatorio):
        self.datos.devolverDato(posicion).obligatorio = obligatorio

    def getApuntador(self, posicion):
        return self.punteros.devolverPuntero(posicion).puntero

    def setApuntador(self, posicion, puntero):
        self.punteros.insertarPunteroP(puntero,posicion)



