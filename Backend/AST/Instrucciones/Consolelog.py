from AST.Abstract.Instruccion import Instruccion


class Consolelog(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        
    def ejecutar(self, entorno, helper):
        val = self.expresion.ejecutar(entorno, helper)
        helper.setConsola(val.valor)
        print(val.valor)
        