from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import (TIPO_DATO, TIPO_OPERACION_RELACIONAL,
                                obtTipoDato)
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Retorno2 import Retorno2
from AST.SingletonErrores import SingletonErrores


class Relacional(Expresion):
    
    def __init__(self, exp1, exp2, operador, fila, columna):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.fila = fila
        self.columna = columna
        super().__init__()

    def ejecutar(self, entorno, helper):
        val1 = Retorno()
        val2 = Retorno()

        val1 = self.exp1.ejecutar(entorno, helper)
        val2 = self.exp2.ejecutar(entorno, helper)

        if self.operador == TIPO_OPERACION_RELACIONAL.MAYOR_QUE:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor > val2.valor, TIPO_DATO.BOOLEANO)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación relacional MAYOR QUE con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: No se puede realizar la operación relacional MAYOR QUE con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None, TIPO_DATO.ERROR)

        elif self.operador == TIPO_OPERACION_RELACIONAL.MENOR_QUE:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor < val2.valor, TIPO_DATO.BOOLEANO)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación relacional MENOR QUE con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: No se puede realizar la operación relacional MENOR QUE con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None,TIPO_DATO.ERROR)
            
        elif self.operador == TIPO_OPERACION_RELACIONAL.MAYOR_IGUAL_QUE:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor >= val2.valor, TIPO_DATO.BOOLEANO)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación relacional MAYOR IGUAL QUE con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: No se puede realizar la operación relacional MAYOR IGUAL QUE con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None,TIPO_DATO.ERROR)

        elif self.operador == TIPO_OPERACION_RELACIONAL.MENOR_IGUAL_QUE:
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                return Retorno(val1.valor <= val2.valor, TIPO_DATO.BOOLEANO)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación relacional MENOR IGUAL QUE con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: No se puede realizar la operación relacional MENOR IGUAL QUE con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None,TIPO_DATO.ERROR)

        elif self.operador == TIPO_OPERACION_RELACIONAL.IGUAL_IGUAL:
            if val1.tipo == val2.tipo:
                return Retorno(val1.valor == val2.valor, TIPO_DATO.BOOLEANO)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación relacional IGUALACIÓN con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: No se puede realizar la operación relacional IGUALACIÓN con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None,TIPO_DATO.ERROR)

        elif self.operador == TIPO_OPERACION_RELACIONAL.DIFERENTE:
            if val1.tipo == val2.tipo:
                return Retorno(val1.valor != val2.valor, TIPO_DATO.BOOLEANO)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se puede realizar la operación relacional DIFERENTE con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: No se puede realizar la operación relacional DIFERENTE con los tipos de datos: " + obtTipoDato(val1.tipo) + " y " + obtTipoDato(val2.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None,TIPO_DATO.ERROR)

    def genArbol(self):
        if self.operador == TIPO_OPERACION_RELACIONAL.MAYOR_QUE:
            nodo = Nodo(">")
        elif self.operador == TIPO_OPERACION_RELACIONAL.MENOR_QUE:
            nodo = Nodo("<")
        elif self.operador == TIPO_OPERACION_RELACIONAL.MAYOR_IGUAL_QUE:
            nodo = Nodo(">=")
        elif self.operador == TIPO_OPERACION_RELACIONAL.MENOR_IGUAL_QUE:
            nodo = Nodo("<=")
        elif self.operador == TIPO_OPERACION_RELACIONAL.IGUAL_IGUAL:
            nodo = Nodo("===")
        elif self.operador == TIPO_OPERACION_RELACIONAL.DIFERENTE:
            nodo = Nodo("!==")
        
        nodo.agregarHijo(self.exp1.genArbol())
        nodo.agregarHijo(self.exp2.genArbol())
        return nodo
    
    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()
        temporalizq = ''
        temporalder = ''
        operador = ''

        val1 = self.exp1.genC3D(entorno, helper)
        val2 = self.exp2.genC3D(entorno, helper)

        retorno = Retorno2(None, TIPO_DATO.BOOLEANO, False)

        if self.operador == TIPO_OPERACION_RELACIONAL.MAYOR_QUE:
            operador = '>'
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                # Label para primer goto
                Lbltrue = generador.newLabel() 
                Lblfalse = generador.newLabel()

                #crea los temporales para las expresiones
                temporalizq = generador.addTemp()
                temporalder = generador.addTemp()
                generador.addExpresion(temporalizq, val1.valor, '', '')
                generador.addExpresion(temporalder, val2.valor, '', '')


                generador.addIf(temporalizq, temporalder, operador, Lbltrue) # if a > b goto Lbltrue
                generador.addGoto(Lblfalse) # goto Lblfalse
                self.trueLabel = Lbltrue
                self.falseLabel = Lblfalse
                
                retorno.trueLabel = Lbltrue
                retorno.falseLabel = Lblfalse
                generador.putLabel(Lbltrue)
                generador.addIndent()
                generador.addPrint('d',1)
                generador.putLabel(Lblfalse)
                generador.addIndent()
                generador.addPrint('d',0)

                return retorno
        elif self.operador == TIPO_OPERACION_RELACIONAL.MENOR_QUE:
            operador = '<'
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                # Label para primer goto
                Lbltrue = generador.newLabel() 
                Lblfalse = generador.newLabel()

                #crea los temporales para las expresiones
                temporalizq = generador.addTemp()
                temporalder = generador.addTemp()
                generador.addExpresion(temporalizq, val1.valor, '', '')
                generador.addExpresion(temporalder, val2.valor, '', '')


                generador.addIf(temporalizq, temporalder, operador, Lbltrue) # if a > b goto Lbltrue
                generador.addGoto(Lblfalse) # goto Lblfalse
                self.trueLabel = Lbltrue
                self.falseLabel = Lblfalse
                
                retorno.trueLabel = Lbltrue
                retorno.falseLabel = Lblfalse
                generador.putLabel(Lbltrue)
                generador.addIndent()
                generador.addPrint('d',1)
                generador.putLabel(Lblfalse)
                generador.addIndent()
                generador.addPrint('d',0)

                return retorno
        elif self.operador == TIPO_OPERACION_RELACIONAL.MAYOR_IGUAL_QUE:
            operador = '>='
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                # Label para primer goto
                Lbltrue = generador.newLabel()
                Lblfalse = generador.newLabel()

                #crea los temporales para las expresiones
                temporalizq = generador.addTemp()
                temporalder = generador.addTemp()
                generador.addExpresion(temporalizq, val1.valor, '', '')
                generador.addExpresion(temporalder, val2.valor, '', '')


                generador.addIf(temporalizq, temporalder, operador, Lbltrue) # if a > b goto Lbltrue
                generador.addGoto(Lblfalse) # goto Lblfalse
                self.trueLabel = Lbltrue
                self.falseLabel = Lblfalse
                
                retorno.trueLabel = Lbltrue
                retorno.falseLabel = Lblfalse
                generador.putLabel(Lbltrue)
                generador.addIndent()
                generador.addPrint('d',1)
                generador.putLabel(Lblfalse)
                generador.addIndent()
                generador.addPrint('d',0)

                return retorno
        elif self.operador == TIPO_OPERACION_RELACIONAL.MENOR_IGUAL_QUE:
            operador = '<='
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                # Label para primer goto
                Lbltrue = generador.newLabel()
                Lblfalse = generador.newLabel()

                #crea los temporales para las expresiones
                temporalizq = generador.addTemp()
                temporalder = generador.addTemp()
                generador.addExpresion(temporalizq, val1.valor, '', '')
                generador.addExpresion(temporalder, val2.valor, '', '')


                generador.addIf(temporalizq, temporalder, operador, Lbltrue) # if a > b goto Lbltrue
                generador.addGoto(Lblfalse) # goto Lblfalse
                self.trueLabel = Lbltrue
                self.falseLabel = Lblfalse
                
                retorno.trueLabel = Lbltrue
                retorno.falseLabel = Lblfalse
                generador.putLabel(Lbltrue)
                generador.addIndent()
                generador.addPrint('d',1)
                generador.putLabel(Lblfalse)
                generador.addIndent()
                generador.addPrint('d',0)

                return retorno
        elif self.operador == TIPO_OPERACION_RELACIONAL.IGUAL_IGUAL:
            operador = '=='
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                # Label para primer goto
                Lbltrue = generador.newLabel()
                Lblfalse = generador.newLabel()

                #crea los temporales para las expresiones
                temporalizq = generador.addTemp()
                temporalder = generador.addTemp()
                generador.addExpresion(temporalizq, val1.valor, '', '')
                generador.addExpresion(temporalder, val2.valor, '', '')


                generador.addIf(temporalizq, temporalder, operador, Lbltrue) # if a > b goto Lbltrue
                generador.addGoto(Lblfalse) # goto Lblfalse
                self.trueLabel = Lbltrue
                self.falseLabel = Lblfalse
                
                retorno.trueLabel = Lbltrue
                retorno.falseLabel = Lblfalse
                generador.putLabel(Lbltrue)
                generador.addIndent()
                generador.addPrint('d',1)
                generador.putLabel(Lblfalse)
                generador.addIndent()
                generador.addPrint('d',0)

                return retorno
        elif self.operador == TIPO_OPERACION_RELACIONAL.DIFERENTE:
            operador = '!='
            if val1.tipo == val2.tipo == TIPO_DATO.NUMERO:
                # Label para primer goto
                Lbltrue = generador.newLabel()
                Lblfalse = generador.newLabel()

                #crea los temporales para las expresiones
                temporalizq = generador.addTemp()
                temporalder = generador.addTemp()
                generador.addExpresion(temporalizq, val1.valor, '', '')
                generador.addExpresion(temporalder, val2.valor, '', '')


                generador.addIf(temporalizq, temporalder, operador, Lbltrue) # if a > b goto Lbltrue
                generador.addGoto(Lblfalse) # goto Lblfalse
                self.trueLabel = Lbltrue
                self.falseLabel = Lblfalse
                
                retorno.trueLabel = Lbltrue
                retorno.falseLabel = Lblfalse
                generador.putLabel(Lbltrue)
                generador.addIndent()
                generador.addPrint('d',1)
                generador.putLabel(Lblfalse)
                generador.addIndent()
                generador.addPrint('d',0)

                return retorno
        
