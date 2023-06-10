from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Retorno import Retorno


class Inc(Expresion):
    def __init__(self, id, orden, fila, columna):
        self.id = id
        self.orden = orden
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        obtenido = entorno.ObtenerSimbolo(self.id)
        if obtenido != None:
            valor = obtenido.valor
            if self.orden == "preInc":
                obtenido.valor = obtenido.valor + 1
                entorno.ActualizarSimbolo(self.id, obtenido)
                return Retorno(obtenido.valor, obtenido.tipo)
            elif self.orden == "postInc":
                obtenido.valor = obtenido.valor + 1
                entorno.ActualizarSimbolo(self.id, obtenido)
                return Retorno(valor, obtenido.tipo)
            
        else:
            return Retorno("No se encontro la variable", "error")
    
    def genArbol(self):
        if self.orden == "preInc":
            nodo = Nodo("++"+str(self.id))
        elif self.orden == "postInc":
            nodo = Nodo(str(self.id)+"++")
        return nodo