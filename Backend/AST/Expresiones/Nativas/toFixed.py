from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno


class ToFixed(Expresion):
    def __init__(self, expresion, cantidad, fila, columna):
        self.expresion = expresion
        self.cantidad = cantidad
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        valor_a_aproximar = self.expresion.ejecutar(entorno, helper)
        cantidad_de_decimales = self.cantidad.ejecutar(entorno, helper)

        if valor_a_aproximar.tipo != TIPO_DATO.NUMERO or cantidad_de_decimales.tipo != TIPO_DATO.NUMERO:
            #error semantico
            pass
        return Retorno(round(float(valor_a_aproximar.valor),int(cantidad_de_decimales.valor)), TIPO_DATO.NUMERO)

    def genArbol(self) -> Nodo:
        nodo = Nodo("TO_FIXED")
        nodo.agregarHijo(Nodo("("))
        nodo.agregarHijo(self.expresion.genArbol())
        nodo.agregarHijo(Nodo(","))
        nodo.agregarHijo(self.cantidad.genArbol())
        nodo.agregarHijo(Nodo(")"))

        return nodo