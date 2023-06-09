from AST.Abstract.Instruccion import Instruccion
from AST.Simbolos.Simbolo import Simbolo


class Interface(Simbolo, Instruccion):
    def __init__(self, id, listaParametros, linea, columna):
        self.id = id
        self.listaParametros = listaParametros
        self.linea = linea
        self.columna = columna

        super().__init__()
    
    def ejecutar(self, entorno, helper):
        self.crearInterface(self.id, self.listaParametros, self.linea, self.columna);
        verif = entorno.ExisteInterface(self.id)
        if not verif:
            entorno.AgregarInterface(self.id , self)