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
        if valor.tipo != TIPO_DATO.NUMERO or cantidad.tipo != TIPO_DATO.NUMERO or cantidad.tipo != TIPO_DATO.ANY or valor.tipo != TIPO_DATO.ANY:
            if valor.tipo != TIPO_DATO.NUMERO:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la funcion nativa toExponential, la expresion debe de ser de tipo Number, pero se encontró de tipo " + obtTipoDato(valor.tipo) )
                s.addError(err)
                helper.setConsola("[ERROR]: Se ha encontrado un error en la funcion nativa toExponential, la expresion debe de ser de tipo Number, pero se encontró de tipo " + obtTipoDato(valor.tipo) + " en la línea " + str(self.fila) + " y columna "+ str(self.columna))
                return Retorno(None, TIPO_DATO.ERROR)
            if cantidad.tipo != TIPO_DATO.NUMERO:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la funcion nativa toExponential, el argumento debe de ser de tipo Number, pero se encontró de tipo " + obtTipoDato(cantidad.tipo) )
                helper.setConsola("[ERROR]: Se ha encontrado un error en la funcion nativa toExponential, el argumento debe de ser de tipo Number, pero se encontró de tipo " + obtTipoDato(cantidad.tipo) + " en la línea " + str(self.fila) + " y columna "+ str(self.columna))
                s.addError(err)
                return Retorno(None, TIPO_DATO.ERROR)
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