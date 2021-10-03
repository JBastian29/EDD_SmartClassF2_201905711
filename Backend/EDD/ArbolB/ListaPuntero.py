from NodoPuntero import nodoPuntero
class listaPuntero:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.cuenta=0

    def vacio(self):
        return self.primero == None

    def insertarPuntero(self, puntero):
        nuevo = nodoPuntero(puntero)
        if self.cuenta<5:
            if self.vacio():
                self.primero=nuevo
                self.ultimo=self.primero
            else:
                self.ultimo.siguienteP=nuevo
                nuevo.anteriorP=self.ultimo
                self.ultimo=nuevo
            self.cuenta+=1

    def insertarPunteroP(self, pagina,posicion):
        aux=self.primero
        while posicion != 0:
            posicion-=1
            aux=aux.siguienteP
        aux.puntero=pagina

    def devolverPuntero(self, posicion):
        aux=self.primero
        while posicion != 0:
            posicion-=1
            aux=aux.siguienteP
        return aux


