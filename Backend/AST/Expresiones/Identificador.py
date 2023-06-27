from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Retorno2 import Retorno2
from AST.SingletonErrores import SingletonErrores


class Identificador(Expresion):
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        super().__init__()

    def ejecutar(self, entorno, helper):
        #print("Desde Identificador (): ")
        print('IDENTIFICADOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOR')
        existe = entorno.ExisteSimbolo(self.nombre)
        print('existeeeeeeeeeeeee:',existe)
        if existe:
            ret = entorno.ObtenerSimbolo(self.nombre)
            ##print("Desde Identificador 2 (): ")
            ##print(ret)
            print('SI RETORNO ALGO ', ret.valor)
            return Retorno(ret.valor, ret.tipo)
        else:
            print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
            print(self.nombre)
            print(entorno.ExisteInterfaceDeclarada(self.nombre))
            existe2 = entorno.ObtenerInterfaceDeclarada(self.nombre)
            print('existeeeeeeeeeeeee22222222222:',existe2)
            if existe2 == None:
                #error semántico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "La variable " + self.nombre + " no existe en el entorno actual" )
                helper.setConsola("[ERROR] La variable " + self.nombre + " no existe en el entorno actual en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                s.addError(err)
                return Retorno(None, None)
            else:
                return Retorno(existe2, TIPO_DATO.INTERFACE)

    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()

        generador.addComment("Acceso a Identificador")
        print('ACCESO IDENTIFICADOR:', self.nombre)
        existe = entorno.ExisteSimbolo(self.nombre)
        print(existe)
        if not existe:
            generador.addComment("Fin Acceso a Identificador - No existe")
            return
        
        s_c3d = entorno.ObtenerSimbolo(self.nombre)
        temp = generador.addTemp()
        print('identificadoooooor:',temp)
        #Se obtiene la posicion de la variable.
        posicionTemp = s_c3d.posicion
        print('POS:', posicionTemp)
        if not s_c3d.globalVar:
            print('no es global')
            posicionTemp = generador.addTemp()
            generador.addExpresion(posicionTemp, "P", s_c3d.posicion, '+')
        generador.getStack(temp, posicionTemp)
        print('hola')
        if s_c3d.tipo == TIPO_DATO.CHAR:
            tempc = generador.addTemp()
            print('tempc', tempc)
            generador.getHeap(tempc, temp)
            generador.addComment("Fin Acceso a Identificador desde char")
            return Retorno2(tempc, s_c3d.tipo, True)

        if s_c3d.tipo != TIPO_DATO.BOOLEANO:
            generador.addComment("Fin Acceso a Identificador")
            return Retorno2(temp, s_c3d.tipo, True)
        if self.trueLabel == '':
            self.trueLabel = generador.newLabel()
        if self.falseLabel == '':
            self.falseLabel = generador.newLabel()

        generador.addIf(temp, '1', '==', self.trueLabel)
        generador.addGoto(self.falseLabel)

        generador.addComment("Fin Acceso a Identificador")
        ret = Retorno2(None, TIPO_DATO.BOOLEANO, True)
        ret.trueLabel = self.trueLabel
        ret.falseLabel = self.falseLabel
        return ret
    


    def genArbol(self) -> Nodo:
        return Nodo(self.nombre)