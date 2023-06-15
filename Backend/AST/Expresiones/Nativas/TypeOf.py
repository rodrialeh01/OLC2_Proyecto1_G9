from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno


class TypeOf(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        found = entorno.ObtenerSimbolo(self.expresion)
        if entorno.ExisteSimbolo(self.expresion):
            tipo = obtTipoDato(found.tipo)
            return Retorno(tipo, TIPO_DATO.CADENA)
        else:
            valor = self.expresion.ejecutar(entorno, helper)
            tipo = obtTipoDato(valor.tipo)
            return Retorno(tipo, TIPO_DATO.CADENA)


    def genArbol(self) -> Nodo:
        pass