from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno


class ToString(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        super().__init__()

    def ejecutar(self, entorno, helper):
        #print("TO STRING")
        #print(self.expresion)
        if isinstance(self.expresion, str):
            #buscar el ID en la tabla de simbolos:
            valor = entorno.ObtenerSimbolo(self.expresion)
            if valor == None:
                print("Error: variable " + self.expresion + " no encontrada")
                return
        else:
            valor = self.expresion.ejecutar(entorno, helper)
        if valor.tipo == TIPO_DATO.ARRAY or valor.tipo == TIPO_DATO.ARRAY_NUMBER or valor.tipo == TIPO_DATO.ARRAY_STRING or valor.tipo == TIPO_DATO.ARRAY_BOOLEAN:
            arr = []
            arr = self.StringArrays(arr, valor.valor)
            return Retorno(str(arr), TIPO_DATO.CADENA)
        print(valor.valor)
        return Retorno(str(valor.valor), TIPO_DATO.CADENA)
        
    def genArbol(self) -> Nodo:
        nodo = Nodo("TO_STRING")
        if isinstance(self.expresion, str):
            nodo.agregarHijo(Nodo(self.expresion))
        else:
            nodo.agregarHijo(self.expresion.genArbol())

        return nodo

    def genC3D(self, entorno, helper):
        pass

    def StringArrays(self, arr, arrexist):
        for a in arrexist:
            if a.tipo == TIPO_DATO.ARRAY or a.tipo == TIPO_DATO.ARRAY_NUMBER or a.tipo == TIPO_DATO.ARRAY_STRING or a.tipo == TIPO_DATO.ARRAY_BOOLEAN:
                arr2 = []
                arr2 = self.ImpresionArrays(arr2, a.valor)
                arr.append(arr2)
            else:
                arr.append(a.valor)
        return arr