from AST.Abstract.Instruccion import Instruccion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO


class Consolelog(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        
    def ejecutar(self, entorno, helper):
        listTemp = []
        exp = None
        textoLog = ""
        if isinstance(self.expresion, list):
            print("ENTRÉ AL LIST")
            for exp in self.expresion:
                val = exp.ejecutar(entorno, helper)
                if val.tipo == TIPO_DATO.ARRAY or val.tipo == TIPO_DATO.ARRAY_NUMBER or val.tipo == TIPO_DATO.ARRAY_STRING or val.tipo == TIPO_DATO.ARRAY_BOOLEAN:
                    array = []
                    impresion = self.ImpresionArrays(array, val.valor)
                    print(impresion)
                    listTemp.append(impresion)
                else:
                    print("QUIERO REVISARRRRR 1: ", val.valor)
                    listTemp.append(val.valor)
            for i in listTemp:
                #print(i)
                textoLog += str(i) + " "
            helper.setConsola(textoLog)
            return

        else:
            print("ENTRÉ AL ELSE")
            exp = self.expresion.ejecutar(entorno, helper)
            print("Estoy llegando al consolelog")
            print(exp.valor)

        
        #print(exp)
        try:
           
            if exp.tipo == TIPO_DATO.ARRAY or exp.tipo == TIPO_DATO.ARRAY_NUMBER or exp.tipo == TIPO_DATO.ARRAY_STRING or exp.tipo == TIPO_DATO.ARRAY_BOOLEAN:

                array = []
                impresion = self.ImpresionArrays(array, exp.valor)
                #print(impresion)
                helper.setConsola(impresion)
            else:
                #print(exp.valor)
                helper.setConsola(exp.valor)

        except Exception:
            val = self.expresion.ejecutar(entorno, helper)
            helper.setConsola(val.valor)
            ##print(val.valor)
        ##print(val.valor)
        

    def ImpresionArrays(self, arr, arrexist):
        for a in arrexist:
            if a.tipo == TIPO_DATO.ARRAY or a.tipo == TIPO_DATO.ARRAY_NUMBER or a.tipo == TIPO_DATO.ARRAY_STRING or a.tipo == TIPO_DATO.ARRAY_BOOLEAN:
                arr2 = []
                arr2 = self.ImpresionArrays(arr2, a.valor)
                arr.append(arr2)
            else:
                arr.append(a.valor)
        return arr
    
    def genArbol(self) -> Nodo:
        nodo = Nodo("CONSOLE_LOG")
        nodo.agregarHijo(self.expresion.genArbol())
        return nodo