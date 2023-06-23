from AST.Abstract.Expresion import Expresion
from AST.Expresiones.Llamada import Llamada
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno2 import Retorno2

arr = []
class Array(Expresion):
    
    def __init__(self, expresiones, linea, columna):
        self.tipo = TIPO_DATO.ANY
        self.expresiones = expresiones
        self.linea = linea
        self.columna = columna
        super().__init__()


    def ejecutar(self, entorno, helper):
        global arr
        arr = []
        if not isinstance(self.expresiones, Llamada):
            for exp in self.expresiones:
                arr.append(exp.ejecutar(entorno, helper))
            retor = Retorno(arr, TIPO_DATO.ARRAY)
            return retor
        else:
            a = self.expresiones.ejecutar(entorno, helper)
            return self.expresiones.ejecutar(entorno, helper)
    
    def ImpresionArrays(self, arr, arrexist):
        for a in arrexist:
            if a.tipo == TIPO_DATO.ARRAY or a.tipo == TIPO_DATO.ARRAY_NUMBER or a.tipo == TIPO_DATO.ARRAY_STRING or a.tipo == TIPO_DATO.ARRAY_BOOLEAN:
                arr2 = []
                arr2 = self.ImpresionArrays(arr2, a.valor)
                arr.append(arr2)
            elif a.tipo == TIPO_DATO.INTERFACE:
                mostrarxd = "{"
                #print(a.valor.paramDeclarados)
                for vals in a.valor.paramDeclarados:
                    for dic in vals:
                        valuexd = vals[dic]
                        mostrarxd += dic + " : " + str(valuexd.valor) + " "
                mostrarxd += "}"
                arr.append(mostrarxd)
            else:
                arr.append(a.valor)
        return arr

    def genArbol(self):
        global arr
        nuevo = []
        mostrar = self.ImpresionArrays(nuevo,arr)
        return Nodo(mostrar)
    
    def genC3D(self, entorno, helper):
        print("GENERACIÓN DE ARRAY: ")
        gen = Generador()
        generador = gen.getInstance()
        #verificar si es una llamada
        global arr
        arr = []
        if isinstance(self.expresiones, Llamada):
            pass
        else:
            for exp in self.expresiones:
                exp.genC3D(entorno, helper)
                arr.append(exp)
            print(arr.shape)
            ret = Retorno2(arr, TIPO_DATO.ARRAY, False)
            return ret

        