from AST.Abstract.Instruccion import Instruccion
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Simbolo import Simbolo


class ForOf(Instruccion):
    def __init__(self, variable, exp1, instrucciones, fila, columna):
        self.variable = variable
        self.exp1 = exp1
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, helper):
        entornoLocal = Entorno(entorno)
        entornoLocal.setActual("ForOf")
        val = self.exp1.ejecutar(entornoLocal, helper)
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
                        if isinstance(result, Break):
                            helper.setCiclo(helperTemp)
                            return result
                        
                        if isinstance(result, Continue):
                            raise Exception
                        
                        if isinstance(result, Return):
                            return result
                except Exception:
                    continue
        elif val.tipo == TIPO_DATO.ARRAY or val.tipo == TIPO_DATO.ARRAY_BOOLEAN or val.tipo == TIPO_DATO.ARRAY_NUMBER or val.tipo == TIPO_DATO.ARRAY_STRING:
            for v in val.valor:
                simboloInterno = Simbolo()
                simboloInterno.linea = self.fila
                simboloInterno.columna = self.columna
                simboloInterno.nombre = self.variable
                simboloInterno.tipo = v.tipo
                simboloInterno.valor = v.valor
                entornoLocal.AgregarSimbolo(simboloInterno.nombre, simboloInterno)
                try:
                    for instruccion in self.instrucciones:
                        result = instruccion.ejecutar(entornoLocal, helper)
                        if isinstance(result, Break):
                            helper.setCiclo(helperTemp)
                            return result
                        
                        if isinstance(result, Continue):
                            raise Exception
                        
                        if isinstance(result, Return):
                            return result
                except Exception:
                    continue

        helper.setCiclo(helperTemp)
                
