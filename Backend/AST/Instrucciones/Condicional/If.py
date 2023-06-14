from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Expresiones.Llamada import Llamada
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
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
        #print("ejecutando if")
        condicion = self.expresion.ejecutar(entorno, helper)
        entornoLocal = Entorno(entorno)
        helperTemp = helper.getFuncion()
        if condicion.tipo != TIPO_DATO.BOOLEANO:
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, debe de ser de tipo booleano, pero se encontró de tipo " + obtTipoDato(condicion.tipo) )
            s.addError(err)
            return
        
        if condicion.valor:
            entornoLocal.setActual("If")
            print("----------------if-----------------")
            if self.lista_instrucciones is not None:
                for instruccion in self.lista_instrucciones:
                    accion = instruccion.ejecutar(entornoLocal, helper)
                    #helper.setTs(entornoLocal)
                    if isinstance(accion, Return):
                        #print("lo que obtengo: ", helper.getFuncion())
                        if helper.getFuncion() == "Funcion":
                            helper.setFuncion(helperTemp)
                            return accion
                        else:
                            #error semántico
                            s = SingletonErrores.getInstance()
                            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, no se puede retornar en un ambito que no sea una función" )
                            s.addError(err)
                            return
                    
                    if isinstance(accion, Break):
                        if helper.getCiclo() == "ciclo":
                            return accion
                        else:
                            #error semántico
                            s = SingletonErrores.getInstance()
                            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, no se puede usar BREAK en un ambito que no sea un ciclo" )
                            s.addError(err)
                            return

                    if isinstance(accion, Continue):
                        if helper.getCiclo() == "ciclo":
                            return accion
                        else:
                            #error semántico
                            s = SingletonErrores.getInstance()
                            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, no se puede usar CONTINUE en un ambito que no sea un ciclo" )
                            s.addError(err)
                            return

                    if isinstance(accion, Retorno):
                        #print("VOY A RETORNAR UN RETORNO DESDE EL IF")
                        #print("lo que obtengo: ", helper.getFuncion())
                        print("VOY A RETORNAAAAAAAAAAAAAAAAR")
                        print(accion.valor)
                        if helper.getFuncion() == "Funcion":
                            helper.setFuncion(helperTemp)
                            #print(accion.valor)
                            #print(accion.tipo)
                            return accion
                return
        #if-else/ else-if
        else:
            #print("la condición del if no es true")
            if self.lista_elseifs is not None:
                for accion in self.lista_elseifs:
                    condicion2 = accion.expresion.ejecutar(entornoLocal, helper)
                    helper.setTs(entornoLocal)
                    if condicion2.tipo != TIPO_DATO.BOOLEANO:
                        s = SingletonErrores.getInstance()
                        err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, debe de ser de tipo booleano, pero se encontró de tipo " + obtTipoDato(condicion.tipo) )
                        s.addError(err)
                        return
                    #print("ELIF: ", condicion2.valor)
                    if condicion2.valor:
                        entornoLocal.setActual("elif")
                        print("----------------elif-----------------")
                        #print("vas a entrar?")
                        for ifTemp in accion.lista_instrucciones:
                            instruc = ifTemp.ejecutar(entornoLocal, helper)
                            if isinstance(instruc, Return):
                                print("RETURN")
                                if helper.getFuncion() == "Funcion":
                                    return instruc
                                else:
                                    #error semántico
                                    s = SingletonErrores.getInstance()
                                    err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, no se puede retornar en un ambito que no sea una función" )
                                    s.addError(err)
                                    return
                            
                            if isinstance(instruc, Break):
                                if helper.getCiclo() == "ciclo":
                                    condicion2 = False
                                    return instruc
                                else:
                                    #error semántico
                                    s = SingletonErrores.getInstance()
                                    err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, no se puede usar BREAK en un ambito que no sea un ciclo" )
                                    s.addError(err)
                                    return

                            if isinstance(instruc, Continue):
                                if helper.getCiclo() == "ciclo":
                                    return instruc
                                else:
                                    #error semántico
                                    s = SingletonErrores.getInstance()
                                    err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, no se puede usar CONTINUE en un ambito que no sea un ciclo" )
                                    s.addError(err)
                                    return
                                
                            if isinstance(instruc, Retorno):
                                print("VOY A RETORNAR UN RETORNO DESDE EL ELIF")
                                #print("lo que obtengo: ", helper.getFuncion())
                                if helper.getFuncion() == "Funcion":
                                    helper.setFuncion(helperTemp)
                                    #print(instruc.valor)
                                    #print(instruc.tipo)
                                    print("RETORNA ELIF: ", instruc)
                                    return instruc
                        return
            if self.lista_instrucciones2 is not None:
                print("----------------else----------------->:(")
                #print("*************************************************** entro al else")
                #print(self.lista_instrucciones2)
                print(self.lista_instrucciones2)
                entornoLocal.setActual("Else")
                for InstElse in self.lista_instrucciones2:
                    print('--------------INSTRUCCIONES DEL ELSE-----------------')
                    print(InstElse)
                    #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++INSTELSE")
                    #print(InstElse)
                    accionElse = InstElse.ejecutar(entornoLocal, helper)
                    #print("5555555555555555555555555555555555555555555555")
                    #print(accionElse)
                    helper.setTs(entornoLocal)
                    if accionElse is not None:
                        if isinstance(accionElse, Return):
                            if helper.getFuncion() == "Funcion":
                                return accionElse
                            else:
                                #error semántico
                                s = SingletonErrores.getInstance()
                                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, no se puede retornar en un ambito que no sea una función" )
                                s.addError(err)
                                return
                                
                        if isinstance(accionElse, Break):
                            if helper.getCiclo() == "ciclo":
                                condicion2 = False
                                return accionElse
                            else:
                                #error semántico
                                s = SingletonErrores.getInstance()
                                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, no se puede usar BREAK en un ambito que no sea un ciclo" )
                                s.addError(err)
                                return

                        if isinstance(accionElse, Continue):
                            if helper.getCiclo() == "ciclo":
                                return accionElse
                            else:
                                #error semántico
                                s = SingletonErrores.getInstance()
                                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, no se puede usar CONTINUE en un ambito que no sea un ciclo" )
                                s.addError(err)
                                return
                        
                        if isinstance(accionElse, Retorno):
                            #print("VOY A RETORNAR UN RETORNO DESDE EL ELSE")
                            ##print("lo que obtengo: ", helper.getFuncion())
                            if helper.getFuncion() == "Funcion":
                                helper.setFuncion(helperTemp)
                                #print(accionElse.valor)
                                #print(accionElse.tipo)
                                return accionElse

    def genArbol(self) -> Nodo:
        nodo = Nodo("IF")
        nodo.agregarHijo(self.expresion.genArbol())
        instrucciones = Nodo("INSTRUCCIONES")
        for instruccion in self.lista_instrucciones:
            instrucciones.agregarHijo(instruccion.genArbol())
        nodo.agregarHijo(instrucciones)

        
        if self.lista_elseifs is not None:
            nodo2 = Nodo("ELSE IF")
            for elseif in self.lista_elseifs:
                nodo2.agregarHijo(elseif.genArbol())
            nodo.agregarHijo(nodo2)

        if self.lista_instrucciones2 is not None:
            nodo3 = Nodo("ELSE")
            for instruccion in self.lista_instrucciones2:
                nodo3.agregarHijo(instruccion.genArbol())
        
            nodo.agregarHijo(nodo3)

        return nodo

