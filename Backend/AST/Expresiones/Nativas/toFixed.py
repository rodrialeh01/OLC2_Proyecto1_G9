from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class ToFixed(Expresion):
    def __init__(self, expresion, cantidad, fila, columna):
        self.expresion = expresion
        self.cantidad = cantidad
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        existe = entorno.ExisteSimbolo(self.expresion)
        cantidad_de_decimales = self.cantidad.ejecutar(entorno, helper)
        if existe == False:
            #validar por si es una llamada a una funcion
            existe2 = self.expresion.ejecutar(entorno, helper)
            if existe2 == None:
                #error semantico
                return
        else:
            valor_a_aproximar = entorno.ObtenerSimbolo(self.expresion)
            if valor_a_aproximar.tipo != TIPO_DATO.NUMERO or cantidad_de_decimales.tipo != TIPO_DATO.NUMERO or cantidad_de_decimales.tipo != TIPO_DATO.ANY or cantidad_de_decimales.tipo != TIPO_DATO.ANY:
                #error semantico
                if valor_a_aproximar.tipo != TIPO_DATO.NUMERO:
                    s = SingletonErrores.getInstance()
                    err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la función toFixed, debe de ser de tipo Number, pero se encontró de tipo " + obtTipoDato(valor_a_aproximar.tipo) )
                    s.addError(err)
                    return
                if cantidad_de_decimales.tipo != TIPO_DATO.NUMERO:
                    s = SingletonErrores.getInstance()
                    err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la función toFixed, debe de ser de tipo Number, pero se encontró de tipo " + obtTipoDato(cantidad_de_decimales.tipo) )
                    s.addError(err)
                    return
                
            return Retorno(round(float(valor_a_aproximar.valor),int(cantidad_de_decimales.valor)), TIPO_DATO.NUMERO)

    def genArbol(self) -> Nodo:
        nodo = Nodo("TO_FIXED")
        nodo.agregarHijo(Nodo("("))
        nodo.agregarHijo(self.expresion.genArbol())
        nodo.agregarHijo(Nodo(","))
        nodo.agregarHijo(self.cantidad.genArbol())
        nodo.agregarHijo(Nodo(")"))

        return nodo