from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.SingletonErrores import SingletonErrores


class Continue(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        super().__init__()
    
    def ejecutar(self, entorno, helper):
        if helper.getCiclo() == "ciclo":
            return self
        else:
            s = SingletonErrores.getInstance()
            error = Error(self.fila, self.columna, "Error Semantico", "Continue fuera de ciclo")
            helper.setConsola("[ERROR]: Continue fuera de ciclo en la línea " + str(self.fila) +" y columna " + str(self.columna))
            s.addError(error)
            return

    def genArbol(self) -> Nodo:
        return Nodo("Continue")

    def genC3D(self, entorno, helper):
        return self