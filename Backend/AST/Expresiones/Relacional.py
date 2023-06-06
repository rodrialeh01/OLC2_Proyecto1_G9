from AST.Abstract.Expresion import Expresion
from AST.Simbolos.Enums import TIPO_DATO, TIPO_OPERACION_RELACIONAL
from AST.Simbolos.Retorno import Retorno


class Relacional(Expresion):
    def __init__(self, exp1, exp2, operador, fila, columna):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        val1 = Retorno()
        val2 = Retorno()

        val1 = self.exp1.ejecutar(entorno, helper)
        val2 = self.exp2.ejecutar(entorno, helper)

        if self.operador == TIPO_OPERACION_RELACIONAL.MAYOR_QUE:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor > val2.valor, TIPO_DATO.BOOLEANO)
            else:
                pass

        elif self.operador == TIPO_OPERACION_RELACIONAL.MENOR_QUE:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor < val2.valor, TIPO_DATO.BOOLEANO)
            else:
                pass
            
        elif self.operador == TIPO_OPERACION_RELACIONAL.MAYOR_IGUAL_QUE:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor >= val2.valor, TIPO_DATO.BOOLEANO)
            else:
                pass

        elif self.operador == TIPO_OPERACION_RELACIONAL.MENOR_IGUAL_QUE:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor <= val2.valor, TIPO_DATO.BOOLEANO)
            else:
                pass

        elif self.operador == TIPO_OPERACION_RELACIONAL.IGUAL_IGUAL:
            if val1.tipo == val2.tipo:
                return Retorno(val1.valor == val2.valor, TIPO_DATO.BOOLEANO)
            else:
                pass

        elif self.operador == TIPO_OPERACION_RELACIONAL.DIFERENTE:
            if val1.tipo == val2.tipo:
                return Retorno(val1.valor != val2.valor, TIPO_DATO.BOOLEANO)
            else:
                pass

    
