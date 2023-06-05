from AST.Abstract.Instruccion import Instruccion


class Break(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        if helper.getCiclo() == "ciclo":
            return self
        else:
            pass