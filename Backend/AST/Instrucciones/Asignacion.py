from AST.Abstract.Instruccion import Instruccion


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
            if simb.tipo == valorG.tipo:
                simb.valor = valorG.valor
                entorno.ActualizarSimbolo(self.id, simb)