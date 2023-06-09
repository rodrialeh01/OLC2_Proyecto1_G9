from AST.Abstract.Instruccion import Instruccion
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return

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
        val1 = self.exp1.ejecutar(entornoLocal, helper)
        helperTemp = helper.getCiclo()
        helper.setCiclo("ciclo")

        while True:
            condicion = self.condicion.ejecutar(entornoLocal, helper)
            if condicion.tipo != TIPO_DATO.BOOLEANO:
                #error semantico
                pass
            
            if condicion.valor == False:
                break
            
            entornoLocal2 = Entorno(entornoLocal)
            entornoLocal2.setActual("for")
            if self.instrucciones != None:
                try:
                    for instruccion in self.instrucciones:
                        result = instruccion.ejecutar(entornoLocal2, helper)
                        print(result)
                        if isinstance(result, Break):
                            helper.setCiclo(helperTemp)
                            return result
                        
                        if isinstance(result, Continue):
                            print("continue")
                            raise Exception
                        
                        if isinstance(result, Return):
                            return result
                        
                except Exception:
                    self.incremento.ejecutar(entornoLocal, helper)
                    continue

                self.incremento.ejecutar(entornoLocal, helper)

        helper.setCiclo(helperTemp)