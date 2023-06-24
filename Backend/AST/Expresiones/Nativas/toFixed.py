from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores
from AST.Simbolos.Retorno2 import Retorno2


class ToFixed(Expresion):
    def __init__(self, expresion, cantidad, fila, columna):
        self.expresion = expresion
        self.cantidad = cantidad
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        cantidad_de_decimales = self.cantidad.ejecutar(entorno, helper)
        valor_a_aproximar = self.expresion.ejecutar(entorno, helper)
        if valor_a_aproximar.tipo != TIPO_DATO.NUMERO or cantidad_de_decimales.tipo != TIPO_DATO.NUMERO or cantidad_de_decimales.tipo != TIPO_DATO.ANY or cantidad_de_decimales.tipo != TIPO_DATO.ANY:
            #error semantico
            if valor_a_aproximar.tipo != TIPO_DATO.NUMERO:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la función toFixed, la expresión debe de ser de tipo Number, pero se encontró de tipo " + obtTipoDato(valor_a_aproximar.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: Se ha encontrado un error en la función toFixed, la expresión debe de ser de tipo Number, pero se encontró de tipo " + obtTipoDato(valor_a_aproximar.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None, TIPO_DATO.ERROR)
            if cantidad_de_decimales.tipo != TIPO_DATO.NUMERO:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la función toFixed, el argumento debe de ser de tipo Number, pero se encontró de tipo " + obtTipoDato(cantidad_de_decimales.tipo))
                s.addError(err)
                helper.setConsola("[ERROR]: Se ha encontrado un error en la función toFixed, el argumento debe de ser de tipo Number, pero se encontró de tipo " + obtTipoDato(cantidad_de_decimales.tipo) + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
                return Retorno(None, TIPO_DATO.ERROR)
            
        return Retorno(round(float(valor_a_aproximar.valor),int(cantidad_de_decimales.valor)), TIPO_DATO.NUMERO)

    def genArbol(self) -> Nodo:
        nodo = Nodo("TO_FIXED")
        nodo.agregarHijo(self.expresion.genArbol())
        nodo.agregarHijo(self.cantidad.genArbol())

        return nodo
    
    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()

        exp = self.expresion.genC3D(entorno, helper)
        cantidad = self.cantidad.genC3D(entorno, helper)
        generador.addComment("----- Inicia toFixed -----")
        #casos:
        tempExp = generador.addTemp()
        tempCantidad = generador.addTemp()

        if exp.tipo == TIPO_DATO.NUMERO and cantidad.tipo == TIPO_DATO.NUMERO:
            
            generador.addAsignacion(tempExp, exp.valor)
            generador.addAsignacion(tempCantidad, cantidad.valor)
            
            tempRes = generador.addTemp()
            tempMult = generador.addTemp()

            generador.addExpresion(tempMult, tempCantidad, 10, '*')
            tempExpRound = generador.addTemp()
            generador.addExpresion(tempExpRound, tempExp, tempMult, '*')
            generador.fotmatPrint(tempRes, tempMult, tempExpRound)

            return Retorno2(tempRes, TIPO_DATO.NUMERO, True)

        else:
            generador.addComment("Hubo un error en toFixed. No se puede realizar la operación")
            
        print("expresion: ", self.expresion)
        print("cantidad de decimales: ", self.cantidad)
        

        pass