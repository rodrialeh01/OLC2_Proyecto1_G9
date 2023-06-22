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
            #se declara la variable
            temp = generador.addTemp() 
            entornoLocal2.setEntorno(self.variable, TIPO_DATO.CHAR, False)
            # obtenemos el simbolo
            s_c3d = entornoLocal2.ObtenerSimbolo(self.variable)
            # seteamos el valor en el stack
            generador.setStack(s_c3d.posicion, val.valor) 
            
            # Se crea la etiaquta donde iniciara el for
            regreso = generador.newLabel()
            generador.addGoto(regreso)

            #Desde aqui empieza la etiqueta donde inicia el for
            generador.putLabel(regreso)
            
            generador.getStack(temp,s_c3d.posicion) #se obtiene en el temp la posicion de la variable que se guardó en el stack; temp = stack[s_c3d.posicion]
            temp2 = generador.addTemp()
            generador.getHeap(temp2, temp) #se obtiene en el temp2 el valor que se guardó en el heap; temp2 = heap[temp]
            
            #Se crea la etiqueta donde se encontraran las instrucciones del for-of 
            labelins = generador.newLabel()
            labelsalida = generador.newLabel() #etiqueta para salir del ciclo

            #Se valida que el valor que se encuentra en el heap sea diferente de -1
            generador.addIf(temp2, "-1", '!=', labelins)
            #en caso contrario se sale del ciclo
            generador.addGoto(labelsalida)

            #Se pone la etiqueta de instrucciones
            generador.putLabel(labelins)

            #Se agregan las instrucciones
            for instruccion in self.instrucciones:
                generador.addComment("Instruccion ForOf")
                result = instruccion.genC3D(entornoLocal2, helper)
                #verificar los break, return y continue
            
            temp3 = generador.addTemp() #se crea un nuevo temporal
            generador.getStack(temp3, s_c3d.posicion) #la posición de la varible/símbolo se asigna al temporal para irlo actualizando posteriormente
            generador.addExpresion(temp3, temp3, "1", "+") # se agrega un +1 a la posición para continuar con el siguiente char
            generador.setStack(s_c3d.posicion, temp3) #se actualiza el valor de la variable/simbolo (stack[s_c3d.posicion] = temp3)
            generador.addGoto(regreso) # se pone el goto para que regrese a validar la condición del for
            generador.putLabel(labelsalida) # se pone la etiqueta de salida del ciclo
        