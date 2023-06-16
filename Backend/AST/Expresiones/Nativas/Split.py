from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class Split(Expresion):
    def __init__(self, expresion, separador, fila, columna):
        self.expresion = expresion
        self.separador = separador
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        cadena = self.expresion.ejecutar(entorno, helper)
        separador = self.separador.ejecutar(entorno, helper)
        #print(separador.valor)
        if cadena.tipo != TIPO_DATO.CADENA or separador.tipo != TIPO_DATO.CADENA:
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "No es posible realizar split con una variable de tipo " + obtTipoDato(cadena.tipo) + " y un separador de tipo " + obtTipoDato(separador.tipo) )
            s.addError(err)
            #print("[ERROR]: No es posible realizar split con una variable de tipo " + obtTipoDato(cadena.tipo) + " y un separador de tipo " + obtTipoDato(separador.tipo)+" en la línea " + str(self.fila) + " y columna "+ str(self.columna))
            helper.setConsola("[ERROR]: No es posible realizar split con una variable de tipo " + obtTipoDato(cadena.tipo) + " y un separador de tipo " + obtTipoDato(separador.tipo)+" en la línea " + str(self.fila) + " y columna "+ str(self.columna) )
            return Retorno(None, TIPO_DATO.ERROR)
        
        new_array = []
        if separador.valor == "":
            for i in str(cadena.valor):
                new_array.append(Retorno(i, TIPO_DATO.CADENA))  
        else:
            for i in str(cadena.valor).split(separador.valor):
                new_array.append(Retorno(i, TIPO_DATO.CADENA))

        return Retorno(new_array, TIPO_DATO.ARRAY_STRING)

    def genArbol(self) -> Nodo:
        nodo = Nodo("SPLIT")
        nodo.agregarHijo(self.expresion.genArbol())
        nodo.agregarHijo(self.separador.genArbol())
        return nodo
