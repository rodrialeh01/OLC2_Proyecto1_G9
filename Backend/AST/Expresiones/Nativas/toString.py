from AST.Abstract.Expresion import Expresion
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno


class ToString(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        '''
        NOTA: Esta funcion cuando quiero hacer un x.toString() + y.toString() no funciona el y.toString() pero si hago esto:
        x.toString() + (y.toString()) si funciona
        '''
        print("EJECUTANDO TOSTRING")
        print(self.expresion)
        found = entorno.ObtenerSimbolo(self.expresion)
        print(found)
        if entorno.ExisteSimbolo(self.expresion):
            print("EXISTE SIMBOLO")
            valor = found.valor
            return Retorno(str(valor), TIPO_DATO.CADENA)
        else:
            print("NO EXISTE SIMBOLO")
            valor = self.expresion.ejecutar(entorno, helper)
            print(valor.tipo)
            print(valor.valor)
            return Retorno(str(valor.valor), TIPO_DATO.CADENA)
        
