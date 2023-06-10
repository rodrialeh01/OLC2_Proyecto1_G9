from AST.Abstract.Instruccion import Instruccion
from AST.Nodo import Nodo


class Params_Interface(Instruccion):
    def __init__(self, id, tipo, linea, columna):
        self.id = id
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        

    def ejecutar(self, entorno, helper):
        pass

    def genArbol(self) -> Nodo:
        nodo = Nodo("PARAMS_INTERFACE")
        nodo.agregarHijo(Nodo(str(self.id)))
        nodo.agregarHijo(Nodo(str(self.tipo)))
        return nodo