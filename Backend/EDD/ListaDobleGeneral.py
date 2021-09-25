from NodoAños import nodoAños
from NodoMeses import nodoMeses

class listaDoble:
    def __init__(self):
        self.cabeza=None

    def add_Años(self,año,listaSemes,listaMeses):
        nuevo = nodoAños(año,listaSemes,listaMeses, None, None)
        if self.cabeza is not None:
          self.cabeza = nuevo
        else:
          aux = self.cabeza
          while aux.siguiente is not None:
            aux = aux.siguiente
          aux.siguiente = nuevo
          nuevo.anterior = aux

    def add_Meses(self,nMes,matrizTareas):
        nuevo = nodoMeses(nMes,matrizTareas, None, None)
        if self.cabeza is not None:
          self.cabeza = nuevo
        else:
          aux = self.cabeza
          while aux.siguiente is not None:
            aux = aux.siguiente
          aux.siguiente = nuevo
          nuevo.anterior = aux

    def add_Semestres(self,nSemestre,arbolCursos):
        nuevo = nodoMeses(nSemestre,arbolCursos, None, None)
        if self.cabeza is not None:
          self.cabeza = nuevo
        else:
          aux = self.cabeza
          while aux.siguiente is not None:
            aux = aux.siguiente
          aux.siguiente = nuevo
          nuevo.anterior = aux


