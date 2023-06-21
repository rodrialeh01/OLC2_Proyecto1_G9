from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.SingletonErrores import SingletonErrores


class While(Instruccion):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        super().__init__()

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

    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()

        entornoLocal = Entorno(entorno)
        
        

        lblprinc = generador.newLabel() # L0:
        generador.putLabel(lblprinc)

        condicion = self.condicion.genC3D(entornoLocal, generador)
        
        if condicion.tipo != TIPO_DATO.BOOLEANO:
            generador.addComment("Error Semantico, la condición a evaluar del while no es booleana")
            pass

        labelT = condicion.trueLabel
        labelF = condicion.falseLabel

        generador.putLabel(labelT) # L1:
        tempbool = generador.addTemp()
        generador.addExpresion(tempbool, "1", "", "")
        lbl_new = generador.newLabel()
        generador.addGoto(lbl_new)

        generador.putLabel(labelF) # L2:
        generador.addExpresion(tempbool, "0", "", "")
        
        generador.putLabel(lbl_new) # L3:
        lbl_ins = generador.newLabel()
        lbl_salida = generador.newLabel()
        generador.addIf(tempbool, "1", "==", lbl_ins)
        generador.addGoto(lbl_salida)

        entornoLocal.breakLabel = lbl_salida
        entornoLocal.continueLabel = lblprinc

        generador.putLabel(lbl_ins) # L4:
        for instruccion in self.instrucciones:
            instruccion.genC3D(entornoLocal, generador)
            if isinstance(instruccion, Break):
                generador.addGoto(lbl_salida)
            if isinstance(instruccion, Continue):
                generador.addGoto(lblprinc)
            if isinstance(instruccion, Return):
                generador.addGoto(lbl_salida)
        
        generador.addGoto(lblprinc)

        generador.putLabel(lbl_salida) # L5:


    def genArbol(self):
        nodo = Nodo("WHILE")
        nodo.agregarHijo(self.condicion.genArbol())
        if self.instrucciones != None:
            ins = Nodo("INSTRUCCIONES")
            for instruccion in self.instrucciones:
                ins.agregarHijo(instruccion.genArbol())
            nodo.agregarHijo(ins)
        return nodo
