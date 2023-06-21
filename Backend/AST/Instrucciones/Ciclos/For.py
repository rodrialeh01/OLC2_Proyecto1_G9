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


class For(Instruccion):
    def __init__(self, exp1, condicion, incremento, instrucciones, fila, columna):
        self.exp1 = exp1 
        self.condicion = condicion
        self.incremento = incremento
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        super().__init__()


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
                        
                        #print(result)
                        if isinstance(result, Break):
                            helper.setCiclo(helperTemp)
                            helper.setTs(entornoLocal2)
                            return result
                        
                        if isinstance(result, Continue):
                            #print("continue")
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
        nodo.agregarHijo(self.condicion.genArbol())
        nodo.agregarHijo(self.incremento.genArbol())
        instrucciones = Nodo("INSTRUCCIONES")
        for instruccion in self.instrucciones:
            instrucciones.agregarHijo(instruccion.genArbol())
        nodo.agregarHijo(instrucciones)
        return nodo

    def genC3D(self, entorno, helper):
        # for dec/asig ; cond ; inc/dec:  Instrucciones
        gen = Generador()
        generador = gen.getInstance()

        generador.addComment("INICIO FOR")
        entornoLocal = Entorno(entorno)
        
        lblPrincipal = generador.newLabel()
        generador.addGoto(lblPrincipal)
        generador.putLabel(lblPrincipal) # L0: INS DECLARACION
        self.exp1.genC3D(entornoLocal, helper)
        
        lblCondicion = generador.newLabel() # L1: INS CONDICION
        generador.putLabel(lblCondicion)
        condicion = self.condicion.genC3D(entornoLocal, helper)
        
        self.trueLabel = condicion.trueLabel
        self.falseLabel = condicion.falseLabel

        generador.putLabel(self.trueLabel)
        tempbool = generador.addTemp()
        generador.addExpresion(tempbool, "1", "", "")
        lbl_new = generador.newLabel()
        generador.addGoto(lbl_new)
        
        generador.putLabel(self.falseLabel)
        generador.addExpresion(tempbool, "0", "", "")

        generador.putLabel(lbl_new) # L3:
        lbl_ins = generador.newLabel()
        lbl_salida = generador.newLabel()
        generador.addIf(tempbool, "1", "==", lbl_ins)
        generador.addGoto(lbl_salida)

        entornoLocal.breakLabel = lbl_salida
        entornoLocal.continueLabel = lblCondicion

        generador.putLabel(lbl_ins) # L4:
        for instruccion in self.instrucciones:
            instruccion.genC3D(entornoLocal, generador)
            if isinstance(instruccion, Break):
                generador.addGoto(lbl_salida)
            if isinstance(instruccion, Continue):
                generador.addGoto(lblCondicion)
            if isinstance(instruccion, Return):
                generador.addGoto(lbl_salida)
        
        self.incremento.genC3D(entornoLocal, generador)

        generador.addGoto(lblCondicion)

        generador.putLabel(lbl_salida) # L5:
