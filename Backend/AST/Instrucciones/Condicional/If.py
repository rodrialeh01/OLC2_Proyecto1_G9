from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Expresiones.Llamada import Llamada
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
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
        super().__init__()
        
    def ejecutar(self, entorno, helper):
        ##print("ejecutando if")
        condicion = self.expresion.ejecutar(entorno, helper)
        entornoLocal = Entorno(entorno)
        helperTemp = helper.getFuncion()
        if condicion.tipo != TIPO_DATO.BOOLEANO:
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en la condicional de IF, debe de ser de tipo booleano, pero se encontró de tipo " + obtTipoDato(condicion.tipo) )
            s.addError(err)
            helper.setConsola("[ERROR]: Se ha encontrado un error en la condicional de IF, debe de ser de tipo booleano, pero se encontró de tipo " + obtTipoDato(condicion.tipo) + " en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
            return
        
        if condicion.valor:
            entornoLocal.setActual("If")
            if self.lista_instrucciones is not None:
                for instruccion in self.lista_instrucciones:
                    accion = instruccion.ejecutar(entornoLocal, helper)
                    if isinstance(accion, Return):
                        if helper.getFuncion() == "Funcion":
                            helper.setFuncion(helperTemp)
                            return accion
                        else:
                            #error semántico
                            s = SingletonErrores.getInstance()
                            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en IF, no se puede retornar en un ambito que no sea una función" )
                            s.addError(err)
                            helper.setConsola("[ERROR]: Se ha encontrado un error en IF, no se puede retornar en un ambito que no sea una función en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                            return
                    
                    if isinstance(accion, Break):
                        if helper.getCiclo() == "ciclo":
                            return accion
                        else:
                            #error semántico
                            s = SingletonErrores.getInstance()
                            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en IF, no se puede usar BREAK en un ambito que no sea un ciclo" )
                            s.addError(err)
                            helper.setConsola("[ERROR]: Se ha encontrado un error en IF, no se puede usar BREAK en un ambito que no sea un ciclo en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                            return

                    if isinstance(accion, Continue):
                        if helper.getCiclo() == "ciclo":
                            return accion
                        else:
                            #error semántico
                            s = SingletonErrores.getInstance()
                            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en IF, no se puede usar CONTINUE en un ambito que no sea un ciclo" )
                            s.addError(err)
                            helper.setConsola("[ERROR]: Se ha encontrado un error en IF, no se puede usar CONTINUE en un ambito que no sea un ciclo en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                            return

                    if isinstance(accion, Retorno):
                        if helper.getFuncion() == "Funcion":
                            helper.setFuncion(helperTemp)
                            return accion
                        else:
                            s = SingletonErrores.getInstance()
                            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en IF, no se puede retornar en un ambito que no sea una función" )
                            s.addError(err)
                            helper.setConsola("[ERROR]: Se ha encontrado un error en IF, no se puede retornar en un ambito que no sea una función en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                            return
                helper.setTs(entornoLocal)
                return
        #if-else/ else-if
        else:
            ##print("la condición del if no es true")
            if self.lista_elseifs is not None:

                for accion in self.lista_elseifs:
                    condicion2 = accion.expresion.ejecutar(entornoLocal, helper)
                    if condicion2.tipo != TIPO_DATO.BOOLEANO:
                        s = SingletonErrores.getInstance()
                        err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en ELSE IF, debe de ser de tipo booleano, pero se encontró de tipo " + obtTipoDato(condicion2.tipo) )
                        helper.setConsola("[ERROR]: Se ha encontrado un error en ELSE IF, debe de ser de tipo booleano, pero se encontró de tipo " + obtTipoDato(condicion2.tipo) + " en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                        s.addError(err)
                        return
                    ##print("ELIF: ", condicion2.valor)
                    if condicion2.valor:
                        entornoLocal.setActual("elif")
                        ##print("vas a entrar?")
                        for ifTemp in accion.lista_instrucciones:
                            instruc = ifTemp.ejecutar(entornoLocal, helper)
                            if isinstance(instruc, Return):
                                if helper.getFuncion() == "Funcion":
                                    return instruc
                                else:
                                    #error semántico
                                    s = SingletonErrores.getInstance()
                                    err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en ELSE IF, no se puede retornar en un ambito que no sea una función" )
                                    s.addError(err)
                                    helper.setConsola("[ERROR]: Se ha encontrado un error en ELSE IF, no se puede retornar en un ambito que no sea una función en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                                    return
                            
                            if isinstance(instruc, Break):
                                if helper.getCiclo() == "ciclo":
                                    condicion2 = False
                                    return instruc
                                else:
                                    #error semántico
                                    s = SingletonErrores.getInstance()
                                    err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en ELSE IF, no se puede usar BREAK en un ambito que no sea un ciclo" )
                                    s.addError(err)
                                    helper.setConsola("[ERROR]: Se ha encontrado un error en ELSE IF, no se puede usar BREAK en un ambito que no sea un ciclo en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                                    return

                            if isinstance(instruc, Continue):
                                if helper.getCiclo() == "ciclo":
                                    return instruc
                                else:
                                    #error semántico
                                    s = SingletonErrores.getInstance()
                                    err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en ELSE IF, no se puede usar CONTINUE en un ambito que no sea un ciclo" )
                                    s.addError(err)
                                    helper.setConsola("[ERROR]: Se ha encontrado un error en ELSE IF, no se puede usar CONTINUE en un ambito que no sea un ciclo en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                                    return
                                
                            if isinstance(instruc, Retorno):
                                if helper.getFuncion() == "Funcion":
                                    helper.setFuncion(helperTemp)
                                    return instruc
                                else:
                                    s = SingletonErrores.getInstance()
                                    err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en ELSE IF, no se puede retornar en un ambito que no sea una función" )
                                    s.addError(err)
                                    helper.setConsola("[ERROR]: Se ha encontrado un error en ELSE IF, no se puede retornar en un ambito que no sea una función en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                                    return
                        
                        helper.setTs(entornoLocal)
                        return
            if self.lista_instrucciones2 is not None:
                entornoLocal.setActual("Else")
                for InstElse in self.lista_instrucciones2:
                    accionElse = InstElse.ejecutar(entornoLocal, helper)
                    if accionElse is not None:
                        if isinstance(accionElse, Return):
                            if helper.getFuncion() == "Funcion":
                                return accionElse
                            else:
                                #error semántico
                                s = SingletonErrores.getInstance()
                                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en ELSE, no se puede retornar en un ambito que no sea una función" )
                                s.addError(err)
                                helper.setConsola("[ERROR]: Se ha encontrado un error en ELSE, no se puede retornar en un ambito que no sea una función en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                                return
                                
                        if isinstance(accionElse, Break):
                            if helper.getCiclo() == "ciclo":
                                condicion2 = False
                                return accionElse
                            else:
                                #error semántico
                                s = SingletonErrores.getInstance()
                                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en ELSE, no se puede usar BREAK en un ambito que no sea un ciclo" )
                                s.addError(err)
                                helper.setConsola("[ERROR]: Se ha encontrado un error en ELSE, no se puede usar BREAK en un ambito que no sea un ciclo en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                                return

                        if isinstance(accionElse, Continue):
                            if helper.getCiclo() == "ciclo":
                                return accionElse
                            else:
                                #error semántico
                                s = SingletonErrores.getInstance()
                                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en ELSE, no se puede usar CONTINUE en un ambito que no sea un ciclo" )
                                s.addError(err)
                                helper.setConsola("[ERROR]: Se ha encontrado un error en ELSE, no se puede usar CONTINUE en un ambito que no sea un ciclo en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                                return
                        
                        if isinstance(accionElse, Retorno):
                            if helper.getFuncion() == "Funcion":
                                helper.setFuncion(helperTemp)
                                return accionElse
                            else:
                                s = SingletonErrores.getInstance()
                                err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado un error en ELSE, no se puede retornar en un ambito que no sea una función" )
                                s.addError(err)
                                helper.setConsola("[ERROR]: Se ha encontrado un error en ELSE, no se puede retornar en un ambito que no sea una función en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
                                return
                helper.setTs(entornoLocal)

    def genC3D(self, entorno, helper):
        
        gen = Generador()
        generador = gen.getInstance()

        generador.addComment("INSTRUCCIÓN IF")

        condicion = self.expresion.genC3D(entorno, helper)

        labelTrue = condicion.trueLabel
        labelFalse = condicion.falseLabel
        tempLabel = generador.newLabel()
        entornoLocal = Entorno(entorno)
        labelReturn = generador.newLabel()
        entornoLocal.returnLabel = labelReturn
        entornoLocal.size = 1 #se pone en 1 porque se reserva el espacio para el return

        generador.putLabel(labelTrue)
        for instruccion in self.lista_instrucciones:
            instruccion.genC3D(entornoLocal, helper)
            if isinstance(instruccion, Continue):
                if entorno.continueLabel != "":
                    generador.addGoto(entorno.continueLabel)
            if isinstance(instruccion, Break):
                if entorno.breakLabel != "":
                    generador.addGoto(entorno.breakLabel)
            #revisar return, break, continue
        generador.addGoto(tempLabel)
        generador.putLabel(labelFalse)
        print(tempLabel)
        #generador.addGoto(labelReturn)
        
        #generador.putLabel(labelReturn)
        if self.lista_elseifs is not None:
            generador.addComment("INSTRUCCIÓN ELSE IF")
            for elseif in self.lista_elseifs:
                condicion2 =  elseif.expresion.genC3D(entornoLocal, helper)
                labelTrueelif = condicion2.trueLabel
                labelFalseelif = condicion2.falseLabel
                generador.putLabel(labelTrueelif)

                for instruccion in elseif.lista_instrucciones:
                    instruccion.genC3D(entornoLocal, helper)
                    if isinstance(instruccion, Continue):
                        if entorno.continueLabel != "":
                            generador.addGoto(entorno.continueLabel)
                    if isinstance(instruccion, Break):
                        if entorno.breakLabel != "":
                            generador.addGoto(entorno.breakLabel)
                    #revisar return, break, continue
                generador.addGoto(tempLabel)
                generador.putLabel(labelFalseelif)

        if self.lista_instrucciones2 is not None:
            generador.addComment("INSTRUCCIÓN ELSE")
            #generador.putLabel(tempLabel)
            for instruccion in self.lista_instrucciones2:
                instruccion.genC3D(entornoLocal, helper)
                if isinstance(instruccion, Continue):
                    generador.addGoto(tempLabel)
                #revisar return, break, continue
        generador.putLabel(tempLabel)



    def genArbol(self) -> Nodo:
        nodo = Nodo("IF")
        nodo.agregarHijo(self.expresion.genArbol())#IF -> CONDICION
        instrucciones = Nodo("TRUE")
        for instruccion in self.lista_instrucciones:
            instrucciones.agregarHijo(instruccion.genArbol())
        nodo.agregarHijo(instrucciones)

        if self.lista_elseifs is not None or self.lista_instrucciones2 is not None:
            instrucciones2 = Nodo("FALSE")
            if self.lista_elseifs is not None:
                for elseif in self.lista_elseifs:
                    instrucciones2.agregarHijo(elseif.genArbol())
            
            if self.lista_instrucciones2 is not None:
                nodo3 = Nodo("ELSE")
                for instruccion in self.lista_instrucciones2:
                    nodo3.agregarHijo(instruccion.genArbol())
            
                instrucciones2.agregarHijo(nodo3)
            nodo.agregarHijo(instrucciones2)

        return nodo

