from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class ToNumber(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        found = entorno.ObtenerSimbolo(self.expresion)
        if entorno.ExisteSimbolo(self.expresion):
            valor = found.valor
            try: 
                a = float(valor)
                return Retorno(a, TIPO_DATO.NUMERO)
            except:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No es posible convertir la expresión '" + str(valor) + "' de tipo "+ obtTipoDato(found.tipo)+" a tipo number."  )
                s.addError(err)
                helper.setConsola("[ERROR]: No es posible convertir la expresión '" + str(valor) + "' de tipo "+ obtTipoDato(found.tipo)+" a tipo number. En la línea " + str(self.fila) + " y columna "+ str(self.columna))
                return Retorno(None, TIPO_DATO.ERROR)
        else:
            try:
                valor = self.expresion.ejecutar(entorno, helper)
                return Retorno(float(valor.valor), TIPO_DATO.NUMERO)
            except:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No es posible convertir la expresión '" + str(valor.valor) + "' de tipo "+ obtTipoDato(valor.tipo)+" a tipo number."  )
                s.addError(err)
                helper.setConsola("[ERROR]: No es posible convertir la expresión '" + str(valor.valor) + "' de tipo "+ obtTipoDato(valor.tipo)+" a tipo number. En la línea " + str(self.fila) + " y columna "+ str(self.columna))
                return Retorno(None, TIPO_DATO.ERROR)
            
    def genArbol(self):
        pass