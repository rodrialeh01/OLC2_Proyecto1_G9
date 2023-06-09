from AST.Abstract.Instruccion import Instruccion
from AST.Simbolos.Simbolo import Simbolo


class Declaracion(Instruccion):
    def __init__(self, id, tipo, valor, fila, columna):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, entorno, helper):
        identificador = self.id
        tipo = self.tipo
        existe = entorno.ExisteSimbolo(identificador)
        if existe:
            #error semantico
            pass
        
        if tipo != None:
            if self.valor != None:
                valorG = self.valor.ejecutar(entorno, helper)
                if valorG.tipo == tipo:
                    simb = Simbolo()
                    simb.nombre = identificador
                    simb.tipo = tipo
                    simb.valor = valorG.valor
                    simb.linea = self.fila
                    simb.columna = self.columna
                    simb.entorno = entorno

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
        

            