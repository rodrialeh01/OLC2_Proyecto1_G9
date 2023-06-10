from AST.Abstract.Expresion import Expresion
from AST.Simbolos.Retorno import Retorno


class Identificador(Expresion):
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        print("Desde Identificador : ")
        existe = entorno.ExisteSimbolo(self.nombre)
        print("Existe: ", existe)
        if existe:
            print("Desde Identificador 2: ")
            ret = entorno.ObtenerSimbolo(self.nombre)
            print(ret)
            return Retorno(ret.valor, ret.tipo)
        else:
            return Retorno(None, None)