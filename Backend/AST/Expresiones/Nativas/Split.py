from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno


class Split(Expresion):
    def __init__(self, expresion, separador, fila, columna):
        self.expresion = expresion
        self.separador = separador
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        '''
        #PENDIENTE POR EL DATATYPE QUE RETORNA

        cadena = self.expresion.ejecutar(entorno, helper)
        separador = self.separador.ejecutar(entorno, helper)
        if cadena.tipo != TIPO_DATO.CADENA or separador.tipo != TIPO_DATO.CADENA:
            #error semantico
            pass

        return Retorno(str(cadena.valor).split(separador), TIPO_DATO.ARREGLO)
        '''
        pass

    def genArbol(self) -> Nodo:
        nodo = Nodo("SPLIT")
        nodo.agregarHijo(self.expresion.genArbol())
        nodo.agregarHijo(Nodo("."))
        nodo.agregarHijo(Nodo("split"))
        nodo.agregarHijo(Nodo("("))
        nodo.agregarHijo(self.separador.genArbol())
        nodo.agregarHijo(Nodo(")"))
        return nodo
