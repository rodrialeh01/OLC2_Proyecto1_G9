from AST.Abstract.Expresion import Expresion
from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Retorno2 import Retorno2
from AST.SingletonErrores import SingletonErrores


class Llamada(Instruccion, Expresion):
    def __init__(self, id, params, linea, columna):
        self.linea = linea
        self.columna = columna
        self.id = id
        self.params = params
        super().__init__()

    def ejecutar(self, entorno, helper):
        #print("Ejecutando llamada a función")
        fn = entorno.ExisteFuncion(self.id)
        helperTemp = helper.getFuncion()

        if fn is False:
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "La función " + self.id + " no existe en el entorno actual")
            s.addError(err)
            helper.setConsola("[ERROR]: La función " + self.id + " no existe en el entorno actual " + " en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
            return Retorno(None, TIPO_DATO.ERROR)

        entornoFN = Entorno(entorno)
        entornoFN.actual = "Función " + str(self.id)
        func = entorno.ObtenerFuncion(self.id)

        argumentos = func.declaracionesParams(entornoFN, self.params, entorno, helper)
        
        if argumentos is False:
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "La cantidad de parámetros de la función "+ self.id+" no coincide con la cantidad de argumentos")
            s.addError(err)
            helper.setConsola("[ERROR]: La cantidad de parámetros de la función "+ self.id+" no coincide con la cantidad de argumentos " + " en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
            return Retorno(None, TIPO_DATO.ERROR)
        

        if func is not None:
            ret = func.ejecutar(entornoFN, helper)
            if ret is not None:
                helper.setFuncion(helperTemp)
                return Retorno(ret.valor, ret.tipo)
    
    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()

        fun = entorno.ExisteFuncion(self.id)
        fn = entorno.ObtenerFuncion(self.id)
        if fun is False:
            print("La función " + self.id + " no existe en el entorno actual")
            generador.addComment("La función " + self.id + " no existe en el entorno actual")
            return Retorno(None, TIPO_DATO.ERROR)
        
        generador.addComment("Llamada a función " + self.id)
        parametros = []
        temps = []
        size = entorno.size
        if self.params is not None:
            for param in self.params:
                val = param.genC3D(entorno, helper)
                if val.tipo == TIPO_DATO.ERROR:
                    return Retorno2(None, TIPO_DATO.ERROR, False)
                parametros.append(val)
                temps.append(val.valor)
        
        temp = generador.addTemp()

        generador.addExpresion(temp, 'P',size+1,'+')

        aux = 0

        if fn.params is not None:
            if len(fn.params) == len(parametros):
                for param in parametros:
                    if fn.params[aux].tipo == param.tipo:
                        aux += 1
                        generador.setStack(temp, param.valor)
                        if aux != len(parametros):
                            generador.addExpresion(temp, temp, 1, '+')
                    else:
                        generador.addComment('Error en la llamada a función ' + self.id)
                        return Retorno2(None, TIPO_DATO.ERROR, False)
                
        generador.crearEntorno(size)
        generador.callFun(fn.nombre)
        generador.getStack(temp, 'P')
        generador.retornarEntorno(size)
        generador.addComment('Fin llamada a función ' + self.id)

        

    def genArbol(self):
        nodo = Nodo("LLAMADA FUNCIÓN")
        nodohijo = Nodo(self.id)
        nodohijo3 = Nodo("PARAMETROS")
        nodo.agregarHijo(nodohijo)
        if self.params is not None:
            for param in self.params:
                nodohijo3.agregarHijo(param.genArbol())
            nodo.agregarHijo(nodohijo3)
        return nodo
    