from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


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
            if valor.tipo != TIPO_DATO.NUMERO:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la funcion nativa toExponential, la expresion debe de ser de tipo Number, pero se encontró de tipo " + obtTipoDato(valor.tipo) )
                s.addError(err)
                return
            if cantidad.tipo != TIPO_DATO.NUMERO:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la funcion nativa toExponential, la expresion debe de ser de tipo Number, pero se encontró de tipo " + obtTipoDato(cantidad.tipo) )
                s.addError(err)

        formato = "{:." + str(int(cantidad.valor)) + "e}"
        return Retorno(formato.format(float(valor.valor)), TIPO_DATO.CADENA)

    def genArbol(self) -> Nodo:
        nodo = Nodo("TO_EXPONENTIAL")
        nodo.agregarHijo(Nodo("("))
        nodo.agregarHijo(self.expresion.genArbol())
        nodo.agregarHijo(Nodo(","))
        nodo.agregarHijo(self.cantidad.genArbol())
        nodo.agregarHijo(Nodo(")"))

        return nodo