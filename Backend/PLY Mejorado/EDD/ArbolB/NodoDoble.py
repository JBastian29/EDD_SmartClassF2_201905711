class nodoDoble:
    def __init__(self, codigoC, nombre, nCreditos, prerrequisitos, obligatorio):
        self.codigoC=codigoC
        self.nombre=nombre
        self.nCreditos=nCreditos
        self.prerrequisitos=prerrequisitos
        self.obligatorio=obligatorio
        self.siguiente=None
        self.anterior=None
        
