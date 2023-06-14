from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, TIPO_OPERACION_LOGICA, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class Logica(Expresion):
    def __init__(self, exp1, exp2, operador, fila, columna, negacion = False):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.fila = fila
        self.columna = columna
        self.negacion = negacion

    def ejecutar(self, entorno, helper):
        val1 = Retorno()
        val2 = Retorno()
        valNegacion = Retorno()

        if self.negacion:
            valNegacion = self.exp1.ejecutar(entorno, helper)
            valNegacion.valor = not valNegacion.valor
            return valNegacion
        
        val1 = self.exp1.ejecutar(entorno, helper)
        val2 = self.exp2.ejecutar(entorno, helper)

        if self.operador == TIPO_OPERACION_LOGICA.AND:
            if val1.tipo == val2.tipo == TIPO_DATO.BOOLEANO:
                #print("ENTREEEEEEEEEEEE AL AND")
                #print(val1.valor and val2.valor)
                return Retorno(val1.valor and val2.valor, TIPO_DATO.BOOLEANO)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación lógica AND con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                return Retorno(None,None)

        elif self.operador == TIPO_OPERACION_LOGICA.OR:
            if val1.tipo == val2.tipo == TIPO_DATO.BOOLEANO:
                #print("ENTREEEEEEEEEE AL ORRRRRRRRR")
                return Retorno(val1.valor or val2.valor, TIPO_DATO.BOOLEANO)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación lógica OR con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                return Retorno(None,None)

    def genArbol(self):
        if self.negacion:
            nodo = Nodo("!")
            nodo.agregarHijo(self.exp1.genArbol())
            return nodo
        
        if self.operador == TIPO_OPERACION_LOGICA.AND:
            nodo = Nodo("&&")
            nodo.agregarHijo(self.exp1.genArbol())
            nodo.agregarHijo(self.exp2.genArbol())
            return nodo
        elif self.operador == TIPO_OPERACION_LOGICA.OR:
            nodo = Nodo("||")
            nodo.agregarHijo(self.exp1.genArbol())
            nodo.agregarHijo(self.exp2.genArbol())
            return nodo
        
            
        