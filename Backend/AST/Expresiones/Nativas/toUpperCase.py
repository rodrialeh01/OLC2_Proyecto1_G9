from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class ToUpperCase(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        valor = self.expresion.ejecutar(entorno, helper)
        if valor.tipo != TIPO_DATO.CADENA:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la función toUpperCase, debe de ser de tipo String, pero se encontró de tipo " + obtTipoDato(valor.tipo) )
            s.addError(err)
            return
        
        return Retorno(str(valor.valor).upper(), TIPO_DATO.CADENA)
    
    
    def genArbol(self) -> Nodo:
        nodo = Nodo("TO_UPPER_CASE")
        nodo.agregarHijo(Nodo("("))
        nodo.agregarHijo(self.expresion.genArbol())
        nodo.agregarHijo(Nodo(")"))

        return nodo
