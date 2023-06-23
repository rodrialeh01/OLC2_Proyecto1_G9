from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Retorno2 import Retorno2
from AST.SingletonErrores import SingletonErrores


class Length(Expresion):
    def  __init__(self, exp1, linea, columna):
        self.exp1 = exp1
        self.linea = linea
        self.columna = columna
        super().__init__()

    def ejecutar(self, entorno, helper):
        valor = self.exp1.ejecutar(entorno, helper)

        if valor.tipo == TIPO_DATO.NUMERO or valor.tipo == TIPO_DATO.BOOLEANO:
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "No es posible obtener 'length' para una variable de tipo " + str(obtTipoDato(valor.tipo)) +"." )
            s.addError(err)
            helper.setConsola("[ERROR]: No es posible obtener 'length' para una variable de tipo " + obtTipoDato(valor.tipo) + " en la línea " + str(self.linea) +  " y columna "+ str(self.columna) )
            return Retorno(None, TIPO_DATO.ERROR)
            
        return Retorno(len(valor.valor), TIPO_DATO.NUMERO)

    def genArbol(self):
        nodo = Nodo("LENGTH")
        nodo.agregarHijo(self.exp1.genArbol())
        return nodo
        
    def genC3D(self, entorno, helper):
        valor = self.exp1.genC3D(entorno, helper)
        gen = Generador()
        generador = gen.getInstance()

        generador.addComment("------- Length ---------")
        if valor.tipo == TIPO_DATO.CADENA:
            generador.flength()
            
            generador.crearEntorno(entorno.size)
            generador.addAsignacion('H', valor.valor)
            generador.callFun('length')

            temp = generador.addTemp()
            generador.getStack(temp, 'P')
            generador.retornarEntorno(entorno.size)
            

            return Retorno2(temp, TIPO_DATO.NUMERO, True)            #return Retorno2('XD', TIPO_DATO.NUMERO, False)