from AST.Abstract.Instruccion import Instruccion
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO


class ElseIf(Instruccion):
    def __init__(self, expresion, lista_instrucciones, fila, columna):
        self.expresion = expresion
        self.lista_instrucciones = lista_instrucciones
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, entorno, helper):
        condicion = self.expresion.ejecutar(entorno, helper)
        entornoLocal = Entorno(entorno)
        if condicion.tipo != TIPO_DATO.BOOLEANO:
            #error semántico
            pass
        if condicion.valor:
            for instruccion in self.lista_instrucciones:
                accion = instruccion.ejecutar(entornoLocal, helper)
                
                if isinstance(accion, Return):
                    if helper.getFuncion == "funcion":
                        return accion
                    else:
                        #error semántico
                        pass
                
                if isinstance(accion, Break):
                    if helper.getCiclo == "ciclo":
                        return accion
                    else:
                        #error semántico
                        pass

                if isinstance(accion, Continue):
                    if helper.getCiclo == "ciclo":
                        return accion
                    else:
                        #error semántico
                        pass
            return