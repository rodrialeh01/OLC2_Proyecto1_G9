from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno


class ToString(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        valor = self.expresion.ejecutar(entorno, helper)
        if valor.tipo == TIPO_DATO.ARRAY or valor.tipo == TIPO_DATO.ARRAY_NUMBER or valor.tipo == TIPO_DATO.ARRAY_STRING or valor.tipo == TIPO_DATO.ARRAY_BOOLEAN:
            arr = []
            arr = self.StringArrays(arr, valor.valor)
            return Retorno(str(arr), TIPO_DATO.CADENA)
        return Retorno(str(valor.valor), TIPO_DATO.CADENA)
        
    def genArbol(self) -> Nodo:
        nodo = Nodo("TO_STRING")
        nodo.agregarHijo(Nodo("("))
        nodo.agregarHijo(self.expresion.genArbol())
        nodo.agregarHijo(Nodo(")"))

        return nodo

    def StringArrays(self, arr, arrexist):
        for a in arrexist:
            if a.tipo == TIPO_DATO.ARRAY or a.tipo == TIPO_DATO.ARRAY_NUMBER or a.tipo == TIPO_DATO.ARRAY_STRING or a.tipo == TIPO_DATO.ARRAY_BOOLEAN:
                arr2 = []
                arr2 = self.ImpresionArrays(arr2, a.valor)
                arr.append(arr2)
            else:
                arr.append(a.valor)
        return arr