from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores


class Interface(Simbolo, Instruccion):
    def __init__(self, id, listaParametros, linea, columna):
        self.id = id
        self.listaParametros = listaParametros
        self.linea = linea
        self.columna = columna
        super().__init__()
    
    def ejecutar(self, entorno, helper):
        for pa in self.listaParametros:
            if not isinstance(pa.tipo, TIPO_DATO):
                existe = entorno.ExisteInterface(pa.tipo)
                if not existe:
                    s = SingletonErrores.getInstance()
                    err = Error(self.linea, self.columna, "Error Semántico", "La interface " + pa.tipo + " no existe en el entorno actual")
                    s.addError(err)
                    helper.setConsola("[ERROR] ;;;;;;;;;; La interface " + pa.tipo + " no existe en el entorno actual en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                    return
        self.crearInterface(self.id, self.listaParametros, self.linea, self.columna)
        verif = entorno.ExisteInterface(self.id)
        if not verif:
            entorno.AgregarInterface(self.id, self)
        else:
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "La interface " + self.id + " ya fue declarada anteriormente en el entorno actual")
            s.addError(err)
            helper.setConsola("[ERROR] La interface " + self.id + " ya fue declarada anteriormente en el entorno actual en la línea "+ str(self.linea) +" y columna " + str(self.columna))
            return

    def genC3D(self, entorno, helper):
        pass

    def genArbol(self) -> Nodo:
        #print("ENTRO A CREAR INTERFACE")
        nodo = Nodo("CREAR INTERFACE")
        return nodo