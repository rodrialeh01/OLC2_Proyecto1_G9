from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class Length(Expresion):
    def  __init__(self, exp1, linea, columna):
        self.exp1 = exp1
        self.linea = linea
        self.columna = columna

    def ejecutar(self, entorno, helper):
        existe = entorno.ExisteSimbolo(self.exp1)
        if existe == False:
            return
        else:
            valor = entorno.ObtenerSimbolo(self.exp1)

            if valor.tipo == TIPO_DATO.NUMERO or valor.tipo == TIPO_DATO.BOOLEANO:
                s = SingletonErrores.getInstance()
                err = Error(self.linea, self.columna, "Error Semántico", "No es posible obtener 'length' para una variable de tipo " + str(obtTipoDato(valor.tipo)) +"." )
                s.addError(err)
                helper.setConsola("[ERROR]: No es posible obtener 'length' para una variable de tipo " + obtTipoDato(valor.tipo) + " en la línea " + str(self.linea) +  " y columna "+ str(self.columna) )
                return Retorno(None, TIPO_DATO.ERROR)
                
            return Retorno(len(valor.valor), TIPO_DATO.NUMERO)

    def genArbol(self):
        pass
        