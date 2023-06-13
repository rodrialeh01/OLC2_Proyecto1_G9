from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores


class Declaracion(Instruccion):
    def __init__(self, id, tipo, valor, fila, columna):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, entorno, helper):
        print("Declaracion************************************************")
        identificador = self.id
        tipo = self.tipo
        print("identificador: " + identificador)
        print("tipo: " + str(tipo))
        existe = entorno.ExisteSimbolo(identificador)
        print("existe: " + str(existe))
        if existe:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La variable " + identificador + " ya fue declarada anteriormente en el entorno actual")
            s.addError(err)
            return
        
        if tipo != None:
            print("valor: " + str(self.valor))
            if self.valor != None:
                valorG = self.valor.ejecutar(entorno, helper)
                print("valorG: " + str(valorG.valor))
                if valorG.tipo == tipo:
                    simb = Simbolo()
                    simb.nombre = identificador
                    simb.tipo = tipo
                    simb.valor = valorG.valor
                    simb.linea = self.fila
                    simb.columna = self.columna
                    simb.entorno = entorno
                    print("si se guardo en la tabla de simbolos")
                    entorno.AgregarSimbolo(identificador, simb)
        else:
            if self.valor != None:
                valorG = self.valor.ejecutar(entorno, helper)
                simb = Simbolo()
                simb.nombre = identificador
                simb.tipo = valorG.tipo
                simb.valor = valorG.valor
                simb.linea = self.fila
                simb.columna = self.columna
                simb.entorno = entorno

                entorno.AgregarSimbolo(identificador, simb)
        

    def genArbol(self) -> Nodo:
        nodo = Nodo("Declaracion")
        nodo.agregarHijo(Nodo(str(self.id)))
        if self.tipo != None:
            nodo.agregarHijo(Nodo(str(self.tipo)))
        if self.valor != None:
            nodo.agregarHijo(self.valor.genArbol())
        return nodo