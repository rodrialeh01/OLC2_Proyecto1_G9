from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class Identificador(Expresion):
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        print("Desde Identificador (): ")
        existe = entorno.ExisteSimbolo(self.nombre)
        print(existe)
        if existe:
            ret = entorno.ObtenerSimbolo(self.nombre)
            #print("Desde Identificador 2 (): ")
            #print(ret)
            return Retorno(ret.valor, ret.tipo)
        else:
            existe2 = entorno.ObtenerInterfaceDeclarada(self.nombre)
            if existe2 == None:
                #error semántico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "La variable " + self.nombre + " no existe en el entorno actual" )
                helper.setConsola("[ERROR] La variable " + self.nombre + " no existe en el entorno actual en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                s.addError(err)
                return Retorno(None, None)
            else:
                return Retorno(existe2, TIPO_DATO.INTERFACE)


        
    def genArbol(self) -> Nodo:
        return Nodo(self.nombre)