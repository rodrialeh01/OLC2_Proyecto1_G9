from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Retorno2 import Retorno2
from AST.SingletonErrores import SingletonErrores


class AccesoArray(Expresion):
    def __init__(self, id, accesos, linea, columna):
        self.id = id
        self.accesos = accesos
        self.linea = linea
        self.columna = columna
        super().__init__()


    def ejecutar(self, entorno, helper):
        #buscar el id en el entorno
        existe = entorno.ExisteSimbolo(self.id)
        if not existe:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La variable " + self.id + " no existe en el entorno actual" )
            s.addError(err)
            helper.setConsola("[ERROR]: La variable " + self.id + " no existe en el entorno actual " + " en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
            Retorno(None, TIPO_DATO.ERROR)
        
        simbolo = entorno.ObtenerSimbolo(self.id)
        print("-------------------------------")
        print(simbolo.tipo)
        listaAccesos = []
        #verificar que sea un array
        for a in self.accesos:
            print(a)
            listaAccesos.append(a.ejecutar(entorno, helper).valor)
        xd = self.accesar(listaAccesos, simbolo, entorno, helper)
        print("XXDXDXD", xd)
        return xd

    def accesar(self, pila, lista, entorno, helper):
        print("UNA VEZ: ", pila)
        if len(pila) == 0:
            return lista
        else:
            index = pila.pop(0)
            try:
                valor = lista.valor[index]
                #print(isinstance(valor, Retorno))
            except:
                #error semantico
                #print("ERROR SOTE")
                s = SingletonErrores.getInstance()
                err = Error(self.linea, self.columna, "Error Semántico", "El indice al que se intenta acceder no existe en el array")
                s.addError(err)
                helper.setConsola("[ERROR]: El indice al que se intenta acceder no existe en el array en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
                return Retorno(None, TIPO_DATO.ERROR)
            if len(pila) == 0 and isinstance(valor, Retorno)==False:
                return Retorno(valor, TIPO_DATO.CADENA)
            elif valor.tipo == TIPO_DATO.ARRAY :
                return self.accesar(pila, valor, entorno, helper)
            elif valor.tipo == TIPO_DATO.CADENA and len(pila) > 0 and len(valor.valor)> 1:
                return self.accesar(pila, valor, entorno, helper)
            else:
                if len(pila) == 0:
                    #print(lista.valor[index])
                    return lista.valor[index]
                else:
                    #error semantico
                    s = SingletonErrores.getInstance()
                    err = Error(self.linea, self.columna, "Error Semántico", "No se puede acceder al valor que se intenta acceder al array")
                    s.addError(err)
                    #print("esto es un ERRRRRRRRROR")
                    helper.setConsola("[ERROR]: No se puede acceder al valor que se intenta acceder al array en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
                    return Retorno(None, TIPO_DATO.ERROR)

    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()
        #buscar el id en el entorno
        existe = entorno.ExisteSimbolo(self.id)
        if not existe:
            generador.addComment("La variable " + self.id + " no existe en el entorno actual")
            return 

        sim = entorno.ObtenerSimbolo(self.id)
        print(sim.dimensiones)
        if sim.tipo != TIPO_DATO.ARRAY and sim.tipo != TIPO_DATO.ARRAY_STRING and sim.tipo != TIPO_DATO.ARRAY_NUMBER and sim.tipo != TIPO_DATO.ARRAY_BOOLEAN and sim.tipo != TIPO_DATO.CADENA:
            generador.addComment("La variable " + self.id + " no es un array, es un " + obtTipoDato(sim.tipo))
            return
        
        posicion = sim.posicion

        #quemado que solo hay 1 acceso
        print("aynooooooooooo", len(sim.dimensiones))

        
        print("ayno", len(sim.dimensiones))
        if len(sim.dimensiones) <= 1:
            print("UNA DIMENSION")
            if len(self.accesos) > 1:
                generador.addComment("Solo se puede acceder a un indice a la vez")
                return
            
            tempAcceso = generador.addTemp()
            acceso = self.accesos[0].genC3D(entorno, helper).valor
            generador.addAsignacion(tempAcceso, acceso)
            #C3D
            generador.addComment("ACCESO ARRAY")

            t0 = generador.addTemp()
            t1 = generador.addTemp()
            generador.getStack(t0, posicion)
            generador.getHeap(t1, t0)

            t2 = generador.addTemp()
            generador.addAsignacion(t2, "0") # contador
            t3 = generador.addTemp()
            generador.addExpresion(t3, t1, "1", "-") # length -1
            if sim.tipo != TIPO_DATO.CADENA:
                generador.addExpresion(t0, t0, "1", "+")
            t4 = generador.addTemp()
            L1 = generador.newLabel()
            L2 = generador.newLabel()
            L3 = generador.newLabel()
            L4 = generador.newLabel()
            L5 = generador.newLabel()

            generador.addIf(acceso, t3, ">", L4)
            generador.addGoto(L1)
            
            generador.putLabel(L1)
            generador.addIndent()
            generador.addIf(t2, t3, "<=", L2)
            generador.addIndent()
            generador.addGoto(L4)

            generador.putLabel(L2)
            generador.addIndent()
            generador.addIf(t2, tempAcceso, "==", L3)
            generador.addIndent()
            generador.addExpresion(t2, t2, "1", "+")
            generador.addExpresion(t0, t0, "1", "+")
            generador.addGoto(L1)

            generador.putLabel(L3)
            generador.addIndent()
            
            generador.getHeap(t4, t0)
            generador.addGoto(L5)
            

            generador.putLabel(L4)
            generador.addIndent()
            generador.addComment("ERROR NO SE PUDO ACCESAR AL ARRAY")
            generador.fPrintError()
            generador.putLabel(L5)
            generador.addComment("Fin del acceso del array")

            if sim.tipo == TIPO_DATO.CADENA:
                return Retorno2(t4, TIPO_DATO.CHAR, True)
            return Retorno2(t4, TIPO_DATO.NUMERO, True)
        else:
            print("ACCESO MULSDAFASDFSATIPLE")
            tempAcceso = generador.addTemp()
            acceso = self.accesos[0].genC3D(entorno, helper).valor
            generador.addAsignacion(tempAcceso, acceso)
            #C3D
            generador.addComment("ACCESO ARRAY")

            t0 = generador.addTemp()
            t1 = generador.addTemp()
            generador.getStack(t0, posicion)
            generador.getHeap(t1, t0)

            generador.addPrint('f', t1)
            
            if sim.tipo == TIPO_DATO.CADENA:
                return Retorno2(t4, TIPO_DATO.CHAR, True)
            return Retorno2(t4, TIPO_DATO.NUMERO, True)
            pass
        
        '''
                ACCESO:

                1. obtener el simbolo del array
                2. obtener el simbolo.posicion para saber donde esta el array en el stack
                3. comienza el algoritmo

                Algoritmo:
                t0 = stack[int(posicion)] # obtenemos la posicion del arreglo
                t1 = heap[int(t0)] # obtenemos la posicion donde inicia el arreglo y el length
                t2 = 0 # inicializar el contador
                t3 = t1 - 1 # length - 1
                L1:
                if t2 != t3 goto L2;
                goto L4

                L2:
                if t2 == no_acceso goto L3;
                t2 = t2 + 1
                t0 = t0 + 1
                goto L1

                L3:
                t4 = heap[t0]
                #RETURN TEMPORAL

                L4:
                #ERROR


                ////////////////////////////////////////
                Para el acceso multiple:
                1. obtener el simbolo del array
                2. obtener el simbolo.posicion para saber donde esta el array en el stack
                3. comienza el algoritmo

                Algoritmo:
                t0 = stack[int(posicion)] # obtenemos la posicion del arreglo

                t1 = heap[int(t0)] # obtenemos la posicion donde inicia el arreglo y el length del array principal
                si 
            '''

    def genArbol(self) -> Nodo:
        nodo = Nodo("=[]")
        nodo.agregarHijo(Nodo(str(self.id)))
        listaAcc = []
        for a in self.accesos:
            listaAcc.append(a.genArbol())
        for a in listaAcc:
            nodo.agregarHijo(a)
        return nodo
