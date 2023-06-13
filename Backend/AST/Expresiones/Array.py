from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno
from AST.Expresiones.Llamada import Llamada

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
        if not isinstance(self.expresiones, Llamada):
            print("RETOR: ")
            print(self.expresiones)
            for exp in self.expresiones:
                arr.append(exp.ejecutar(entorno, helper))
            retor = Retorno(arr, TIPO_DATO.ARRAY)
            return retor
        else:
            print("HOLAAAAAAAAAAAAAAAAAAAAAAAAA")
            a = self.expresiones.ejecutar(entorno, helper)
            print(a)
            print("------------------------------")
            return self.expresiones.ejecutar(entorno, helper)
    
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