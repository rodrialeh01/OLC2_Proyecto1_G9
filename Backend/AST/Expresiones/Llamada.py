from AST.Abstract.Expresion import Expresion
from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class Llamada(Instruccion, Expresion):
    def __init__(self, id, params, linea, columna):
        self.linea = linea
        self.columna = columna
        self.id = id
        self.params = params

    def ejecutar(self, entorno, helper):
        fn = entorno.ExisteFuncion(self.id)
        if fn is False:
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La función " + self.id + " no existe en el entorno actual")
            s.addError(err)
            return Retorno(None, None)

        entornoFN = Entorno(entorno)
        entornoFN.actual = "Función " + str(self.id)
        func = entorno.ObtenerFuncion(self.id)

        argumentos = func.declaracionesParams(entornoFN, self.params, entorno, helper)

        if argumentos is False:
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La cantidad de parámetros no coincide con la cantidad de argumentos")
            s.addError(err)
            return Retorno(None, None)
        

        if func is not None:
            func.ejecutar(entornoFN, helper)

    def genArbol(self):
        nodo = Nodo("LLAMADA FUNCIÓN")
        nodohijo = Nodo(self.id)
        nodohijo2 = Nodo("(")
        nodohijo3 = Nodo("PARAMETROS")
        nodohijo4 = Nodo(")")
        nodo.agregarHijo(nodohijo)
        nodo.agregarHijo(nodohijo2)
        for param in self.params:
            nodohijo3.agregarHijo(param.genArbol())
        nodo.agregarHijo(nodohijo3)
        nodo.agregarHijo(nodohijo4)

        return nodo
    