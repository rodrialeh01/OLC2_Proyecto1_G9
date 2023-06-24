from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Retorno2 import Retorno2
from AST.SingletonErrores import SingletonErrores


class ToLowerCase(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        found = self.expresion.ejecutar(entorno, helper)

        if found == None:
            pass
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la función toLowerCase, la expresión debe de ser de tipo string, pero se encontró de tipo " + obtTipoDato(found.tipo) )
            s.addError(err)
            helper.setConsola("[ERROR]: Se ha encontrado un error en la función toLowerCase, la expresión debe de ser de tipo string, pero se encontró de tipo " + obtTipoDato(found.tipo) + " en la línea " + str(self.fila) + " y columna "+ str(self.columna))
            return Retorno(None, TIPO_DATO.ERROR)
        
        if found.tipo != TIPO_DATO.CADENA:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la función toLowerCase, la expresión debe de ser de tipo string, pero se encontró de tipo " + obtTipoDato(found.tipo) )
            s.addError(err)
            helper.setConsola("[ERROR]: Se ha encontrado un error en la función toLowerCase, la expresión debe de ser de tipo string, pero se encontró de tipo " + obtTipoDato(found.tipo) + " en la línea " + str(self.fila) + " y columna "+ str(self.columna))
            return Retorno(None, TIPO_DATO.ERROR)
        
        return Retorno(str(found.valor).lower(), TIPO_DATO.CADENA)
            
    def genC3D(self, entorno, helper):
        print("ToLowerCase")
        gen = Generador()
        generador = gen.getInstance()

        
        temp = generador.addTemp()
        temp2 = generador.addTemp()

        exp = self.expresion.genC3D(entorno, helper)
        print(exp.tipo)
        if exp.tipo == TIPO_DATO.CADENA:
            generador.ftoLowerCase()
            generador.addExpresion(temp, 'P', entorno.size, '+')

            generador.setStack(temp, exp.valor)
            #stack[0] = 5
            generador.crearEntorno(entorno.size)
            generador.addAsignacion('H', exp.valor)
            generador.callFun('toLowerCase')
            generador.getStack(temp2, 'P')
            generador.retornarEntorno(entorno.size)
            return Retorno2(temp2, TIPO_DATO.CADENA, True)

    def genArbol(self) -> Nodo:
        nodo = Nodo("TO_LOWER_CASE")
        nodo.agregarHijo(self.expresion.genArbol())
        return nodo