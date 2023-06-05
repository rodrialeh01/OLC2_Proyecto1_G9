from AST.Abstract.Instruccion import Instruccion


class Return(Instruccion):
    def __init__(self, valor, fila, columna):
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        if helper.getFuncion() == "funcion":
            if self.valor != None:
                valor = self.valor.ejecutar(entorno, helper)
                return valor
            else:
                return self
        else:
            pass