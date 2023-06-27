from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.SingletonErrores import SingletonErrores


class AsignarInterface(Instruccion):
    def __init__(self, id_interface,id_param,expresion, linea, columna):
        self.id_interface = id_interface
        self.id_param = id_param
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        super().__init__()

    def ejecutar(self, entorno, helper):
        existe = entorno.ExisteInterfaceDeclarada(self.id_interface)
        #print("EXISTE INTERFACEEEEEEEEEEEEEEEEEE", existe)
        if not existe:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "Se ha encontrado un error en la Asignación, no existe la interface " + self.id_interface)
            s.addError(err)
            helper.setConsola("[ERROR] Se ha encontrado un error en la Asignación, no existe la interface " + self.id_interface + " en la línea "+ str(self.linea) +" y columna " + str(self.columna))
            return

        objeto = entorno.ObtenerInterfaceDeclarada(self.id_interface)
        interface = entorno.ObtenerInterface(objeto.objeto)
        for p in objeto.paramDeclarados:
            if self.id_param in p:
                #print(p[self.id_param].tipo != self.expresion.tipo)
                #print(p[self.id_param].valor)
                tipo = None
                for i in interface.params:
                    if i.id == self.id_param:
                        tipo = i.tipo
                        break
                if tipo == TIPO_DATO.ANY:
                    p[self.id_param].valor = self.expresion.ejecutar(entorno,helper).valor
                    entorno.ActualizarInterfaceDeclarada(self.id_interface, objeto)
                    return
                elif p[self.id_param].tipo != self.expresion.tipo :
                    #error semantico
                    s = SingletonErrores.getInstance()
                    err = Error(self.linea, self.columna, "Error Semántico", "Se ha encontrado un error en la Asignación, el tipo de dato no coincide con el parametro " + self.id_param + " en la interface " + self.id_interface)
                    s.addError(err)
                    helper.setConsola("[ERROR] Se ha encontrado un error en la Asignación, el tipo de dato no coincide con el parametro " + self.id_param + " en la interface " + self.id_interface + " en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                    return
                p[self.id_param].valor = self.expresion.ejecutar(entorno,helper).valor
                entorno.ActualizarInterfaceDeclarada(self.id_interface, objeto)
                return
                
        #error semantico
        s = SingletonErrores.getInstance()
        err = Error(self.linea, self.columna, "Error Semántico", "Se ha encontrado un error en la Asignación, no existe el parametro " + self.id_param + " en la interface " + self.id_interface)
        s.addError(err)
        helper.setConsola("[ERROR] Se ha encontrado un error en la Asignación, no existe el parametro " + self.id_param + " en la interface " + self.id_interface + " en la línea "+ str(self.linea) +" y columna " + str(self.columna))
        return

    def genC3D(self, entorno, helper):
        pass
    def genArbol(self) -> Nodo:
        nodo = Nodo("ASIGNAR INTERFACE")
        return nodo



