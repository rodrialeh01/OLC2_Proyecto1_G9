from AST.Abstract.Instruccion import Instruccion
from AST.Nodo import Nodo
from AST.Error import Error
from AST.SingletonErrores import SingletonErrores

class Break(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        if helper.getCiclo() == "ciclo":
            return self
        else:
            s = SingletonErrores.getInstance()
            error = Error(self.fila, self.columna, "Error Semantico", "Break fuera de ciclo")
            helper.setConsola("[ERROR]: Break fuera de ciclo en la línea " + str(self.fila) +" y columna " + str(self.columna))
            s.addError(error)
            return 
        
    def genArbol(self) -> Nodo:
        return Nodo("break")