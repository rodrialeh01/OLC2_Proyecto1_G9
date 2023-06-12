from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class AccesoInterface(Expresion):
    def __init__(self, id_interface,id_param, linea, columna):
        self.id_interface = id_interface
        self.id_param = id_param
        self.linea = linea
        self.columna = columna
        
    def ejecutar(self, entorno, helper):
        existe = entorno.ExisteInterfaceDeclarada(self.id_interface)
        if not existe:
            return
        objeto = entorno.ObtenerInterfaceDeclarada(self.id_interface)
        for p in objeto.paramDeclarados:
            if self.id_param in p:
                return p[self.id_param]
                
        #error semantico
        s = SingletonErrores.getInstance()
        err = Error(self.fila, self.columna, "Error Semántico", "No se encontro ningun valor para " + str(self.id_interface) + "." + str(self.id_param) )
        s.addError(err)
        return Retorno(None, None)

    def genArbol(self) -> Nodo:
        nodo = Nodo("ACCESO INTERFACE")
        nodo.agregarHijo(Nodo(str(self.id_interface)))
        nodo.agregarHijo(Nodo("."))
        nodo.agregarHijo(Nodo(str(self.id_param)))
        return nodo
