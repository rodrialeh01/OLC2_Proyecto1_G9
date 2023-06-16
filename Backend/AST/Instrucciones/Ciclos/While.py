from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.SingletonErrores import SingletonErrores


class While(Instruccion):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        condTemp = True
        helperTemp = helper.getCiclo()
        helper.setCiclo("ciclo")
        #entorno_local = None
        while condTemp == True:
            condicion = self.condicion.ejecutar(entorno, helper)
            if condicion.tipo != TIPO_DATO.BOOLEANO:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de WHILE, debe de ser de tipo booleano, pero se encontró de tipo " + obtTipoDato(condicion.tipo) )
                s.addError(err)
                helper.setConsola("[ERROR]: Se ha encontrado un error en la condicional de WHILE, debe de ser de tipo booleano, pero se encontró de tipo " + obtTipoDato(condicion.tipo) + " en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))	
                return
            
            if self.instrucciones != None:
                try:
                    if condicion.valor != condTemp:
                        condTemp = False
                        helper.setCiclo(helperTemp)
                        helper.setTs(entorno_local)
                        return

                    entorno_local = Entorno(entorno)
                    #if condicion.valor:
                    #entorno_local = Entorno(entorno)
                    entorno_local.setActual("While")
                    for instruccion in self.instrucciones:
                        result = instruccion.ejecutar(entorno_local, helper)
                        if isinstance(result, Break):
                            helper.setCiclo(helperTemp)
                            condTemp = False
                            helper.setTs(entorno_local)
                            return result
                        
                        if isinstance(result, Continue):
                            
                            raise Exception
                            
                        if isinstance(result, Return):
                            
                            return result

                except Exception:
                    continue

        #if entorno_local != None:
        helper.setCiclo(helperTemp)

    def genArbol(self):
        nodo = Nodo("WHILE")
        nodo.agregarHijo(Nodo("while"))
        nodo.agregarHijo(Nodo("("))
        nodo.agregarHijo(self.condicion.getNodo())
        nodo.agregarHijo(Nodo(")"))
        if self.instrucciones != None:
            ins = Nodo("INSTRUCCIONES")
            for instruccion in self.instrucciones:
                ins.agregarHijo(instruccion.getNodo())
            nodo.agregarHijo(ins)
        return nodo
