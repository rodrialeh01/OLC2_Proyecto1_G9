from AST.Abstract.Expresion import Expresion
from AST.Simbolos.Retorno import Retorno


class Primitivo(Expresion):

    def __init__(self, tipo, valor, fila, columna):
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper) -> Retorno:
        return Retorno(self.valor, self.tipo)
    