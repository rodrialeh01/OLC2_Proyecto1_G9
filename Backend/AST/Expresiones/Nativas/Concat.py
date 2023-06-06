from AST.Abstract.Expresion import Expresion
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno


class Concat(Expresion):
    def __init__(self, expresion1, expresion2, fila, columna):
        self.expresion1 = expresion1
        self.expresion2 = expresion2
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        #suponiendo que si se puedan tambien cadenas que es un array de caracteres
        valor1 = self.expresion1.ejecutar(entorno, helper)
        valor2 = self.expresion2.ejecutar(entorno, helper)
        if valor1.tipo == TIPO_DATO.CADENA and valor2.tipo == TIPO_DATO.CADENA:
            return Retorno(str(valor1.valor) + str(valor2.valor), TIPO_DATO.CADENA)
        