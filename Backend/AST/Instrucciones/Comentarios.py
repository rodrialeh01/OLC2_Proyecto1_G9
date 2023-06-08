from AST.Abstract.Instruccion import Instruccion


class Comentarios(Instruccion):
    def __init__(self, comentario, linea, columna):
        self.comentario = comentario
        self.linea = linea
        self.columna = columna

    def ejecutar(self, entorno, helper):
        pass