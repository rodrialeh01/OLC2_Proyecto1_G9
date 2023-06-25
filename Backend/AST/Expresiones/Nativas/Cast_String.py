from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno


class Cast_String(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        super().__init__()

    def ejecutar(self, entorno, helper):
        valor = self.expresion.ejecutar(entorno, helper)
        if valor.tipo == TIPO_DATO.ARRAY or valor.tipo == TIPO_DATO.ARRAY_NUMBER or valor.tipo == TIPO_DATO.ARRAY_STRING or valor.tipo == TIPO_DATO.ARRAY_BOOLEAN:
            arr = []
            arr = self.ToStringArrays(arr, valor.valor)
            salida = ""
            for a in range(len(arr)):
                if a == len(arr) - 1:
                    salida += str(arr[a])
                else:
                    salida += str(arr[a]) + ","
            return Retorno(str(salida), TIPO_DATO.CADENA)
        return Retorno(str(valor.valor), TIPO_DATO.CADENA)

    def genArbol(self):
        nodo = Nodo("STRING")
        nodo.agregarHijo(self.expresion.genArbol())
        return nodo
    
    def genC3D(self, entorno, helper):
        pass

    def ToStringArrays(self, arr, arrexist):
        for a in arrexist:
            if a.tipo == TIPO_DATO.ARRAY or a.tipo == TIPO_DATO.ARRAY_NUMBER or a.tipo == TIPO_DATO.ARRAY_STRING or a.tipo == TIPO_DATO.ARRAY_BOOLEAN:
                arr2 = []
                arr2 = self.ImpresionArrays(arr2, a.valor)
                arr.append(arr2)
            else:
                arr.append(a.valor)
        return arr