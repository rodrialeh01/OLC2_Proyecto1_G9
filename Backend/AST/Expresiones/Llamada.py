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
        print("Ejecutando llamada a función")
        fn = entorno.ExisteFuncion(self.id)
        helperTemp = helper.getFuncion()

        if fn is False:
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "La función " + self.id + " no existe en el entorno actual")
            s.addError(err)
            helper.setConsola("[ERROR]: La función " + self.id + " no existe en el entorno actual " + " en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
            return Retorno(None, TIPO_DATO.ERROR)

        entornoFN = Entorno(entorno)
        entornoFN.actual = "Función " + str(self.id)
        func = entorno.ObtenerFuncion(self.id)

        argumentos = func.declaracionesParams(entornoFN, self.params, entorno, helper)
        
        if argumentos is False:
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "La cantidad de parámetros de la función "+ self.id+" no coincide con la cantidad de argumentos")
            s.addError(err)
            helper.setConsola("[ERROR]: La cantidad de parámetros de la función "+ self.id+" no coincide con la cantidad de argumentos " + " en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
            return Retorno(None, TIPO_DATO.ERROR)
        

        if func is not None:
            ret = func.ejecutar(entornoFN, helper)
            if ret is not None:
                helper.setFuncion(helperTemp)
                return Retorno(ret.valor, ret.tipo)
            

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
    