from AST.Abstract.Instruccion import Instruccion
from AST.Nodo import Nodo
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

    def genArbol(self) -> Nodo:
        nodo = Nodo("CREAR INTERFACE")
        nodo.agregarHijo(self.id)
        atribs = Nodo("ATRIBUTOS")
        if self.listaParametros != None:
            atribs.agregarHijo(self.listaParametros.genArbol())
        nodo.agregarHijo(atribs)
        return nodo