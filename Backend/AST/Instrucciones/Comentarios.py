from AST.Abstract.Instruccion import Instruccion
from AST.Nodo import Nodo


class Comentarios(Instruccion):
    def __init__(self, comentario, linea, columna):
        self.comentario = comentario
        self.linea = linea
        self.columna = columna
        super().__init__()

    def ejecutar(self, entorno, helper):
        pass
    def genC3D(self, entorno, helper):
        pass
    def genArbol(self):
        pass