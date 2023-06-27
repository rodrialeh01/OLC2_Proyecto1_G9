from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Retorno2 import Retorno2


class TypeOf(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        super().__init__()

    def ejecutar(self, entorno, helper):
        valor = self.expresion.ejecutar(entorno, helper)
        tipo = obtTipoDato(valor.tipo)
        return Retorno(tipo, TIPO_DATO.CADENA)


    def genArbol(self) -> Nodo:
        nodo = Nodo("TYPEOF")
        nodo.agregarHijo(self.expresion.genArbol())
        return nodo
    
    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()

        generador.addComment("------- TypeOf ---------")
        exp = self.expresion.genC3D(entorno, helper)
        print(exp.valor, "66666666666666666666666666666")
        if exp.tipo == TIPO_DATO.BOOLEANO:
            generador.putLabel(exp.trueLabel)
            generador.putLabel(exp.falseLabel)

        temp = generador.addTemp()
        temp2 = generador.addTemp()
        generador.crearEntorno(entorno.size)
        generador.addExpresion(temp, 'P', entorno.size, '+')

        if exp.tipo != TIPO_DATO.BOOLEANO:
            generador.setStack(temp, exp.valor)
            print(temp, "999999999999999999999999999999999999999999999999999")
        else:
            print(exp.valor)
            if exp.valor:
                generador.setStack(temp, 1)
            else:
                generador.setStack(temp, 0)

        if exp.tipo == TIPO_DATO.CADENA or exp.tipo == TIPO_DATO.CHAR:
            generador.addAsignacion('H', exp.valor)
            generador.fStringString()
            generador.callFun('typeString')

        elif exp.tipo == TIPO_DATO.NUMERO:
            generador.fStringNumber()
            generador.callFun('typeNumber')
        
        elif exp.tipo == TIPO_DATO.BOOLEANO:
            generador.fStringBoolean()
            generador.callFun('typeBoolean')

        generador.getStack(temp2, 'P')

        generador.retornarEntorno(entorno.size)

        return Retorno2(temp2, TIPO_DATO.CADENA, True)