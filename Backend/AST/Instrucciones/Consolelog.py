from AST.Abstract.Instruccion import Instruccion
from AST.Expresiones.Identificador import Identificador
from AST.Expresiones.Primitivo import Primitivo
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.generador import Generador


class Consolelog(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        super().__init__()
        
    def ejecutar(self, entorno, helper):
        print('VOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOY AAA IMPRIMIIIIIIIIIR')
        listTemp = []
        exp = None
        textoLog = ""
        # VALIDAR QUE SI ES INSTANCE DE UN IDENTIFICADOR, VER SI ESE VALOR ES UNA INTERFACE
        if isinstance(self.expresion, list):
            for exp in self.expresion:
                val = exp.ejecutar(entorno, helper)
                if val.tipo == TIPO_DATO.ERROR:
                    return

                elif val.tipo == TIPO_DATO.ARRAY or val.tipo == TIPO_DATO.ARRAY_NUMBER or val.tipo == TIPO_DATO.ARRAY_STRING or val.tipo == TIPO_DATO.ARRAY_BOOLEAN:
                    array = []
                    impresion = self.ImpresionArrays(array, val.valor)
                    listTemp.append(impresion)
                elif val.tipo == TIPO_DATO.ARRAY_INTERFACE:
                    array = []
                    impresion = self.ImpresionArraysInterfaces(array, val.valor)
                    listTemp.append(impresion)
                elif val.tipo == TIPO_DATO.INTERFACE:
                    mostrarxd = "{"
                    #arrKeys = list(exp.valor.paramDeclarados.keys())
                    cont = 0
                    for vals in val.valor.paramDeclarados:
                        for dic in vals:
                            if cont != len(val.valor.paramDeclarados) - 1:
                                valuexd = vals[dic]
                                mostrarxd += dic + " : " + str(valuexd.valor) + " , "
                            else:
                                valuexd = vals[dic]
                                mostrarxd += dic + " : " + str(valuexd.valor)
                        cont += 1
                    mostrarxd += "}"
                    listTemp.append(mostrarxd)
                elif val.tipo == TIPO_DATO.BOOLEANO:
                    if val.valor == True:
                        listTemp.append("true")
                    else:
                        listTemp.append("false")
                else:
                    if val.valor == None and val.tipo == TIPO_DATO.ANY:
                        val.valor = "null"
                    elif val.valor == None and val.tipo == TIPO_DATO.NULL:
                        val.valor = "null"
                    listTemp.append(val.valor)
            for i in listTemp:
                ##print(i)
                textoLog += str(i) + " "
            helper.setConsola(textoLog)
            return

        else:
            exp = self.expresion.ejecutar(entorno, helper)
            if exp.tipo == TIPO_DATO.ERROR:
                return
            elif exp.tipo == TIPO_DATO.INTERFACE:
                mostrarxd = "{\n"
                for vals in exp.valor.paramDeclarados:
                    for dic in vals:
                        valuexd = vals[dic]
                        mostrarxd += "\t" + dic + " : " + str(valuexd.valor) + "\n"
                mostrarxd += "}"
                helper.setConsola(mostrarxd)
                return
            elif exp.tipo == TIPO_DATO.ARRAY_INTERFACE:
                array = []
                impresion = self.ImpresionArraysInterfaces(array, exp.valor)
                ##print(impresion)
                txt = "[\n"
                for i in range(len(impresion)):
                    if i != len(impresion) - 1:
                        txt += str(impresion[i]) + ",\n"
                    else:
                        txt += str(impresion[i])
                txt += "]"
                helper.setConsola(txt)
                return
            elif exp.valor == None and exp.tipo == TIPO_DATO.ANY:
                exp.valor = "null"
            elif exp.valor == None and exp.tipo == TIPO_DATO.NULL:
                exp.valor = "null"
            elif exp.tipo == TIPO_DATO.BOOLEANO:
                if exp.valor == True:
                    exp.valor = "true"
                else:
                    exp.valor = "false"

        
        ##print(exp)
        try:
            if exp.tipo == TIPO_DATO.ARRAY or exp.tipo == TIPO_DATO.ARRAY_NUMBER or exp.tipo == TIPO_DATO.ARRAY_STRING or exp.tipo == TIPO_DATO.ARRAY_BOOLEAN:

                array = []
                impresion = self.ImpresionArrays(array, exp.valor)
                ##print(impresion)
                helper.setConsola(impresion)
            else:
                print(exp.tipo)
                helper.setConsola(exp.valor)
            return
        except Exception:
            val = self.expresion.ejecutar(entorno, helper)
            helper.setConsola(val.valor)
            ###print(val.valor)
        ###print(val.valor)
        return

    def ImpresionArrays(self, arr, arrexist):
        for a in arrexist:
            if a.tipo == TIPO_DATO.ARRAY or a.tipo == TIPO_DATO.ARRAY_NUMBER or a.tipo == TIPO_DATO.ARRAY_STRING or a.tipo == TIPO_DATO.ARRAY_BOOLEAN:
                arr2 = []
                arr2 = self.ImpresionArrays(arr2, a.valor)
                arr.append(arr2)
            elif a.tipo == TIPO_DATO.INTERFACE:
                mostrarxd = "{\n"
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

    def ImpresionArraysInterfaces(self, arr, arrexist):
        for a in arrexist:
            mostrarxd = "\t{\n"
            #arrKeys = list(exp.valor.paramDeclarados.keys())
            for vals in a.valor.paramDeclarados:
                for dic in vals:
                    valuexd = vals[dic]
                    mostrarxd += "\t\t" + dic + " : " + str(valuexd.valor) + '\n'
            mostrarxd += "\t}\n"
            arr.append(mostrarxd)
        return arr
    
    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()
        print("ENTRO A IMPRIMIR")
        exp = self.expresion.genC3D(entorno, helper)
        print("IMPRIMIR CON EL TIPO:", exp.tipo)
        if exp != None:
            if isinstance(exp.valor, list):
                generador.addComment("Compilación del array")
                temporal0 = generador.addTemp()
                temporal1 = generador.addTemp()

                generador.addAsignacion(temporal0, "H")
                generador.addExpresion(temporal1, temporal0, '1', '+')
                generador.setHeap('H', len(exp.valor))

                apuntador = str(len(exp.valor)+1)
                generador.addExpresion('H', 'H', apuntador, '+')
                
                length = 0
                for val in exp.valor:
                    if val.tipo== TIPO_DATO.NUMERO:
                        generador.setHeap(temporal1, val.valor)
                        generador.addExpresion(temporal1, temporal1, '1', '+')
                        length += 1

                generador.addComment("Fin de la compilación del array")

                generador.fPrintArrayNums()
                paramTemp = generador.addTemp()
                generador.addExpresion(paramTemp, 'P', entorno.size , '+')
                generador.addExpresion(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, temporal0)
                generador.crearEntorno(entorno.size)

                generador.callFun('printArray')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retornarEntorno(entorno.size)
            else:
                if exp.tipo == TIPO_DATO.NUMERO:
                    generador.addPrint('f', exp.valor)
                elif exp.tipo == TIPO_DATO.CHAR:
                    generador.addPrintChar(exp.valor)
                elif exp.tipo == TIPO_DATO.CADENA:
                    generador.fPrintString()

                    paramTemp = generador.addTemp()
                    generador.addExpresion(paramTemp, 'P', entorno.size , '+')
                    generador.addExpresion(paramTemp, paramTemp, '1', '+')
                    generador.setStack(paramTemp, exp.valor)
                    generador.crearEntorno(entorno.size)

                    generador.callFun('printString')

                    temp = generador.addTemp()
                    generador.getStack(temp, 'P')
                    generador.retornarEntorno(entorno.size)
                elif exp.tipo == TIPO_DATO.BOOLEANO:
                    tempLbl = generador.newLabel()
                    generador.putLabel(exp.trueLabel)
                    generador.printTrue()

                    generador.addGoto(tempLbl)

                    generador.putLabel(exp.falseLabel)
                    generador.printFalse()

                    generador.putLabel(tempLbl)
                elif exp.tipo == TIPO_DATO.ARRAY_NUMBER :
                    generador.fPrintArrayNums()
                    paramTemp = generador.addTemp()
                    generador.addExpresion(paramTemp, 'P', entorno.size , '+')
                    generador.addExpresion(paramTemp, paramTemp, '1', '+')
                    generador.setStack(paramTemp, exp.valor)
                    generador.crearEntorno(entorno.size)

                    generador.callFun('printArray')

                    temp = generador.addTemp()
                    generador.getStack(temp, 'P')
                    generador.retornarEntorno(entorno.size)

            generador.addPrintChar(10.0)


    def genArbol(self) -> Nodo:
        nodo = Nodo("CONSOLE_LOG")
        if not isinstance(self.expresion, list):
            nodo.agregarHijo(self.expresion.genArbol())
        else:
            for exp in self.expresion:
                nodo.agregarHijo(exp.genArbol())
        return nodo