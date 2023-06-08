from AST.Abstract.Expresion import Expresion
from AST.Abstract.Instruccion import Instruccion
from AST.Simbolos.Entorno import Entorno


class Llamada(Instruccion, Expresion):
    def __init__(self, id, params, linea, columna):
        self.linea = linea
        self.columna = columna
        self.id = id
        self.params = params

    def ejecutar(self, entorno, helper):
        print("ejecutar llamada")
        fn = entorno.ExisteFuncion(self.id)
        if fn is False:
            print("Error semántico, la función no existe")
            return
        

        entornoFN = Entorno(entorno)
        func = entorno.ObtenerFuncion(self.id)

        argumentos = func.declaracionesParams(entornoFN, self.params, entorno, helper)
        print("argumentos")
        if argumentos is False:
            print("Error semántico, la cantidad de argumentos no coincide con la cantidad de parametros")
            return
        

        if func is not None:
            func.ejecutar(entornoFN, helper)