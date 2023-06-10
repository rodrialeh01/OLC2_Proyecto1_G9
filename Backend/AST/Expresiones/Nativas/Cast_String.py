from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno


class Cast_String(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        valor = self.expresion.ejecutar(entorno, helper)
        return Retorno(str(valor.valor), TIPO_DATO.CADENA)

    def genArbol(self) -> Nodo:
        nodo = Nodo("CASTEO-STRING")
        nodo.addHijoValor(Nodo("("))
        nodo.addHijoNodo(self.expresion.genArbol())
        nodo.addHijoValor(Nodo(")"))
        return nodo