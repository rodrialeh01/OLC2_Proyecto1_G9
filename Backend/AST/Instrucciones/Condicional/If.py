from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.SingletonErrores import SingletonErrores


class If(Instruccion):
    def __init__(self, expresion, lista_instrucciones, lista_elseifs, lista_instrucciones2, fila, columna):
        self.expresion = expresion
        self.lista_instrucciones = lista_instrucciones
        self.lista_elseifs = lista_elseifs
        self.lista_instrucciones2 = lista_instrucciones2
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        condicion = self.expresion.ejecutar(entorno, helper)

        entornoLocal = Entorno(entorno)
        if condicion.tipo != TIPO_DATO.BOOLEANO:
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, debe de ser de tipo booleano, pero se encontró de tipo " + obtTipoDato(condicion.tipo) )
            s.addError(err)
            return
        
        if condicion.valor:
            for instruccion in self.lista_instrucciones:
                accion = instruccion.ejecutar(entornoLocal, helper)
                if isinstance(accion, Return):
                    if helper.getFuncion == "funcion":
                        return accion
                    else:
                        pass
                        #error semántico
                
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

        #if-else/ else-if
        else:
            for accion in self.lista_elseifs:
                condicion2 = accion.expresion.ejecutar(entornoLocal, helper)  
                if condicion2.tipo != TIPO_DATO.BOOLEANO:
                    s = SingletonErrores.getInstance()
                    err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, debe de ser de tipo booleano, pero se encontró de tipo " + obtTipoDato(condicion.tipo) )
                    s.addError(err)
                    return
                    
                if condicion2.valor:
                    
                    for ifTemp in accion.lista_instrucciones:
                        instruc = ifTemp.ejecutar(entornoLocal, helper)

                        if instruc is not None:
                            if isinstance(accion, Return):
                                if helper.getFuncion == "funcion":
                                    return accion
                                else:
                                    pass
                                    #error semántico
                            
                            if isinstance(accion, Break):
                                if helper.getCiclo == "ciclo":
                                    condicion2 = False
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

            for InstElse in self.lista_instrucciones2:
                accionElse = InstElse.ejecutar(entornoLocal, helper)
                if accionElse is not None:
                    if isinstance(accion, Return):
                        if helper.getFuncion == "funcion":
                            return accion
                        else:
                            pass
                            #error semántico
                            
                    if isinstance(accion, Break):
                        if helper.getCiclo == "ciclo":
                            condicion2 = False
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