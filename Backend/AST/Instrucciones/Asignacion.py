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
        print("Desde Asignacion:D")
        existe = entorno.ExisteSimbolo(self.id)
        print(existe)
        if existe:
            valorG = self.valor.ejecutar(entorno, helper)

            simb = entorno.ObtenerSimbolo(self.id)
            print("ID: ", self.id)
            print("SIMBTIPO: ", obtTipoDato(simb.tipo))
            print("VALORG: ", obtTipoDato(valorG.tipo))
            if simb.tipo == valorG.tipo:
                print("==========Asignacion===========")
                print("Valor anterior: ", simb.valor)
                print("Valor nuevo: ", valorG.valor)
                simb.valor = valorG.valor
                entorno.ActualizarSimbolo(self.id, simb)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "No se le puede asignar un valor de tipo " + str(obtTipoDato(valorG.tipo)) + " a la variable " + self.id + " de tipo " + str(obtTipoDato(simb.tipo)))
                s.addError(err)
                return 
        else:
            #error semántico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La variable " + self.id + " no existe en el entorno actual" )
            s.addError(err)
            return 

    def genArbol(self) -> Nodo:
        nodo = Nodo("Asignacion")
        nodo.agregarHijo(Nodo(str(self.id)))
        nodo.agregarHijo(self.valor.genArbol())
        return nodo
    