from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores


class ForOf(Instruccion):
    def __init__(self, variable, exp1, instrucciones, fila, columna):
        self.variable = variable
        self.exp1 = exp1
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        super().__init__()

    def ejecutar(self, entorno, helper):
        entornoLocal = Entorno(entorno)

        val = self.exp1.ejecutar(entornoLocal, helper)
        entornoLocal2 = Entorno(entornoLocal)
        helperTemp = helper.getCiclo()
        helper.setCiclo("ciclo")

        #print(str(val.tipo))
        if val.tipo == TIPO_DATO.CADENA:
            for v in val.valor:
                
                simboloInterno = Simbolo()
                simboloInterno.linea = self.fila
                simboloInterno.columna = self.columna
                simboloInterno.nombre = self.variable
                simboloInterno.tipo = TIPO_DATO.CADENA
                simboloInterno.valor = v
                entornoLocal.AgregarSimbolo(simboloInterno.nombre, simboloInterno)
                try:
                    for instruccion in self.instrucciones:
                        result = instruccion.ejecutar(entornoLocal, helper)
                        #helper.setTs(entornoLocal)
                        if isinstance(result, Break):
                            helper.setCiclo(helperTemp)
                            helper.setTs(entornoLocal)
                            return result
                        
                        if isinstance(result, Continue):
                            raise Exception
                        
                        if isinstance(result, Return):
                            return result
                except Exception:
                    continue
        elif val.tipo == TIPO_DATO.ARRAY or val.tipo == TIPO_DATO.ARRAY_BOOLEAN or val.tipo == TIPO_DATO.ARRAY_NUMBER or val.tipo == TIPO_DATO.ARRAY_STRING or val.tipo == TIPO_DATO.ARRAY_INTERFACE:
            for v in val.valor:
                entornoLocal2.setActual("ForOf")
                simboloInterno = Simbolo()
                simboloInterno.linea = self.fila
                simboloInterno.columna = self.columna
                simboloInterno.nombre = self.variable
                simboloInterno.tipo = v.tipo
                simboloInterno.valor = v.valor
                entornoLocal.AgregarSimbolo(simboloInterno.nombre, simboloInterno)
                try:
                    for instruccion in self.instrucciones:
                        #print(instruccion)
                        result = instruccion.ejecutar(entornoLocal2, helper)
                        
                        if isinstance(result, Break):
                            helper.setTs(entornoLocal)
                            helper.setTs(entornoLocal2)
                            helper.setCiclo(helperTemp)
                            return result
                        
                        if isinstance(result, Continue):
                            raise Exception
                        
                        if isinstance(result, Return):
                            return result
                except Exception:
                    continue
        else:
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "Se ha encontrado una variable de tipo" + obtTipoDato(val.tipo) + " no compatible dentro del ForOf" )
            s.addError(err)
            helper.setConsola("[ERROR]: Se ha encontrado una variable de tipo " + obtTipoDato(val.tipo) + "no compatible dentro del ForOf en la linea: " + str(self.fila)+ " y columna: " + str(self.columna))
            return
        
        helper.setTs(entornoLocal)
        helper.setTs(entornoLocal2)
        helper.setCiclo(helperTemp)
                
    def genArbol(self) -> Nodo:
        nodo = Nodo("FOR-OF")
        nodo.agregarHijo(Nodo(str(self.variable)))
        nodo.agregarHijo(self.exp1.genArbol())
        instrucciones = Nodo("INSTRUCCIONES")
        for instruccion in self.instrucciones:
            instrucciones.agregarHijo(instruccion.genArbol())
        nodo.agregarHijo(instrucciones)
        return nodo
    
    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()

        entornoLocal = Entorno(entorno)
        entornoLocal2 = Entorno(entornoLocal)

        generador.addComment("Inicia ForOf")
        val = self.exp1.genC3D(entornoLocal, helper)
        if val.tipo == TIPO_DATO.CADENA:


            temp = generador.addTemp() # t2
            generador.getStack(temp,val.valor)

            temp2 = generador.addTemp() # t3
            s = entornoLocal2.setEntorno(self.variable, TIPO_DATO.CADENA, False)
            generador.getHeap(temp2,temp)

            regreso = generador.newLabel()
            generador.addGoto(regreso)
            generador.putLabel(regreso)

            labelins = generador.newLabel()
            labelsalida = generador.newLabel()
            generador.addIf(temp2, "-1", '!=', labelins)
            generador.addGoto(labelsalida)

            generador.putLabel(labelins)
            for instruccion in self.instrucciones:
                generador.addComment("Instruccion ForOf")
                result = instruccion.genC3D(entornoLocal2, helper)
            
            generador.addExpresion(temp, temp, "1", "+")
            #generador.addAsignacion(self.variable, temp2)
            generador.getHeap(temp2,temp)
            print("temp:", temp)
            print(generador.codigo)
            generador.addGoto(regreso)

            generador.putLabel(labelsalida)
            

            '''
                t2 = stack[int(t1)]
                declaracion y se asigna el heap[int(t2)]
                t3 = heap[int(t2)]
                goto L1
                L1:
                if t3 != -1: goto L2
                goto L3
                L2:
                for instruccion in self.instrucciones:
                    result = instruccion.genC3D(entornoLocal, helper)
                t2 = t2 + 1
                t3 = heap[int(t2)]
                goto L1
                L3:
                    salida
            '''
        #for (let i of arreglo) {
        # instrucciones
        #}

        # declaracion: genc3d
        # condicion: genc3d
        # instrucciones: genc3d
        