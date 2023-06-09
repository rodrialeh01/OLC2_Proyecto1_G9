from AST.Abstract.Instruccion import Instruccion
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO


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
        
        while condTemp == True:
            condicion = self.condicion.ejecutar(entorno, helper)
            
            if condicion.tipo != TIPO_DATO.BOOLEANO:
                    #error semantico
                    pass
            if self.instrucciones != None:
                try:
                    if condicion.valor != condTemp:
                        condTemp = False
                        helper.setCiclo(helperTemp)
                        return

                    #if condicion.valor:
                    entorno_local = Entorno(entorno)
                    entorno_local.setActual("while")
                    for instruccion in self.instrucciones:
                        result = instruccion.ejecutar(entorno_local, helper)
    
                        if isinstance(result, Break):
                            helper.setCiclo(helperTemp)
                            condTemp = False
                            return result
                        
                        if isinstance(result, Continue):
                            raise Exception
                            
                        if isinstance(result, Return):
                            return result

                except Exception:
                    continue
        
        helper.setCiclo(helperTemp)
