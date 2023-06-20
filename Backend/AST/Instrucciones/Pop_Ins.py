from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.SingletonErrores import SingletonErrores


class Pop_Ins(Instruccion):
    def __init__(self, id, fila, columna) -> None:
        self.id = id
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        existe = entorno.ExisteSimbolo(self.id)
        if existe:
            val = entorno.ObtenerSimbolo(self.id)

            if val.tipo == TIPO_DATO.NUMERO or val.tipo == TIPO_DATO.CADENA or val.tipo == TIPO_DATO.BOOLEANO or val.tipo == TIPO_DATO.NULL:
                s = SingletonErrores.getInstance()
                s.addError(Error(self.linea, self.columna, "Error Semántico", "No es posible hacer push a un tipo de variable que no es array"))
                helper.setConsola("[ERROR] Un tipo de dato que no es array no posee la funcion push en linea: "+str(self.linea)+ " y columna: "+str(self.columna))
                return
            else:
                if len(val.valor) != 0:
                    val.valor.pop()
                    entorno.ActualizarSimbolo(self.id, val)
                else:
                    s = SingletonErrores.getInstance()
                    s.addError(Error(self.linea, self.columna, "Error Semántico", "No es posible hacer pop a un array vacio"))
                    helper.setConsola("[ERROR] No es posible hacer pop a un array vacio en la línea "+str(self.linea)+ " y columna: "+str(self.columna))
                    return
            


    def genArbol(self) -> Nodo:
        pass
    
    def genC3D(self, entorno, helper):
        pass
    