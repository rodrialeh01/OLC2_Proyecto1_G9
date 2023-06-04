from AST.Abstract.Expresion import Expresion
from AST.Simbolos.Enums import TIPO_DATO, TIPO_OPERACION_ARITMETICA
from AST.Simbolos.Retorno import Retorno


class Operacion(Expresion):
    def __init__(self, exp1, exp2, operador, fila, columna, unario = False):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.fila = fila
        self.columna = columna
        self.unario = unario

    def ejecutar(self, entorno, helper) -> Retorno:
        val1 = Retorno()
        val2 = Retorno()
        valUnario = Retorno()

        #Validando el numero negativo (UNARIO)
        if self.unario:
            valUnario = self.exp1.ejecutar(entorno, helper)
            valUnario.valor = valUnario.valor * -1
            return valUnario
        
        val1 = self.exp1.ejecutar(entorno, helper)
        val2 = self.exp2.ejecutar(entorno, helper)

        # Validando las distintas operaciones aritméticas
        #MAS
        if self.operador == TIPO_OPERACION_ARITMETICA.SUMA:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor + val2.valor, TIPO_DATO.NUMERO)
            elif val1.tipo == val2.tipo == TIPO_DATO.CADENA:
                return Retorno(val1.valor + val2.valor, TIPO_DATO.CADENA)
            else:
                pass
        #MENOS
        elif self.operador == TIPO_OPERACION_ARITMETICA.RESTA:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor - val2.valor, TIPO_DATO.NUMERO)
            else:
                pass
        #POR
        elif self.operador == TIPO_OPERACION_ARITMETICA.MULTIPLICACION:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor * val2.valor, TIPO_DATO.NUMERO)
            else:
                pass
        #DIVIDIDO
        elif self.operador == TIPO_OPERACION_ARITMETICA.DIVISION:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                if val2.tipo != 0:
                    return Retorno(val1.valor / val2.valor, TIPO_DATO.NUMERO)
                else:
                    pass
            else:
                pass
        #POTENCIA
        elif self.operador == TIPO_OPERACION_ARITMETICA.POTENCIA:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor ** val2.valor, TIPO_DATO.NUMERO)
            else:
                pass
        #MODULO
        elif self.operador == TIPO_OPERACION_ARITMETICA.MODULO:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor % val2.valor, TIPO_DATO.NUMERO)
            else:
                pass

