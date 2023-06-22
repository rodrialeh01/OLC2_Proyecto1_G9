from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.SingletonErrores import SingletonErrores


class Return(Instruccion):
    def __init__(self, valor, fila, columna):
        self.valor = valor
        self.fila = fila
        self.columna = columna
        super().__init__()

    def ejecutar(self, entorno, helper):
        if helper.getFuncion() == "Funcion":
            if self.valor != None:
                valor = self.valor.ejecutar(entorno, helper)
                #print("Desde Return: ")
                #print(valor)
                return valor
            else:
                return self
        else:
            s = SingletonErrores.getInstance()
            error = Error(self.fila, self.columna, "Error Semantico", "Return fuera de función")
            helper.setConsola("[ERROR]: Return fuera de función en la línea " + str(self.fila) +" y columna " + str(self.columna))
            s.addError(error)
            return

    def genArbol(self) -> Nodo:
        if self.valor != None:
            nodo = Nodo("RETURN")
            nodo.agregarHijo(self.valor.genArbol())
            return nodo
        else:
            nodo = Nodo("RETURN")
            return nodo
    
    def genC3D(self, entorno, helper):
        print("QUIERO VER ESTE PRINT:::::::::: ", self.valor)
        result = self.valor.genC3D(entorno, helper)
        if result.valor == None:
            print("ESTE ES UN ERRROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOR")
        if isinstance(result, Error):

            return None
        if result.tipo == TIPO_DATO.BOOLEANO:
            self.trueLabel = result.trueLabel
            self.falseLabel = result.falseLabel
        return result