from AST.Abstract.Instruccion import Instruccion
from AST.Nodo import Nodo


class AsignarInterface(Instruccion):
    def __init__(self, id_interface,id_param,expresion, linea, columna):
        self.id_interface = id_interface
        self.id_param = id_param
        self.expresion = expresion
        self.linea = linea
        self.columna = columna


    def ejecutar(self, entorno, helper):
        existe = entorno.ExisteInterfaceDeclarada(self.id_interface)
        if not existe:
            return
        objeto = entorno.ObtenerInterfaceDeclarada(self.id_interface)
        for p in objeto.paramDeclarados:
            if self.id_param in p:
                if p[self.id_param].tipo != self.expresion.tipo:
                    pass
                    return
                p[self.id_param].valor = self.expresion.ejecutar(entorno,helper).valor
                entorno.ActualizarInterfaceDeclarada(self.id_interface, objeto)
                return
                
        #error semantico

    def genArbol(self) -> Nodo:
        nodo = Nodo("ASIGNAR INTERFACE")
        nodo.agregarHijo(Nodo(self.id_interface))
        nodo.agregarHijo(Nodo("."))
        nodo.agregarHijo(Nodo(self.id_param))
        nodo.agregarHijo(Nodo("="))
        nodo.agregarHijo(self.expresion.genArbol())
        return nodo



