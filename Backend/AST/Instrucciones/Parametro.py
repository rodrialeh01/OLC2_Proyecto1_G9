from AST.Abstract.Instruccion import Instruccion
from AST.Nodo import Nodo
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Simbolo import Simbolo


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
        print("ejecutar parametro")
        print("hola hola", self.valor)
        print("adios adios", self.utilizado)
        if self.valor != None or self.utilizado != None:
            print(self.utilizado)
            retorno = Retorno()
            if self.valor != None: 
                retorno = self.valor.ejecutar(entorno, helper)
            else:
                #ya tiene un valor
                retorno.valor = self.utilizado.valor
                retorno.tipo = self.utilizado.tipo


            if self.tipo != retorno.tipo:
                print("Error semántico, el tipo de dato no coincide con el tipo del parametro")
                return
            
            existencia = entorno.BuscarSimboloLocal(self.id)
            if existencia is False:

                simbolo = Simbolo()
                simbolo.nombre = self.id
                simbolo.tipo = self.tipo
                simbolo.valor = retorno.valor
                simbolo.linea = self.fila
                simbolo.columna = self.columna
                simbolo.entorno = entorno

                print("ESTE ES EL SIMBOLO VALOR: ", simbolo.valor)

                if self.esRef:
                    simbolo.entorno = self.entorno
                    simbolo.valorRef = self.valorRef

                    simbolo.linea = self.fila
                    simbolo.columna = self.columna
                    simbolo.nombre = self.id
                    simbolo.tipo = self.tipo
                    simbolo.valor = None

                else:
                    simbolo.nombre = self.id
                    simbolo.tipo = self.tipo
                    simbolo.valor = retorno.valor
                    simbolo.linea = self.fila
                    simbolo.columna = self.columna
                    simbolo.entorno = entorno

                entorno.AgregarSimbolo(self.id, simbolo)
        else:

            print(self.id, "no tiene valor")

    def genArbol(self) -> Nodo:
        nodo = Nodo("Parametro")
        nodo.agregarHijo(Nodo(str(self.id)))
        if self.tipo != None:
            nodo.agregarHijo(Nodo(str(self.tipo)))
        if self.valor != None:
            nodo.agregarHijo(self.valor.genArbol())

            
        return nodo



