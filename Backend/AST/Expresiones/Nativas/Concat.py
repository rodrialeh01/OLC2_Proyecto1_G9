from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Expresiones.Identificador import Identificador
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Retorno2 import Retorno2
from AST.SingletonErrores import SingletonErrores


class Concat(Expresion):
    def __init__(self, expresion1, expresion2, fila, columna):
        self.expresion1 = expresion1
        self.expresion2 = expresion2
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        valor1 = self.expresion1.ejecutar(entorno, helper)
        valor2 = self.expresion2.ejecutar(entorno, helper)
        
        if valor1.tipo == TIPO_DATO.CADENA and valor2.tipo == TIPO_DATO.CADENA: #
            return Retorno(str(valor1.valor) + str(valor2.valor), TIPO_DATO.CADENA)
        elif valor1.tipo == TIPO_DATO.ARRAY_STRING: #
            if valor2.tipo == TIPO_DATO.CADENA:
                return Retorno(valor1.valor + [valor2], TIPO_DATO.ARRAY_STRING)
            elif valor2.tipo == TIPO_DATO.ARRAY_STRING:
                return Retorno(valor1.valor + valor2.valor, TIPO_DATO.ARRAY_STRING)
            elif valor2.tipo == TIPO_DATO.ARRAY:
                bandera = True
                bandera = self.Verificar_Tipos_array(valor2.valor, TIPO_DATO.CADENA, bandera)
                if bandera == None:
                    bandera = True
                if not bandera: 
                    s = SingletonErrores.getInstance()
                    err = Error(self.fila, self.columna, "Error Semántico", "No es posible realizar 'Concat'. Tipos no compatibles. Se esperaba un array de tipo string pero se obtuvo un array de tipo any." )
                    s.addError(err)
                    helper.setConsola("[ERROR]: No es posible realizar 'Concat'. Tipos no compatibles. Se esperaba un array tipo string pero se obtuvo un array de tipo any. en la línea " + str(self.fila) + " y columna "+ str(self.columna) )
                    return Retorno(None, TIPO_DATO.ERROR)

                return Retorno(valor1.valor + valor2.valor, TIPO_DATO.ARRAY_STRING)
        elif valor1.tipo == TIPO_DATO.ARRAY_NUMBER: #
            if valor2.tipo == TIPO_DATO.NUMERO:
                return Retorno(valor1.valor + [valor2.valor], TIPO_DATO.ARRAY_NUMBER)
            elif valor2.tipo == TIPO_DATO.ARRAY_NUMBER:
                return Retorno(valor1.valor + valor2.valor, TIPO_DATO.ARRAY_NUMBER)
            elif valor2.tipo == TIPO_DATO.ARRAY:
                bandera = True
                bandera = self.Verificar_Tipos_array(valor2.valor, TIPO_DATO.NUMERO, bandera)
                if bandera == None:
                    bandera = True
                if not bandera: 
                    s = SingletonErrores.getInstance()
                    err = Error(self.fila, self.columna, "Error Semántico", "No es posible realizar 'Concat'. Tipos no compatibles. Se esperaba un array de tipo number pero se obtuvo un array de tipo any. " )
                    s.addError(err)
                    helper.setConsola("[ERROR]: No es posible realizar 'Concat'. Tipos no compatibles. Se esperaba un array tipo number pero se obtuvo un array de tipo any. en la línea " + str(self.fila) + " y columna "+ str(self.columna) )
                    return Retorno(None, TIPO_DATO.ERROR)

                return Retorno(valor1.valor + valor2.valor, TIPO_DATO.ARRAY_NUMBER)
        elif valor1.tipo == TIPO_DATO.ARRAY_BOOLEAN:
            if valor2.tipo == TIPO_DATO.BOOLEANO:
                return Retorno(valor1.valor + [valor2.valor], TIPO_DATO.ARRAY_BOOLEAN)
            elif valor2.tipo == TIPO_DATO.ARRAY_BOOLEAN:
                return Retorno(valor1.valor + valor2.valor, TIPO_DATO.ARRAY_BOOLEAN)
            elif valor2.tipo == TIPO_DATO.ARRAY:
                bandera = True
                bandera = self.Verificar_Tipos_array(valor2.valor, TIPO_DATO.BOOLEANO, bandera)
                if bandera == None:
                    bandera = True
                if not bandera: 
                    s = SingletonErrores.getInstance()
                    err = Error(self.fila, self.columna, "Error Semántico", "No es posible realizar 'Concat'. Tipos no compatibles. Se esperaba un array de tipo boolean pero se obtuvo un array de tipo any. " )
                    s.addError(err)
                    helper.setConsola("[ERROR]: No es posible realizar 'Concat'. Tipos no compatibles. Se esperaba un array tipo boolean pero se obtuvo un array de tipo any. en la línea " + str(self.fila) + " y columna "+ str(self.columna) )
                    return Retorno(None, TIPO_DATO.ERROR)
                    
                return Retorno(valor1.valor + valor2.valor, TIPO_DATO.ARRAY_BOOLEAN)
        elif valor1.tipo == TIPO_DATO.ARRAY:
                if valor2.tipo == TIPO_DATO.ARRAY or valor2.tipo == TIPO_DATO.ARRAY_NUMBER or valor2.tipo == TIPO_DATO.ARRAY_BOOLEAN or valor2.tipo == TIPO_DATO.ARRAY_STRING:
                    return Retorno(valor1.valor + valor2.valor, TIPO_DATO.ARRAY)
                elif valor2.tipo == TIPO_DATO.NUMERO or valor2.tipo == TIPO_DATO.BOOLEANO or valor2.tipo == TIPO_DATO.CADENA:
                    return Retorno(valor1.valor + [valor2.valor], TIPO_DATO.ARRAY)
        else:
            #error semántico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "No es posible realizar 'Concat' entre "+ obtTipoDato(valor1.tipo) + " y " + obtTipoDato(valor2.tipo))
            s.addError(err)
            helper.setConsola("[ERROR] No es posible realizar 'Concat' entre "+ obtTipoDato(valor1.tipo) + " y " + obtTipoDato(valor2.tipo) + " en la línea: "+ str(self.fila) + " y columna "+ str(self.columna) )
            return Retorno(None, TIPO_DATO.ERROR)
            #error

    def Verificar_Tipos_array(self,arr, tipo, bandera):
        if isinstance(arr,list):
            for a in arr:
                if a.tipo == TIPO_DATO.ARRAY:
                    bandera = self.Verificar_Tipos_array(a.valor, tipo, bandera)
                    if bandera == False:
                        return False
                else:
                    bandera = self.Verificar_Tipos_array(a, tipo, bandera)
                    if bandera == False:
                        return False
        else:
            if arr.tipo != tipo:
                if tipo != TIPO_DATO.ANY:
                    bandera = False
                    return bandera
                else:
                    bandera = True
                    return bandera
            else:
                bandera = True
                return bandera

    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()

        exp1 = self.expresion1.genC3D(entorno, helper)
        exp2 = self.expresion2.genC3D(entorno, helper)

        if exp1.tipo == TIPO_DATO.CADENA and exp2.tipo == TIPO_DATO.CADENA:
            generador.fConcatString()
            temp = generador.addTemp()
            temp2 = generador.addTemp()

            generador.addExpresion(temp, 'P', entorno.size, '+')
            generador.addExpresion(temp2, temp2, '1', '+')

            generador.setStack(temp, exp1.valor)
            generador.addExpresion(temp, temp, '1', '+')
            generador.setStack(temp2, exp2.valor)

            generador.crearEntorno(entorno.size)
            generador.callFun('ConcatString')
            generador.getStack(temp2, 'P')
            generador.retornarEntorno(entorno.size)
            return Retorno2(temp2, TIPO_DATO.CADENA, True)

    def genArbol(self) -> Nodo:
        nodo = Nodo("CONCAT")
        nodo.agregarHijo(self.expresion1.genArbol())
        nodo.agregarHijo(self.expresion2.genArbol())
        return nodo