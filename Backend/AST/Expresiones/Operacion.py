from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import (TIPO_DATO, TIPO_OPERACION_ARITMETICA,
                                obtTipoDato)
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Retorno2 import Retorno2
from AST.SingletonErrores import SingletonErrores


class Operacion(Expresion):
    def __init__(self, exp1, exp2, operador, fila, columna, unario = False):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.fila = fila
        self.columna = columna
        self.unario = unario
        super().__init__()


    def ejecutar(self, entorno, helper) -> Retorno:
        val1 = Retorno()
        val2 = Retorno()
        valUnario = Retorno()

        #Validando el numero negativo (UNARIO)
        if self.unario:
            
            valUnario = self.exp1.ejecutar(entorno, helper)
            valUnario.valor = valUnario.valor * -1
            return valUnario
        
        ##print(self.exp1)
        ##print(self.exp2)
        
        val1 = self.exp1.ejecutar(entorno, helper)
        val2 = self.exp2.ejecutar(entorno, helper)

        # Validando las distintas operaciones aritméticas
        #MAS
        if self.operador == TIPO_OPERACION_ARITMETICA.SUMA:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                ##print(str(val1.valor) + " + " + str(val2.valor))
                ##print(str(val1.valor + val2.valor))
                return Retorno(val1.valor + val2.valor, TIPO_DATO.NUMERO)
            elif val1.tipo == val2.tipo == TIPO_DATO.CADENA:
                return Retorno(val1.valor + val2.valor, TIPO_DATO.CADENA)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación Aritmetica SUMA con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: No se puede realizar la operación Aritmetica SUMA con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None,TIPO_DATO.ERROR)
        #MENOS
        elif self.operador == TIPO_OPERACION_ARITMETICA.RESTA:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                ##print(str(val1.valor) + " - " + str(val2.valor))
                ##print(str(val1.valor - val2.valor))
                return Retorno(val1.valor - val2.valor, TIPO_DATO.NUMERO)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación Aritmetica RESTA con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: No se puede realizar la operación Aritmetica RESTA con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None,TIPO_DATO.ERROR)
        #POR
        elif self.operador == TIPO_OPERACION_ARITMETICA.MULTIPLICACION:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor * val2.valor, TIPO_DATO.NUMERO)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación Aritmetica MULTIPLICACIÓN con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: No se puede realizar la operación Aritmetica MULTIPLICACIÓN con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None,TIPO_DATO.ERROR)
        #DIVIDIDO
        elif self.operador == TIPO_OPERACION_ARITMETICA.DIVISION:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                if val2.tipo != 0:
                    return Retorno(val1.valor / val2.valor, TIPO_DATO.NUMERO)
                else:
                    s = SingletonErrores.getInstance()
                    err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación Aritmética DIVISIÓN con el valor 0")
                    s.addError(err)
                    helper.setConsola("[ERROR]: No se puede realizar la operación Aritmética DIVISIÓN con el valor 0 en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                    return Retorno(None,TIPO_DATO.ERROR)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación Aritmpetica MULTIPLICACIÓN con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: No se puede realizar la operación Aritmpetica MULTIPLICACIÓN con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None,TIPO_DATO.ERROR)
        #POTENCIA
        elif self.operador == TIPO_OPERACION_ARITMETICA.POTENCIA:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor ** val2.valor, TIPO_DATO.NUMERO)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación Aritmetica POTENCIA con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: No se puede realizar la operación Aritmetica POTENCIA con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None,TIPO_DATO.ERROR)
        #MODULO
        elif self.operador == TIPO_OPERACION_ARITMETICA.MODULO:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor % val2.valor, TIPO_DATO.NUMERO)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación Aritmetica MODULO con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: No se puede realizar la operación Aritmetica MODULO con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None,TIPO_DATO.ERROR)

    def genArbol(self):
        if self.unario:
            nodo = Nodo("-")
            nodo.agregarHijo(self.exp1.genArbol())
            return nodo

        if self.operador == TIPO_OPERACION_ARITMETICA.SUMA:
            nodo = Nodo("+")
        elif self.operador == TIPO_OPERACION_ARITMETICA.RESTA:
            nodo = Nodo("-")
        elif self.operador == TIPO_OPERACION_ARITMETICA.MULTIPLICACION:
            nodo = Nodo("*")
        elif self.operador == TIPO_OPERACION_ARITMETICA.DIVISION:
            nodo = Nodo("/")
        elif self.operador == TIPO_OPERACION_ARITMETICA.POTENCIA:
            nodo = Nodo("^")
        elif self.operador == TIPO_OPERACION_ARITMETICA.MODULO:
            nodo = Nodo("%")
        
        nodo.agregarHijo(self.exp1.genArbol())
        nodo.agregarHijo(self.exp2.genArbol())
        return nodo
    
    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()
        temporal = ''
        operador = ''
        val1 = self.exp1.genC3D(entorno, helper)
        val2 = self.exp2.genC3D(entorno, helper)
        if self.operador == TIPO_OPERACION_ARITMETICA.SUMA:
            operador = '+'
            temporal = generador.addTemp()
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                generador.addExpresion(temporal, val1.valor, val2.valor, operador)
            elif val1.tipo == val2.tipo == TIPO_DATO.CADENA:
                pass
            return Retorno2(temporal, TIPO_DATO.NUMERO, True)
        
        elif self.operador == TIPO_OPERACION_ARITMETICA.RESTA:
            operador = '-'
            temporal = generador.addTemp()
            print('resta')
            print(val1)
            print(val2)
            generador.addExpresion(temporal, val1.valor, val2.valor, operador)
            return Retorno2(temporal, TIPO_DATO.NUMERO, True)
        
        elif self.operador == TIPO_OPERACION_ARITMETICA.MULTIPLICACION:
            operador = '*'
            temporal = generador.addTemp()
            generador.addExpresion(temporal, val1.valor, val2.valor, operador)
            return Retorno2(temporal, TIPO_DATO.NUMERO, True)
        elif self.operador == TIPO_OPERACION_ARITMETICA.DIVISION:
            operador = '/'
            temporal = generador.addTemp()
            generador.addExpresion(temporal, val1.valor, val2.valor, operador)
            return Retorno2(temporal, TIPO_DATO.NUMERO, True)
        elif self.operador == TIPO_OPERACION_ARITMETICA.POTENCIA:
            operador = '^'
            temporal = generador.addTemp()
            generador.addExpresion(temporal, val1.valor, val2.valor, operador)
            return Retorno2(temporal, TIPO_DATO.NUMERO, True)
        elif self.operador == TIPO_OPERACION_ARITMETICA.MODULO:
            operador = '%'
            temporal = generador.addTemp()
            generador.addExpresion(temporal, val1.valor, val2.valor, operador)
            return Retorno2(temporal, TIPO_DATO.NUMERO, True)
    