class nodoSemestres:
    def __init__(self,nSemestre,arbolCursos,siguiente,anterior):
        self.nSemestre=nSemestre
        self.arbolCursos=arbolCursos
        self.siguiente = siguiente
        self.anterior= anterior