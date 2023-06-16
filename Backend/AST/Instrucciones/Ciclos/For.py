from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.SingletonErrores import SingletonErrores


class For(Instruccion):
    def __init__(self, exp1, condicion, incremento, instrucciones, fila, columna):
        self.exp1 = exp1 
        self.condicion = condicion
        self.incremento = incremento
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna


    def ejecutar(self, entorno, helper):
        entornoLocal = Entorno(entorno)
        self.exp1.ejecutar(entornoLocal, helper)
        helperTemp = helper.getCiclo()
        helper.setCiclo("ciclo")

        while True:

            condicion = self.condicion.ejecutar(entornoLocal, helper)
            if condicion.tipo != TIPO_DATO.BOOLEANO:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de FOR, debe de ser de tipo booleano, pero se encontró de tipo " + obtTipoDato(condicion.tipo) )
                s.addError(err)
                helper.setConsola("[ERROR]: Se ha encontrado un error en la condicional de FOR, debe de ser de tipo booleano, pero se encontró de tipo " + obtTipoDato(condicion.tipo) + " en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                return 
            
            if condicion.valor == False:
                helper.setTs(entornoLocal2)
                break
            
            entornoLocal2 = Entorno(entornoLocal)
            entornoLocal2.setActual("For")
            if self.instrucciones != None:
                try:
                    for instruccion in self.instrucciones:
                        result = instruccion.ejecutar(entornoLocal2, helper)
                        
                        print(result)
                        if isinstance(result, Break):
                            helper.setCiclo(helperTemp)
                            helper.setTs(entornoLocal2)
                            return result
                        
                        if isinstance(result, Continue):
                            print("continue")
                            raise Exception
                        
                        if isinstance(result, Return):
                            helper.setTs(entornoLocal2)
                            return result
                        
                except Exception:
                    self.incremento.ejecutar(entornoLocal, helper)
                    continue

                self.incremento.ejecutar(entornoLocal, helper)
        helper.setTs(entornoLocal2)
        helper.setCiclo(helperTemp)

    def genArbol(self) -> Nodo:
        nodo = Nodo("FOR")
        nodo.agregarHijo(self.exp1.genArbol())
        nodo.agregarHijo(Nodo(";"))
        nodo.agregarHijo(self.condicion.genArbol())
        nodo.agregarHijo(Nodo(";"))
        nodo.agregarHijo(self.incremento.genArbol())
        instrucciones = Nodo("INSTRUCCIONES")
        for instruccion in self.instrucciones:
            instrucciones.agregarHijo(instruccion.genArbol())
        nodo.agregarHijo(instrucciones)
        return nodo