from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class Inc(Expresion):
    def __init__(self, id, orden, fila, columna):
        self.id = id
        self.orden = orden
        self.fila = fila
        self.columna = columna
        print("ZSSSSSSSSSSSSSSSSSSSSSSSSSSS")

    def ejecutar(self, entorno, helper):
        obtenido = entorno.ObtenerSimbolo(self.id)
        if obtenido != None:
            valor = obtenido.valor
            if self.orden == "preInc":
                obtenido.valor = obtenido.valor + 1
                entorno.ActualizarSimbolo(self.id, obtenido)
                return Retorno(obtenido.valor, obtenido.tipo)
            elif self.orden == "postInc":
                obtenido.valor = obtenido.valor + 1
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
        if self.orden == "preInc":
            nodo = Nodo("++"+str(self.id))
        elif self.orden == "postInc":
            nodo = Nodo(str(self.id)+"++")
        return nodo