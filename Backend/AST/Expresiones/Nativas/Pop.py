from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class Pop(Expresion):
    def __init__(self, arreglo, fila, columna):
        self.arreglo = arreglo
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        array = self.arreglo.ejecutar(entorno, helper)
        if array.tipo == TIPO_DATO.ERROR:
            return array
        
        if not isinstance(array.valor, list):
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "No es posible hacer un 'pop' para una expresión de tipo " + obtTipoDato(array.tipo) + " en la línea " + str(self.linea) +  " y columna "+ str(self.columna) +"." )
            s.addError(err)
            helper.setConsola("[ERROR]: No es posible hacer un 'pop' para una expresión de tipo " + obtTipoDato(array.tipo) + " en la línea " + str(self.linea) +  " y columna "+ str(self.columna) )
            return Retorno(None, TIPO_DATO.ERROR)
        
        if len(array.valor) == 0:
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "No es posible hacer un 'pop' para un arreglo vacío en la línea " + str(self.linea) +  " y columna "+ str(self.columna) +"." )
            s.addError(err)
            helper.setConsola("[ERROR]: No es posible hacer un 'pop' para un arreglo vacío en la línea " + str(self.linea) +  " y columna "+ str(self.columna) )
            return Retorno(None, TIPO_DATO.ERROR)
        
        if array.tipo == TIPO_DATO.ARRAY_BOOLEAN:
            return Retorno(array.valor.pop().valor, TIPO_DATO.BOOLEANO)
        elif array.tipo == TIPO_DATO.ARRAY_NUMBER:
            return Retorno(array.valor.pop().valor, TIPO_DATO.NUMERO)
        elif array.tipo == TIPO_DATO.ARRAY_STRING:
            return Retorno(array.valor.pop().valor, TIPO_DATO.CADENA)
        elif array.tipo == TIPO_DATO.ARRAY:
            return Retorno(array.valor.pop().valor, TIPO_DATO.ANY)
        elif array.tipo == TIPO_DATO.ARRAY_INTERFACE:
            return Retorno(array.valor.pop().valor, TIPO_DATO.INTERFACE)


    def genArbol(self):
        pass

    def genC3D(self, entorno, helper):
        pass
        