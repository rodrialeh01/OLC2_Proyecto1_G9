from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class Asignacion(Instruccion):
    def __init__(self, id, valor, fila, columna):
        self.id = id
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        existe = entorno.ExisteSimbolo(self.id)
        if existe:
            valorG = self.valor.ejecutar(entorno, helper)
            simb = entorno.ObtenerSimbolo(self.id)
            if simb.tipo == valorG.tipo or  simb.tipo == TIPO_DATO.ANY:
                simb.valor = valorG.valor
                entorno.ActualizarSimbolo(self.id, simb)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se le puede asignar un valor de tipo " + str(obtTipoDato(valorG.tipo)) + " a la variable " + self.id + " de tipo " + str(obtTipoDato(simb.tipo)))
                s.addError(err)
                helper.setConsola("[ERROR] No se le puede asignar un valor de tipo " + str(obtTipoDato(valorG.tipo)) + " a la variable " + self.id + " de tipo " + str(obtTipoDato(simb.tipo)) + " en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                return 
        else:
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La variable " + self.id + " no existe en el entorno actual" )
            s.addError(err)
            helper.setConsola("[ERROR] La variable " + self.id + " no existe en el entorno actual en la línea "+ str(self.fila) +" y columna " + str(self.columna))
            return 

    def genArbol(self) -> Nodo:
        nodo = Nodo("Asignacion")
        nodo.agregarHijo(Nodo(str(self.id)))
        nodo.agregarHijo(self.valor.genArbol())
        return nodo
    