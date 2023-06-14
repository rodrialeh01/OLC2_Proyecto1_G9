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
        print("HOLA SOY EL SPLIT ")
        existe = entorno.ExisteSimbolo(self.expresion)        
        if existe == False:
            pass
        else:
            cadena = entorno.ObtenerSimbolo(self.expresion)
            print(cadena)
            separador = self.separador.ejecutar(entorno, helper)
            if cadena.tipo != TIPO_DATO.CADENA or separador.tipo != TIPO_DATO.CADENA:
                #error semantico
                pass
            new_array = []
            for i in str(cadena.valor).split(separador.valor):
                new_array.append(Retorno(i, TIPO_DATO.CADENA))

            print("EL ARRAY: ", new_array)
            return Retorno(new_array, TIPO_DATO.ARRAY_STRING)

    def genArbol(self) -> Nodo:
        nodo = Nodo("SPLIT")
        nodo.agregarHijo(self.expresion.genArbol())
        nodo.agregarHijo(Nodo("."))
        nodo.agregarHijo(Nodo("split"))
        nodo.agregarHijo(Nodo("("))
        nodo.agregarHijo(self.separador.genArbol())
        nodo.agregarHijo(Nodo(")"))
        return nodo
