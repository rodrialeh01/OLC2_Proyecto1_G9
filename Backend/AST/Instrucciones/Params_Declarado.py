from AST.Abstract.Expresion import Expresion


class Params_Declarado(Expresion):
    def __init__(self, id, expresion, linea, columna):
        self.id = id
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        

    def ejecutar(self, entorno, helper):
        return self
        