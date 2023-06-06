from AST.Abstract.Expresion import Expresion
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno


class ToExponential(Expresion):
    def __init__(self, expresion, cantidad, fila, columna):
        self.expresion = expresion
        self.cantidad = cantidad
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        valor = self.expresion.ejecutar(entorno, helper)
        cantidad = self.cantidad.ejecutar(entorno, helper)
        if valor.tipo != TIPO_DATO.NUMERO or cantidad.tipo != TIPO_DATO.NUMERO:
            #error semantico
            pass

        formato = "{:." + str(int(cantidad.valor)) + "e}"
        return Retorno(formato.format(float(valor.valor)), TIPO_DATO.CADENA)