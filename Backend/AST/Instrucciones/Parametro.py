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
        #print("============================================================================")
        #print("ejecutar parametro")
        #print("hola hola", self.valor)
        #print("adios adios", self.utilizado)
        #print("============================================================================")
        if self.valor != None or self.utilizado != None:
            
            retorno = Retorno()
            if self.valor != None: 
                
                retorno = self.valor.ejecutar(entorno, helper)
                #print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-", retorno)
            else:
                #ya tiene un valor
                #print("oh no: ")
                #print(self.utilizado.valor)
                #print(self.utilizado.tipo)
                retorno.valor = self.utilizado.valor
                retorno.tipo = self.utilizado.tipo

            #print("-*- ESTA LA VERIFICACIÓN DE AHORAAAAAAAAAAAAAAAAAAA: *-*-**-*-")
            #print(self.tipo)
            #print(retorno.tipo)
            if self.tipo != retorno.tipo:
                #print(self.tipo)
                #print(retorno.tipo)
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "El tipo de dato no coincide con el tipo de dato del parametro")
                s.addError(err)
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
                #ERROR
                return
        else:
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "El parametro" + self.id +" no tiene un valor asignado")
            s.addError(err)
            return

    def genArbol(self) -> Nodo:
        nodo = Nodo("Parametro")
        nodo.agregarHijo(Nodo(str(self.id)))
        if self.tipo != None:
            nodo.agregarHijo(Nodo(str(self.tipo)))
        if self.valor != None:
            nodo.agregarHijo(self.valor.genArbol())

            
        return nodo



