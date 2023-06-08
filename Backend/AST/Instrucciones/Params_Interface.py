from AST.Abstract.Instruccion import Instruccion


class Params_Interface(Instruccion):
    def __init__(self, id, tipo, linea, columna):
        self.id = id
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        

    def ejecutar(self, entorno, helper):
        print("PARAM: " , self.id , " - " , self.tipo)