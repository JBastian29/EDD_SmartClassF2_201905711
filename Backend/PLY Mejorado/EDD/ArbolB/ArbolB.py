import time

from EDD.ArbolB.PaginaB import paginaB
from EDD.ArbolB.compareTo import compareTo
import os


class arbolB:
    def __init__(self):
        self.Raiz=paginaB()
        self.codigoC = 0
        self.nombre = ""
        self.nCreditos = 0
        self.prerrequisitos = ""
        self.obligatorio = ""
        self.aux1=False
        self.aux2=paginaB()
        self.subeArriba=False
        self.estado=False
        self.comparador=False
        self.grafica=""
        self.grafica2=""
        self.codigoCgrafica=""
        self.nodos=0

    def estaVacio(self, raiz):
        return (raiz==None or raiz.cuenta==0)

    def insertarDatos(self, codigoC, nombre, nCreditos, prerrequisitos, obligatorio):
        self.insertarDatos2(self.Raiz,codigoC, nombre, nCreditos, prerrequisitos, obligatorio)

    def insertarDatos2(self,raiz,codigoC, nombre, nCreditos, prerrequisitos, obligatorio):
        self.empujar(raiz,codigoC, nombre, nCreditos, prerrequisitos, obligatorio)
        if self.subeArriba:
            self.Raiz = paginaB()
            self.Raiz.cuenta=1
            self.Raiz.setCodigo(0,self.codigoC)
            self.Raiz.setNombre(0,self.nombre)
            self.Raiz.setnCreditos(0, self.nCreditos)
            self.Raiz.setPrerrequisitos(0, self.prerrequisitos)
            self.Raiz.setObligatorio(0, self.obligatorio)
            self.Raiz.setApuntador(0, raiz)
            self.Raiz.setApuntador(1,self.aux2)

    def empujar(self, raiz,codigoC, nombre, nCreditos, prerrequisitos, obligatorio):
        posicion=0
        estado=False

        if self.estaVacio(raiz) and self.comparador==False:
            self.subeArriba=True
            self.codigoC=codigoC
            self.nombre=nombre
            self.nCreditos=nCreditos
            self.prerrequisitos=prerrequisitos
            self.obligatorio=obligatorio
            self.aux2=None
        else:
            posicion=self.buscarNodoB(codigoC,raiz)
            if self.comparador == False:
                if estado:
                    self.subeArriba=False
                else:
                    self.empujar(raiz.getApuntador(posicion),codigoC, nombre, nCreditos, prerrequisitos, obligatorio)
                    if self.subeArriba:
                        if raiz.cuenta<4:
                            self.subeArriba=False
                            self.meterHoja(raiz,posicion,self.codigoC,self.nombre,self.nCreditos,self.prerrequisitos,self.obligatorio)
                        else:
                            self.subeArriba=True
                            self.dividirPaginaB(raiz,posicion,self.codigoC,self.nombre,self.nCreditos,self.prerrequisitos,self.obligatorio)
            else:
                print("Dato repetido: "+codigoC)
                self.comparador=False

    def buscarNodoB(self, codigo, raiz):
        auxContador=0
        if (compareTo(codigo,raiz.getCodigo(0)).comparar())<0:
            self.estado=False
            auxContador=0
        else:
            while auxContador is not raiz.cuenta:
                if codigo == raiz.getCodigo(auxContador):
                    self.comparador=True
                auxContador+=1
            auxContador=raiz.cuenta

            while (compareTo(codigo,raiz.getCodigo(auxContador-1)).comparar())<0 and auxContador>1:
                auxContador-=1
                self.estado = True if((codigo==raiz.getCodigo(auxContador-1))) else False

        return auxContador

    def meterHoja(self, raiz, posicion,codigoC, nombre, nCreditos, prerrequisitos, obligatorio):
        auxC=raiz.cuenta
        while auxC is not posicion:
            if auxC != 0:
                raiz.setCodigo(auxC,raiz.getCodigo(auxC-1))
                raiz.setNombre(auxC,raiz.getNombre(auxC-1))
                raiz.setnCreditos(auxC,raiz.getnCreditos(auxC-1))
                raiz.setPrerrequisitos(auxC,raiz.getPrerrequisitos(auxC-1))
                raiz.setObligatorio(auxC,raiz.getPrerrequisitos(auxC-1))
                raiz.setApuntador(auxC+1,raiz.getApuntador(auxC))
            auxC-=1
        raiz.setCodigo(posicion,codigoC)
        raiz.setNombre(posicion, nombre)
        raiz.setnCreditos(posicion, nCreditos)
        raiz.setPrerrequisitos(posicion, prerrequisitos)
        raiz.setObligatorio(posicion, obligatorio)
        raiz.setApuntador(posicion+1,self.aux2)
        raiz.cuenta=raiz.cuenta+1

    def dividirPaginaB(self,raiz,posicion,codigoC, nombre, nCreditos, prerrequisitos, obligatorio):
        posicion2=0
        posicionMedia=0

        if posicion<=2:
            posicionMedia=2
        else:
            posicionMedia=3

        paginaDerecha=paginaB()
        posicion2=posicionMedia+1

        while posicion2!=5:
            if(posicion2-posicionMedia)!=0:
                paginaDerecha.setCodigo((posicion2-posicionMedia)-1,raiz.getCodigo(posicion2-1))
                paginaDerecha.setNombre((posicion2 - posicionMedia) - 1, raiz.getNombre(posicion2 - 1))
                paginaDerecha.setnCreditos((posicion2 - posicionMedia) - 1, raiz.getnCreditos(posicion2 - 1))
                paginaDerecha.setPrerrequisitos((posicion2 - posicionMedia) - 1, raiz.getPrerrequisitos(posicion2 - 1))
                paginaDerecha.setObligatorio((posicion2 - posicionMedia) - 1, raiz.getObligatorio(posicion2 - 1))
            posicion2+=1

        paginaDerecha.cuenta=4-posicionMedia
        raiz.cuenta=posicionMedia

        if(posicion<=2):
            self.aux1=True
            self.meterHoja(raiz,posicion,codigoC, nombre, nCreditos, prerrequisitos, obligatorio)
        else:
            self.aux1=True
            self.meterHoja(paginaDerecha,(posicion-posicionMedia),codigoC, nombre, nCreditos, prerrequisitos, obligatorio)

        self.codigoC=raiz.getCodigo(raiz.cuenta-1)
        self.nombre = raiz.getNombre(raiz.cuenta - 1)
        self.nCreditos = raiz.getnCreditos(raiz.cuenta - 1)
        self.prerrequisitos = raiz.getPrerrequisitos(raiz.cuenta - 1)
        self.obligatorio = raiz.getObligatorio(raiz.cuenta - 1)

        paginaDerecha.setApuntador(0,raiz.getApuntador(raiz.cuenta))
        raiz.cuenta=raiz.cuenta-1
        self.aux2=paginaDerecha

        if(self.aux1):
            raiz.setCodigo(3,0)
            raiz.setNombre(3, "")
            raiz.setnCreditos(3, 0)
            raiz.setPrerrequisitos(3, "")
            raiz.setObligatorio(3, "")
            raiz.setApuntador(4, None)

            raiz.setCodigo(2, 0)
            raiz.setNombre(2, "")
            raiz.setnCreditos(2, 0)
            raiz.setPrerrequisitos(2, "")
            raiz.setObligatorio(2, "")
            raiz.setApuntador(3, None)

    def preOrden(self):
        self.preOrden2(self.Raiz)

    def preOrden2(self,pagina):
        if pagina is not None:
            for i in range(pagina.cuenta):
                if pagina.getCodigo(i) is not None:
                    if pagina.getCodigo(i) != 0:
                        print(str(pagina.getCodigo(i))+"_")
            print("")
            self.preOrden2(pagina.getApuntador(0))
            self.preOrden2(pagina.getApuntador(1))
            self.preOrden2(pagina.getApuntador(2))
            self.preOrden2(pagina.getApuntador(3))
            self.preOrden2(pagina.getApuntador(4))

    def graficar(self,name):
        f = open('dotArbolB'+name+'.dot', 'w', encoding='utf-8')
        self.grafica = "digraph ArbolB{\n"
        self.grafica += "\nrankdir=TB;\n"
        self.grafica += "node[color=\"blue\",style=\"rounded,filled\",fillcolor=lightyellow, shape=record];\n"
        self.graficar2(self.Raiz)
        self.graficar3(self.Raiz)
        self.grafica+="\n}\n"
        f.write(self.grafica)
        f.close()
        os.system('dot -Tpng dotArbolB'+name+'.dot -o sArbolB'+name+'.png')

    def graficar2(self, pagina):
        contador=0
        if pagina is not None:
            self.nodos=0
            for i in range(pagina.cuenta):
                if pagina.getCodigo(i) != 0:
                    if pagina.getCodigo(i)!= 0:
                        self.nodos+=1
                        if i!=0:
                            self.grafica+="|"
                        if self.nodos==1:
                            self.grafica += "\nNodo" + str(pagina.getCodigo(i)) + "[label=\"<f0> |"
                        if i==0:
                            self.grafica += "<f" + str(i + 1) + ">" + str(pagina.getCodigo(i))+ "\\n" + pagina.getNombre(i) + "|<f" + str(i + 2) + "> "
                            contador = 3
                        else:
                            self.grafica += "<f" + str(contador) + ">" + str(pagina.getCodigo(i)) + "\\n" + pagina.getNombre(i) + "|<f" + str(contador + 1) + "> "
                            contador += 2
                        if i==(pagina.cuenta)-1:
                            contador=0
                            self.grafica+=" \",group=0];\n"

            self.graficar2(pagina.getApuntador(0))
            self.graficar2(pagina.getApuntador(1))
            self.graficar2(pagina.getApuntador(2))
            self.graficar2(pagina.getApuntador(3))
            self.graficar2(pagina.getApuntador(4))

    def graficar3(self, pagina):
        if pagina is not None:

            if pagina.getCodigo(0) != 0:
                if pagina.getCodigo(0)!= 0:
                    if pagina.getApuntador(0) is not None and pagina.getApuntador(0).getCodigo(0) != 0:
                        self.grafica+="\nNodo"+str(pagina.getCodigo(0))+":f0->"+"Nodo"+str(pagina.getApuntador(0).getCodigo(0))
                    if pagina.getApuntador(1) is not None and pagina.getApuntador(1).getCodigo(0) != 0:
                        self.grafica += "\nNodo" + str(pagina.getCodigo(0)) + ":f2->" + "Nodo" + str(pagina.getApuntador(1).getCodigo(0))
                    if pagina.getApuntador(2) is not None and pagina.getApuntador(2).getCodigo(0) != 0:
                        self.grafica += "\nNodo" + str(pagina.getCodigo(0)) + ":f4->" + "Nodo" + str(pagina.getApuntador(2).getCodigo(0))
                    if pagina.getApuntador(3) is not None and pagina.getApuntador(3).getCodigo(0) != 0:
                        self.grafica += "\nNodo" + str(pagina.getCodigo(0)) + ":f6->" + "Nodo" + str(pagina.getApuntador(3).getCodigo(0))
                    if pagina.getApuntador(4) is not None and pagina.getApuntador(4).getCodigo(0) != 0:
                        self.grafica += "\nNodo" + str(pagina.getCodigo(0)) + ":f8->" + "Nodo" + str(pagina.getApuntador(4).getCodigo(0))
            self.graficar3(pagina.getApuntador(0))
            self.graficar3(pagina.getApuntador(1))
            self.graficar3(pagina.getApuntador(2))
            self.graficar3(pagina.getApuntador(3))
            self.graficar3(pagina.getApuntador(4))

