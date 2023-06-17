from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno2 import Retorno2
from AST.Simbolos.Enums import TIPO_DATO

class Primitivo(Expresion):

    def __init__(self, tipo, valor, fila, columna):
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna
        super().__init__()

    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()
        if self.tipo == TIPO_DATO.NUMERO:               #No está en el heap
            return Retorno2(str(self.valor), self.tipo, False)
        elif self.tipo == TIPO_DATO.CADENA:
            temporal = generador.addTemp()
            generador.addAsignacion(temporal, 'H')

            for c in str(self.valor):
                generador.setHeap('H', ord(c))
                generador.nextHeap()
            generador.setHeap('H', -1) #-1 es un caracter no imprimible, por lo que se usa para indicar el final de la cadena
            generador.nextHeap()
                                                #si está en el heap
            return Retorno2(temporal, self.tipo, True)
        elif self.tipo == TIPO_DATO.BOOLEANO: 
            pass


    def ejecutar(self, entorno, helper) -> Retorno:
        return Retorno(self.valor, self.tipo)
    
    def genArbol(self):
        ##print("ENTRO A PRIMITIVO")
        ##print(self.valor)
        return Nodo(str(self.valor))