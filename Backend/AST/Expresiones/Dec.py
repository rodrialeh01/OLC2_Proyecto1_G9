from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Retorno2 import Retorno2
from AST.SingletonErrores import SingletonErrores


class Dec(Expresion):
    def __init__(self, id, orden, fila, columna):
        self.id = id
        self.orden = orden
        self.fila = fila
        self.columna = columna
        super().__init__()
        
    def ejecutar(self, entorno, helper):
        obtenido = entorno.ObtenerSimbolo(self.id)
        if obtenido != None:
            valor = obtenido.valor
            ##print(obtenido.tipo)
            if self.orden == "preDec":
                obtenido.valor = obtenido.valor - 1
                entorno.ActualizarSimbolo(self.id, obtenido)
                return Retorno(obtenido.valor, obtenido.tipo)
            elif self.orden == "postDec":
                obtenido.valor = obtenido.valor - 1
                entorno.ActualizarSimbolo(self.id, obtenido)
                return Retorno(valor, obtenido.tipo)
        else:
            #error semántico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La variable " + self.id + " no existe en el entorno actual" )
            s.addError(err)
            helper.setConsola("[ERROR]: La variable " + self.id + " no existe en el entorno actual " + " en la linea: " + str(self.fila) + " y columna: " + str(self.columna))
            return Retorno(None, TIPO_DATO.ERROR)
    
    def genArbol(self):
        if self.orden == "preDec":
            nodo = Nodo("--"+str(self.id))
        elif self.orden == "postDec":
            nodo = Nodo(str(self.id)+"--")
        return nodo

    def genC3D(self, entorno, helper):
        obt = entorno.ObtenerSimbolo(self.id)
        gen = Generador()

        generador = gen.getInstance()
        if obt != None:
            print("XD")
            if obt.tipo != TIPO_DATO.NUMERO:
                pass
            #Se obtiene la posicion de la variable.
            temp = generador.addTemp()
            posicionTemp = obt.posicion
            if not obt.globalVar:
                posicionTemp = generador.addTemp()
                generador.addExpresion(posicionTemp, "P", str(obt.posicion), '+')
            generador.getStack(temp, posicionTemp)
            #Se suma 1 al valor de la variable.
            temp2 = generador.addTemp()
            generador.addExpresion(temp2, temp, 1, '-')
            #Se guarda el nuevo valor en la variable.
            generador.setStack(posicionTemp, temp2)
            #Se retorna el valor de la variable.
            if self.orden == "preInc":
                return Retorno2(temp2, TIPO_DATO.NUMERO,True)
            elif self.orden == "postInc":
                return Retorno2(temp, TIPO_DATO.NUMERO,True)