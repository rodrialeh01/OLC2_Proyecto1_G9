from AST.Abstract.Instruccion import Instruccion
from AST.Nodo import Nodo


class Return(Instruccion):
    def __init__(self, valor, fila, columna):
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        if helper.getFuncion() == "Funcion":
            if self.valor != None:
                print("RETURN CON VALOR")
                valor = self.valor.ejecutar(entorno, helper)
                return valor
            else:
                print("RETURN VACIO")
                return self
        else:
            pass

    def genArbol(self) -> Nodo:
        if self.valor != None:
            nodo = Nodo("RETURN")
            nodo.addHijoValor(self.valor.genArbol())
            return nodo
        else:
            nodo = Nodo("RETURN")
            return nodo