"""btree = arbolB()
btree.insertarDatos(100, "Guatemala",2,"No","Si")
btree.insertarDatos(110, "Noruega",2,"No","Si")
btree.insertarDatos(120, "Alemania",2,"No","Si")
btree.insertarDatos(130, "Suiza",2,"No","Si")
btree.insertarDatos(140, "Francia",2,"No","Si")
btree.insertarDatos(150, "Japon",2,"No","Si")
btree.insertarDatos(160, "China",2,"No","Si")
btree.insertarDatos(170, "Singapour",2,"No","Si")
btree.insertarDatos(180, "Corea del Sur",2,"No","Si")
btree.insertarDatos(190, "Tailandia",2,"No","Si")
btree.insertarDatos(200, "Australia",2,"No","Si")
btree.insertarDatos(210, "Guatemala",2,"No","Si")
btree.insertarDatos(220, "Noruega",2,"No","Si")
btree.insertarDatos(230, "Alemania",2,"No","Si")
btree.insertarDatos(240, "Suiza",2,"No","Si")
btree.insertarDatos(250, "Francia",2,"No","Si")
btree.insertarDatos(260, "Japon",2,"No","Si")
btree.insertarDatos(270, "China",2,"No","Si")
btree.insertarDatos(280, "Singapour",2,"No","Si")
btree.insertarDatos(290, "Corea del Sur",2,"No","Si")
btree.insertarDatos(300, "Tailandia",2,"No","Si")
btree.insertarDatos(400, "Australia",2,"No","Si")
btree.insertarDatos(410, "Australia",2,"No","Si")
btree.insertarDatos(420, "Tailandia",2,"No","Si")
btree.insertarDatos(430, "Australia",2,"No","Si")
btree.insertarDatos(440, "Australia",2,"No","Si")
btree.graficar()"""

