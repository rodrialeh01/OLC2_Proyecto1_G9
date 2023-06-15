from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
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
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "No se encontró la variable " + str(self.id_interface))
            helper.setConsola("[ERROR]: No se encontró la variable " + str(self.id_interface) + " en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
            s.addError(err)
            return Retorno(None, TIPO_DATO.ERROR)
        
        objeto = entorno.ObtenerInterfaceDeclarada(self.id_interface)
        for p in objeto.paramDeclarados:
            if self.id_param in p:
                return p[self.id_param]
                
        #error semantico
        s = SingletonErrores.getInstance()
        err = Error(self.linea, self.columna, "Error Semántico", "La variable " + str(self.id_interface) + " no posee el atributo" + str(self.id_param) )
        helper.setConsola("[ERROR]: La variable " + str(self.id_interface) + " no posee el atributo " + str(self.id_param) + " en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
        s.addError(err)
        return Retorno(None, TIPO_DATO.ERROR)

    def genArbol(self) -> Nodo:
        nodo = Nodo("ACCESO INTERFACE")
        nodo.agregarHijo(Nodo(str(self.id_interface)))
        nodo.agregarHijo(Nodo("."))
        nodo.agregarHijo(Nodo(str(self.id_param)))
        return nodo
