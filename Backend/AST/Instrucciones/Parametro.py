from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores


class Parametro(Instruccion):
    def __init__(self, id, tipo, valor, fila, columna, esRef):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna

        self.esRef = esRef 
        self.utilizado = None 
        self.entorno = None 
        self.valorRef = None 

    def ejecutar(self, entorno, helper):
        if self.valor != None or self.utilizado != None:
            
            retorno = Retorno()
            if self.valor != None: 
                retorno = self.valor.ejecutar(entorno, helper)
            else:
                retorno.valor = self.utilizado.valor
                retorno.tipo = self.utilizado.tipo

            if self.tipo != retorno.tipo:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "El tipo de dato no coincide con el tipo de dato del parametro")
                s.addError(err)
                helper.setConsola("[ERROR] El tipo de dato no coincide con el tipo de dato del parametro en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                return
            #print("SIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIUUUUUUUUUUUUU")
            existencia = entorno.BuscarSimboloLocal(self.id)
            #print(existencia)
            if existencia is False:

                simbolo = Simbolo()
                simbolo.nombre = self.id
                simbolo.tipo = self.tipo
                simbolo.valor = retorno.valor
                simbolo.linea = self.fila
                simbolo.columna = self.columna
                simbolo.entorno = entorno

                entorno.AgregarSimbolo(self.id, simbolo)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "El parametro " + self.id + " ya fue declarado anteriormente en el entorno actual")
                s.addError(err)
                helper.setConsola("[ERROR] El parametro " + self.id + " ya fue declarado anteriormente en el entorno actual en la línea "+ str(self.fila) +" y columna " + str(self.columna))

                #ERROR
                return
        else:
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "El parametro" + self.id +" no tiene un valor asignado")
            s.addError(err)
            helper.setConsola("[ERROR] El parametro" + self.id +" no tiene un valor asignado en la línea "+ str(self.fila) +" y columna " + str(self.columna))
            return

    def genArbol(self) -> Nodo:
        nodo = Nodo("Parametro")
        nodo.agregarHijo(Nodo(str(self.id)))
        if self.tipo != None:
            nodo.agregarHijo(Nodo(str(self.tipo)))
        if self.valor != None:
            nodo.agregarHijo(self.valor.genArbol())

            
        return nodo



