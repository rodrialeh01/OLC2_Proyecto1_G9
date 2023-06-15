from AST.Abstract.Instruccion import Instruccion
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores
from AST.Error import Error
from AST.Simbolos.Enums import obtTipoDato

class ForOf(Instruccion):
    def __init__(self, variable, exp1, instrucciones, fila, columna):
        self.variable = variable
        self.exp1 = exp1
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        entornoLocal = Entorno(entorno)

        val = self.exp1.ejecutar(entornoLocal, helper)
        entornoLocal2 = Entorno(entornoLocal)
        helperTemp = helper.getCiclo()
        helper.setCiclo("ciclo")

        print(str(val.tipo))
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
                        print(instruccion)
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
        nodo = Nodo("FOR")
        nodo.agregarHijo(Nodo(str(self.variable)))
        nodo.agregarHijo(Nodo("of"))
        nodo.agregarHijo(self.exp1.genArbol())
        instrucciones = Nodo("INSTRUCCIONES")
        for instruccion in self.instrucciones:
            instrucciones.agregarHijo(instruccion.genArbol())
        nodo.agregarHijo(instrucciones)
        return nodo