from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno


class Concat(Expresion):
    def __init__(self, expresion1, expresion2, fila, columna):
        self.expresion1 = expresion1
        self.expresion2 = expresion2
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        print("ENTRE EN EL CONCAT")
        print(self.expresion1)
        print(self.expresion2)
        
        existe = entorno.ExisteSimbolo(self.expresion1)
        print(existe)
        #suponiendo que si se puedan tambien cadenas que es un array de caracteres
        if existe == False:
            pass
        else:
            valor1 = entorno.ObtenerSimbolo(self.expresion1)
            valor2 = self.expresion2.ejecutar(entorno, helper)
            print(valor2)
            if valor1.tipo == TIPO_DATO.CADENA and valor2.tipo == TIPO_DATO.CADENA:
                return Retorno(str(valor1.valor) + str(valor2.valor), TIPO_DATO.CADENA)
            elif valor1.tipo == TIPO_DATO.ARRAY_STRING or valor1.tipo == TIPO_DATO.ARRAY and valor2.tipo == TIPO_DATO.ARRAY_STRING or valor2.tipo == TIPO_DATO.ARRAY:
                return Retorno(valor1.valor + valor2.valor, TIPO_DATO.ARRAY_STRING)
            elif valor1.tipo == TIPO_DATO.ARRAY_NUMBER or valor1.tipo == TIPO_DATO.ARRAY and valor2.tipo == TIPO_DATO.ARRAY_NUMBER or valor2.tipo == TIPO_DATO.ARRAY:
                return Retorno(valor1.valor + valor2.valor, TIPO_DATO.ARRAY_NUMBER)
            elif valor1.tipo == TIPO_DATO.ARRAY_BOOLEAN or valor1.tipo == TIPO_DATO.ARRAY and valor2.tipo == TIPO_DATO.ARRAY_BOOLEAN or valor2.tipo == TIPO_DATO.ARRAY:
                return Retorno(valor1.valor + valor2.valor, TIPO_DATO.ARRAY_BOOLEAN)
        
    def genArbol(self) -> Nodo:
        nodo = Nodo("CONCATENACION")
        nodo.addHijoNodo(self.expresion1.genArbol())
        nodo.addHijoNodo(Nodo("."))
        nodo.addHijoNodo(Nodo("concat"))
        nodo.addHijoNodo(Nodo("("))
        nodo.addHijoNodo(self.expresion2.genArbol())
        nodo.addHijoNodo(Nodo(")"))
        return nodo