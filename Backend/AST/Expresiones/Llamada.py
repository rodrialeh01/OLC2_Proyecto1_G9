from AST.Abstract.Expresion import Expresion
from AST.Abstract.Instruccion import Instruccion
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno


class Llamada(Instruccion, Expresion):
    def __init__(self, id, params, linea, columna):
        self.linea = linea
        self.columna = columna
        self.id = id
        self.params = params

    def ejecutar(self, entorno, helper):
        fn = entorno.ExisteFuncion(self.id)
        if fn is False:
            print("Error semántico, la función no existe")
            return

        entornoFN = Entorno(entorno)
        entornoFN.actual = "Función " + str(self.id)
        func = entorno.ObtenerFuncion(self.id)

        argumentos = func.declaracionesParams(entornoFN, self.params, entorno, helper)

        if argumentos is False:
            print("Error semántico, la cantidad de argumentos no coincide con la cantidad de parametros")
            return
        

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
    