from AST.Abstract.Expresion import Expresion
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno


class ToUpperCase(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        valor = self.expresion.ejecutar(entorno, helper)
        if valor.tipo != TIPO_DATO.CADENA:
            #error semantico
            pass
        
        return Retorno(str(valor.valor).upper(), TIPO_DATO.CADENA)