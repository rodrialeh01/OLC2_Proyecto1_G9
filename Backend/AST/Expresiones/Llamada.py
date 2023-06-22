from AST.Abstract.Expresion import Expresion
from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Instrucciones.Transferencia.Return import Return
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
                
                #val = param.genC3D(entorno, helper)
                #if val.tipo == TIPO_DATO.ERROR:
                #    return Retorno2(None, TIPO_DATO.ERROR, False)
                if isinstance(param, Llamada):
                    print('Llamada a función en llamada a función')
                    self.guardarTemps(generador, entorno, temps)
                    a = param.genC3D(entorno, helper)
                    parametros.append(a)
                    self.recuperarTemps(generador, entorno, temps)
                else:
                    val = param.genC3D(entorno, helper)
                    parametros.append(val)
                    temps.append(val.valor)
        
        temp = generador.addTemp()
        print('Llamada: ', temp)
        generador.addComment(" VOY A GENERAR: " + str(temp))
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
        print('a')
        generador.getStack(temp, 'P')
        generador.retornarEntorno(size)
        generador.addComment('Fin llamada a función ' + self.id)
        print('a')


        if fn.tipo is not None:
            if fn.tipo != TIPO_DATO.BOOLEANO:
                re =  Retorno2(temp, fn.tipo, False)
                return re
            else:
                generador.addComment('Recuperando el booleano')
                if self.trueLabel == '':
                    self.trueLabel = generador.newLabel()
                if self.falseLabel == '':
                    self.falseLabel = generador.newLabel()
                generador.addIf(temp, 1, '==', self.trueLabel)
                generador.addGoto(self.falseLabel)
                ret = Return(temp, 0,0)
                ret.trueLabel = self.trueLabel
                ret.falseLabel = self.falseLabel
                generador.addComment('Fin recuperando el booleano')
                return ret

    def guardarTemps(self, generador, tabla, tmp2):
        generador.addComment('Guardando temporales de llamada a función ' + self.id)
        tmp = generador.addTemp()
        print('TMP:', tmp)
        for tmp1 in tmp2:
            print('TMP1:', tmp1)
            generador.addExpresion(tmp, 'P', tabla.size, '+')
            generador.setStack(tmp, tmp1)
            tabla.size += 1
        generador.addComment('Fin guardando temporales de llamada a función ' + self.id)
    
    def recuperarTemps(self, generador, tabla, tmp2):
        generador.addComment('Recuperando temporales de llamada a función ' + self.id)
        tmp = generador.addTemp()
        print('recuperando TMP:', tmp)
        for tmp1 in tmp2:
            tabla.size -= 1
            generador.addExpresion(tmp, 'P', tabla.size, '+')
            generador.getStack(tmp1, tmp)
        generador.addComment('Fin recuperando temporales de llamada a función ' + self.id)


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
    