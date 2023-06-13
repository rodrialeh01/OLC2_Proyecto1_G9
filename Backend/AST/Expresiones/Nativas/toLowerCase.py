from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class ToLowerCase(Expresion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        print("TO LOWER CASE")
        print("EXPRESION: ", self.expresion)
        found = entorno.ObtenerSimbolo(self.expresion)
        print("FOUND: ", found)
        if found == None:
            pass
            #error semantico
        
        if found.tipo != TIPO_DATO.CADENA:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la función toLowerCase, debe de ser de tipo cadena, pero se encontró de tipo " + obtTipoDato(found.tipo) )
            s.addError(err)
            return
        
        return Retorno(str(found.valor).lower(), TIPO_DATO.CADENA)
            
    def genArbol(self) -> Nodo:
        nodo = Nodo("TO_LOWER_CASE")
        nodo.agregarHijo(Nodo("("))
        nodo.agregarHijo(self.expresion.genArbol())
        nodo.agregarHijo(Nodo(")"))

        return nodo