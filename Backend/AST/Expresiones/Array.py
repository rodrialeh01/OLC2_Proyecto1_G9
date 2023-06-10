from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno

arr = []
class Array(Expresion):
    
    def __init__(self, expresiones, linea, columna):
        self.tipo = TIPO_DATO.ANY
        self.expresiones = expresiones
        self.linea = linea
        self.columna = columna


    def ejecutar(self, entorno, helper):
        global arr
        arr = []
        for exp in self.expresiones:
            arr.append(exp.ejecutar(entorno, helper))
        retor = Retorno(arr, TIPO_DATO.ARRAY)
        return retor
    
    def ImpresionArrays(self, arr, arrexist):
        for a in arrexist:
            if a.tipo == TIPO_DATO.ARRAY or a.tipo == TIPO_DATO.ARRAY_NUMBER or a.tipo == TIPO_DATO.ARRAY_STRING or a.tipo == TIPO_DATO.ARRAY_BOOLEAN:
                arr2 = []
                arr2 = self.ImpresionArrays(arr2, a.valor)
                arr.append(arr2)
            else:
                arr.append(a.valor)
        return arr

    def genArbol(self):
        global arr
        nuevo = []
        mostrar = self.ImpresionArrays(nuevo,arr)
        return Nodo(mostrar)