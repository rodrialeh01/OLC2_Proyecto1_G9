from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo


class Params_Declarado(Expresion):
    def __init__(self, id, expresion, linea, columna):
        self.id = id
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        

    def ejecutar(self, entorno, helper):
        return self
    
    def genArbol(self) -> Nodo:
        
        nodo = Nodo("PARAMS_DECLARADO")
        nodoIg = Nodo("=")
        nodoIg.agregarHijo(Nodo(str(self.id)))
        nodoIg.agregarHijo(self.expresion.genArbol())
        nodo.agregarHijo(nodoIg)
        return nodo