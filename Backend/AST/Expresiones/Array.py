from AST.Abstract.Expresion import Expresion
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno


class Array(Expresion):
    def __init__(self, expresiones, linea, columna):
        self.tipo = TIPO_DATO.ANY
        self.expresiones = expresiones
        self.linea = linea
        self.columna = columna
        
        # print("Se va a crear una expresion de Array:")
        # print(self.tipo)
        # print("[")
        # for exp in self.expresiones:
        #     print("\t",exp.ejecutar(None,None).valor)
        # print("]")


    def ejecutar(self, entorno, helper):
        arr = []
        for exp in self.expresiones:
            arr.append(exp.ejecutar(entorno, helper))
        return Retorno(arr, TIPO_DATO.ARRAY)