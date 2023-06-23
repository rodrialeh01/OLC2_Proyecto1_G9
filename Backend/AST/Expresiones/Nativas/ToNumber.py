from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Retorno2 import Retorno2
from AST.SingletonErrores import SingletonErrores


class ToNumber(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        super().__init__()

    def ejecutar(self, entorno, helper):
        
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
        nodo = Nodo("NUMBER")
        nodo.agregarHijo(self.expresion.genArbol())
        return nodo
    
    def genC3D(self, entorno, helper):

        gen = Generador()
        generador = gen.getInstance()
        generador.addComment("------- ToNumber ---------")
        try:
            valor = self.expresion.genC3D(entorno, helper)
            generador.crearEntorno(entorno.size)
            generador.fNumber()
            generador.addAsignacion('H', valor.valor)
            generador.callFun('fNumber')
            temp = generador.addTemp()
            generador.getStack(temp, 'P')
            generador.retornarEntorno(entorno.size)
            print("ToNumber: ", temp)
            return Retorno2(temp, TIPO_DATO.NUMERO, True)
        except:
            generador.addComment("El valor a convertir a número no es válido.")   