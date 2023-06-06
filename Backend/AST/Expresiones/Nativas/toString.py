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

        valor = self.expresion.ejecutar(entorno, helper)
        return Retorno(str(valor.valor), TIPO_DATO.CADENA)