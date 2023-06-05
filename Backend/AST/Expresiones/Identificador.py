from AST.Abstract.Expresion import Expresion
from AST.Simbolos.Retorno import Retorno


class Identificador(Expresion):
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        existe = entorno.ExisteSimbolo(self.nombre)

        if existe:
            ret = entorno.ObtenerSimbolo(self.nombre)
            return Retorno(ret.valor, ret.tipo)
        else:
            pass