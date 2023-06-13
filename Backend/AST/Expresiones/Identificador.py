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
        print("Desde Identificador : ")
        existe = entorno.ExisteSimbolo(self.nombre)
        print("Existe: ", existe)
        if existe:
            #print("Desde Identificador 2 (): ")
            ret = entorno.ObtenerSimbolo(self.nombre)
            #print(ret)
            return Retorno(ret.valor, ret.tipo)
        else:
            #error semántico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La variable " + self.nombre + " no existe en el entorno actual" )
            s.addError(err)
            return Retorno(None, None)
        
    def genArbol(self) -> Nodo:
        return Nodo(self.nombre)