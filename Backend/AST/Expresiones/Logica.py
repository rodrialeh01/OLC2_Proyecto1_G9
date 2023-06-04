from AST.Abstract.Expresion import Expresion
from AST.Simbolos.Enums import TIPO_DATO, TIPO_OPERACION_LOGICA
from AST.Simbolos.Retorno import Retorno


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
                return Retorno(val1.valor and val2.valo, TIPO_DATO.BOOLEANO)
            else:
                pass

        elif self.operador == TIPO_OPERACION_LOGICA.OR:
            if val1.tipo == val2.tipo == TIPO_DATO.BOOLEANO:
                return Retorno(val1.valor or val2.valo, TIPO_DATO.BOOLEANO)
            else:
                pass
            
        