from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores
from AST.Simbolos.Retorno2 import Retorno2


class DeclaracionArray(Instruccion):
    #let id: number[][] = 
    def __init__(self, id, tipo, expresion, linea, columna):
        self.id = id
        self.tipo = tipo
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        self.find = True
        self.multiDimensional = False
        super().__init__()

    
    def ejecutar(self, entorno, helper):
        print("Declaracion Array")
        exp = self.expresion.ejecutar(entorno, helper) #obtiene objeto Array

        
        if isinstance(self.tipo, TIPO_DATO):
            bandera = True
            if self.tipo != TIPO_DATO.ANY and self.tipo != TIPO_DATO.ARRAY:
                
                bandera = self.Verificar_Tipos_array(exp.valor, self.tipo, bandera, entorno)
                if bandera == None:
                    bandera = True
                if not bandera:
                    #error semantico
                    s = SingletonErrores.getInstance()
                    err = Error(self.linea, self.columna, "Error Semántico", "El tipo de dato del array no coincide con el tipo de dato declarado")
                    helper.setConsola("[ERROR] El tipo de dato del array no coincide con el tipo de dato declarado en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                    s.addError(err)
            #crear el simbolo
            simbolo = Simbolo()
            simbolo.nombre = self.id
            if self.tipo == TIPO_DATO.NUMERO:
                simbolo.tipo = TIPO_DATO.ARRAY_NUMBER
            elif self.tipo == TIPO_DATO.CADENA:
                simbolo.tipo = TIPO_DATO.ARRAY_STRING

            elif self.tipo == TIPO_DATO.BOOLEANO:
                simbolo.tipo = TIPO_DATO.ARRAY_BOOLEAN
            elif self.tipo == TIPO_DATO.ANY or self.tipo == TIPO_DATO.ARRAY:
                simbolo.tipo = TIPO_DATO.ARRAY
            else:
                print("entro al else")
            simbolo.valor = exp.valor
            simbolo.linea = self.linea
            simbolo.columna = self.columna

            #agregar el simbolo al entorno
            verifExistencia = entorno.BuscarSimboloLocal(simbolo.nombre)
            if not verifExistencia:
                verifExistencia = entorno.BuscarInterfaceDeclaradaLocal(simbolo.nombre)
                if not verifExistencia:
                    verifExistencia = entorno.BuscarInterfaceLocal(simbolo.nombre)
            if verifExistencia:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.linea, self.columna, "Error Semántico", "La variable " + simbolo.nombre + " ya existe en el entorno actual")
                s.addError(err)
                helper.setConsola("[ERROR] La variable " + simbolo.nombre + " ya existe en el entorno actual en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                return
            entorno.AgregarSimbolo(self.id,simbolo)
        else:
            tipo_interface = entorno.ExisteInterface(self.tipo)
            if not tipo_interface:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.linea, self.columna, "Error Semántico", "La interface " + self.id_interface + " no existe en el entorno actual")
                s.addError(err)
                helper.setConsola("[ERROR] La interface " + self.id_interface + " no existe en el entorno actual en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                return
            
            #crear el simbolo
            bandera = True
            if self.tipo != TIPO_DATO.ANY and self.tipo != TIPO_DATO.ARRAY:
                bandera = self.Verificar_Tipos_array(exp.valor, self.tipo, bandera, entorno)
                if bandera == None:
                    bandera = True
                if not bandera:
                    #error semantico
                    s = SingletonErrores.getInstance()
                    err = Error(self.linea, self.columna, "Error Semántico", "El tipo de dato del array no coincide con el tipo de dato declarado se esperaba " + self.tipo +  " y se obtuvo " + str(obtTipoDato(exp.valor)) )
                    helper.setConsola("[ERROR] El tipo de dato del array no coincide con el tipo de dato declarado en la línea "+ str(self.linea) +" y columna " + str(self.columna) + " se esperaba " + self.tipo +  " y se obtuvo " + str(obtTipoDato(exp.valor)))
                    s.addError(err)
                    return
                
            simbolo = Simbolo()
            simbolo.nombre = self.id
            simbolo.tipo = TIPO_DATO.ARRAY_INTERFACE
            simbolo.valor = exp.valor
            simbolo.linea = self.linea
            simbolo.columna = self.columna
            verifExistencia = entorno.ExisteSimbolo(simbolo.nombre)
            if verifExistencia:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.linea, self.columna, "Error Semántico", "La variable " + simbolo.nombre + " ya existe en el entorno actual")
                s.addError(err)
                helper.setConsola("[ERROR] La variable " + simbolo.nombre + " ya existe en el entorno actual en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                return

            entorno.AgregarSimbolo(self.id,simbolo)

    def Verificar_Tipos_array(self,arr, tipo, bandera, entorno):
        if isinstance(arr,list):
            for a in arr:
                if a.tipo == TIPO_DATO.ARRAY:
                    bandera = self.Verificar_Tipos_array(a.valor, tipo, bandera,entorno)
                    if bandera == False:
                        return False
                else:
                    bandera = self.Verificar_Tipos_array(a, tipo, bandera, entorno)
                    if bandera == False:
                        return False
        else:
            if arr.tipo != tipo:
                if arr.tipo == TIPO_DATO.INTERFACE:
                    return entorno.ExisteInterface(tipo)
                elif tipo != TIPO_DATO.ANY:
                    bandera = False
                    return bandera
                else:
                    bandera = True
            else:
                bandera = True

    def genArbol(self) -> Nodo:
        nodo = Nodo("DECLARACION ARRAY")
        nodo_id = Nodo(str(self.id))
        if isinstance(self.tipo, TIPO_DATO):
            nodo_id.agregarHijo(Nodo(obtTipoDato(self.tipo)))
        else:
            nodo_id.agregarHijo(Nodo(self.tipo))
        nodo_id.agregarHijo(self.expresion.genArbol())
        nodo.agregarHijo(nodo_id)
        return nodo
    
    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()
        generador.addComment("Declaracion de un array")
        if self.expresion != None:

            tipoGuardado = ''
            if self.tipo == TIPO_DATO.NUMERO:
                tipoGuardado = TIPO_DATO.ARRAY_NUMBER
            elif self.tipo == TIPO_DATO.CADENA:
                tipoGuardado = TIPO_DATO.ARRAY_STRING

            elif self.tipo == TIPO_DATO.BOOLEANO:
                tipoGuardado = TIPO_DATO.ARRAY_BOOLEAN
            elif self.tipo == TIPO_DATO.ANY or self.tipo == TIPO_DATO.ARRAY:
                tipoGuardado = TIPO_DATO.ARRAY

            
            exp = self.expresion.genC3D(entorno, helper)
            obt = self.obtener_dimensiones(exp.valor) #dimensiones del array
            if len(obt) == 1:
                generador.addComment("Compilación del array")
                temporal0 = generador.addTemp()
                temporal1 = generador.addTemp()

                generador.addAsignacion(temporal0, "H")
                generador.addExpresion(temporal1, temporal0, '1', '+')
                generador.setHeap('H', len(exp.valor))

                apuntador = str(len(exp.valor)+1)
                generador.addExpresion('H', 'H', apuntador, '+')
                
                length = 0
                
                bandera = True
                print("SOY EL TIPO", self.tipo)
                if self.tipo != TIPO_DATO.ANY and self.tipo != TIPO_DATO.ARRAY:
                    bandera = self.Verificar_Tipos_array(exp.valor, self.tipo, bandera, entorno)
                    if bandera == None:
                        bandera = True
                    if not bandera:
                        generador.addComment("Error, los tipos de datos no coinciden")
                        return
                    
                for val in exp.valor:
                    generador.setHeap(temporal1, val.valor)
                    generador.addExpresion(temporal1, temporal1, '1', '+')
                    length += 1
                    
                s_c3d = entorno.setEntorno(self.id, tipoGuardado, True)
                s_c3d.length = len(exp.valor)
                s_c3d.dimensiones = obt
                posTemp = s_c3d.posicion
                if not s_c3d.globalVar:
                    posTemp = generador.addTemp()
                    generador.addExpresion(posTemp, "P", s_c3d.posicion, "+")
                generador.setStack(posTemp, temporal0)
                generador.addComment("Fin de la compilación del array")
            else:
                generador.addComment("Compilación del array multidimensional")
                temp0 = generador.addTemp()
                temp1 = generador.addTemp()

                generador.addAsignacion(temp0, "H")
                generador.addExpresion(temp1, temp0, '1', '+')
                contador = 0
                copiaObt = self.obtener_dimensiones(exp.valor)
                print("Soy copia", copiaObt)
                self.dec_multidim_C3D(exp.valor, obt, temp0, temp1, generador, contador)
                s_c3d = entorno.setEntorno(self.id, tipoGuardado, True)
                
                s_c3d.length = len(exp.valor)
                s_c3d.dimensiones = copiaObt
                print("Soy el id", s_c3d.dimensiones)
                print("Soy copia", copiaObt)
                posTemp = s_c3d.posicion
                if not s_c3d.globalVar:
                    posTemp = generador.addTemp()
                    generador.addExpresion(posTemp, "P", s_c3d.posicion, "+")
                generador.setStack(posTemp, temp0)
                

    def obtener_dimensiones(self, lista):
        if isinstance(lista, list):
            dimensiones_sublista = self.obtener_dimensiones(lista[0])
            return [len(lista)] + dimensiones_sublista
        elif isinstance(lista, Retorno2):
            return self.obtener_dimensiones(lista.valor)
        else:
            return []
    
    def dec_multidim_C3D(self, lista, dims, temp0, temp1, generador, contador):
        
        if contador == 0:
            generador.setHeap('H', dims[0]) #se guarda la dimensión del primer array en la primera posición
            apuntador = str(dims[0]+1)
            generador.addExpresion('H', 'H', apuntador, '+')
            dims.pop(0)
            contador += 1
            self.dec_multidim_C3D(lista, dims, temp0, temp1, generador, contador)
            return
        if len(dims) >= 2: #n-dimensional, donde n es mayor o igual que 2
            temp1_2 = generador.addTemp()
            generador.addAsignacion(temp1_2, temp1)
            tempComparacion = generador.addTemp()
            tempContador = generador.addTemp()
            tempContador2 = generador.addTemp()
            tempCopiat1 = generador.addTemp()
            tempCopiat2 = generador.addTemp()
            tempNewApuntador = generador.addTemp()
            tempMult = generador.addTemp()
            tempSum = generador.addTemp()


            tempVals = generador.addTemp()

            generador.addAsignacion(tempCopiat1, temp1)
            generador.addAsignacion(tempContador, '0')
            generador.addExpresion(tempComparacion, 'H', '1', '-')

            generador.addExpresion(tempVals, tempVals, 'H', '+')
            generador.addAsignacion(tempCopiat2, tempVals)
            # generador.addExpresion(tempCopiat2, tempCopiat2, '1', '+')
            
            Labelinicio = generador.newLabel()
            Labelfin = generador.newLabel()



            generador.putLabel(Labelinicio)
            generador.addIf(tempContador, tempComparacion, '==', Labelfin)
            tempTest = generador.addTemp()
            generador.addExpresion(tempTest, temp1, tempComparacion, '+')


            generador.setHeap(tempTest, dims[0])

            generador.setHeap(tempCopiat1, tempTest)
            generador.addExpresion(tempCopiat1, tempCopiat1, '1', '+')
            generador.addExpresion(tempContador, tempContador, '1', '+')
            generador.addExpresion(temp1, temp1, dims[0]+1, '+')
            generador.addAsignacion(tempContador2, '0')
                
            '''
            generador.putLabel(labelFor)
            generador.addIf(tempContador2, tempComparacion, '==', labelSalidaFor)
            generador.addExpresion(tempContador2, tempContador2, '1', '+')

            generador.addExpresion(tempNewApuntador, temp1, '1', '+')
            generador.addExpresion(tempMult, dims[0], tempComparacion, '*')
            generador.addExpresion(tempSum, tempMult, dims[0], '+')
            generador.addExpresion(tempNewApuntador, tempNewApuntador, tempSum, '+')

            generador.setHeap(tempNewApuntador, dims[1])

            generador.addGoto(labelFor)

            generador.putLabel(labelSalidaFor)
            '''
            

            '''
            generador.addExpresion(tempNewApuntador, temp1, '1', '+')
            generador.addExpresion(tempMult, dims[0], tempComparacion, '*')
            generador.addExpresion(tempSum, tempMult, dims[0], '+')
            generador.addExpresion(tempNewApuntador, tempNewApuntador, tempSum, '+')

            generador.setHeap(tempNewApuntador, dims[1])
            '''
            
            generador.addGoto(Labelinicio)
            
            generador.putLabel(Labelfin)
            contador3 = generador.addTemp()
            labelFor2 = generador.newLabel()
            labelSalidaFor2 = generador.newLabel()
            
            generador.addComment("***************************************")
            generador.putLabel(labelFor2)
            generador.addComment("***************************************")
            generador.addExpresion(tempCopiat2, tempCopiat2, 1, '+')
            generador.addAsignacion(contador3, '0')
            generador.addIf(tempContador2, dims[0], '==', labelSalidaFor2)
            labelFor = generador.newLabel()
            labelSalidaFor = generador.newLabel()

            generador.putLabel(labelFor)
            generador.addIf(contador3, tempComparacion, '==', labelSalidaFor)
            
            print(contador3)
            generador.addPrint('f', tempCopiat2)
            generador.addExpresion(tempCopiat2, tempCopiat2, tempComparacion, '+')
            generador.addExpresion(contador3, contador3, '1', '+')
            generador.addGoto(labelFor)
            generador.putLabel(labelSalidaFor)

            generador.addExpresion(tempCopiat2, tempVals, '1', '+')
            generador.addExpresion(tempContador2, tempContador2, '1', '+')
            generador.addGoto(labelFor2)
            generador.addComment("***************************************")
            generador.putLabel(labelSalidaFor2)
            generador.addComment("***************************************")
            #NUEVO LOOP
            #for index in range(0, dims[0]):
                


            '''
            for index in range(0, len(dims)):
                index = index + 1
                generador.addExpresion(tempNewApuntador, temp1, '1', '+')
                generador.addExpresion(tempMult, dims[0], tempComparacion, '*')
                generador.addExpresion(tempSum, tempMult, dims[0], '+')
                generador.addExpresion(tempNewApuntador, tempNewApuntador, tempSum, '+')
                if index % 2 == 0:
                    generador.addExpresion(tempNewApuntador, tempNewApuntador, index, '+')
                generador.addPrint('f', tempNewApuntador)
                generador.setHeap(tempNewApuntador, dims[1])
            '''


            '''
            tempComparacion_2 = generador.addTemp()
            tempContador_2 = generador.addTemp()
            tempCopiat1_2 = generador.addTemp()

            tempVals_2 = generador.addTemp()

            generador.addAsignacion(tempCopiat1_2, temp1_2)

            generador.addAsignacion(tempContador_2, '0')
            generador.addExpresion(tempComparacion_2, 'H', '1', '-')

            generador.addExpresion(tempVals_2, tempVals_2, 'H', '+')

            Labelinicio_2 = generador.newLabel()
            Labelfin_2 = generador.newLabel()

            generador.putLabel(Labelinicio_2)
            generador.addIf(tempContador_2, tempComparacion_2, '==', Labelfin_2)
            tempTest_2 = generador.addTemp()
            generador.addExpresion(tempTest_2, temp1_2, tempComparacion_2, '+')


            #generador.setHeap(tempTest_2, dims[0])

            #generador.setHeap(tempCopiat1_2, tempTest_2)
            generador.addExpresion(tempCopiat1_2, tempCopiat1_2, '1', '+')
            generador.addExpresion(tempContador_2, tempContador_2, '1', '+')
            generador.addExpresion(temp1_2, temp1_2, dims[0]+1, '+')
            generador.addPrint('f', temp1_2)

            generador.addGoto(Labelinicio_2)
            generador.putLabel(Labelfin_2)
            
            '''





            #actualizando H:.
            #generador.addExpresion('H', 'H', temp1, '+')
            #generador.addExpresion('H', 'H', '1', '+')
            dims.pop(0)


            #for val in lista:
            #    self.dec_multidim_C3D(val.valor, dims, temp0, temp1, generador, contador)
            #    val.valor.pop(0)
            #self.dec_multidim_C3D(lista, dims, temp0, temp1, generador, contador)
            '''
            temp2 = generador.addTemp()
            tempComparacion = generador.addTemp()

            generador.addExpresion(tempComparacion, 'H', '1', '-')

            tempContador = generador.addTemp()
            generador.addAsignacion(tempContador, '0')

            labelInic = generador.newLabel()
            labelFin = generador.newLabel()

            generador.putLabel(labelInic)
            generador.addIf(tempContador, tempComparacion, '==', labelFin)
            generador.addExpresion(tempContador, tempContador, '1', '+')
            generador.putLabel(labelFin)
            '''
            #self.dec_multidim_C3D(lista, dims, temp0, temp1, generador, contador)
            generador.visualizarHeap()
            pass
            
        else: #es bidimensional
            print("ESTA ES LA SEGUNDA LISTA QUE QUIERO REVISAR")
            print(lista)
            temp2 = generador.addTemp()
            tempComparacion = generador.addTemp()
            tempContador = generador.addTemp()
            tempCopiat1 = generador.addTemp()
            tempVals = generador.addTemp()

            generador.addAsignacion(tempCopiat1, temp1)
            generador.addAsignacion(tempContador, '0')
            generador.addExpresion(tempComparacion, 'H', '1', '-')

            generador.addExpresion(tempVals, tempVals, 'H', '+')

            Labelinicio = generador.newLabel()
            Labelfin = generador.newLabel()

            generador.putLabel(Labelinicio)
            generador.addIf(tempContador, tempComparacion, '==', Labelfin)
            tempTest = generador.addTemp()
            generador.addExpresion(tempTest, temp1, tempComparacion, '+')


            generador.setHeap(tempTest, dims[0])

            generador.setHeap(tempCopiat1, tempTest)
            generador.addExpresion(tempCopiat1, tempCopiat1, '1', '+')
            generador.addExpresion(tempContador, tempContador, '1', '+')
            generador.addExpresion(temp1, temp1, dims[0]+1, '+')
            generador.addGoto(Labelinicio)
            
            generador.putLabel(Labelfin)
    
            #LLENAR ACÁ
            self.llenarHeap(tempVals, generador, lista)

            generador.addComment("Compilación del array")
            #generador.visualizarHeap()
            # falta guardar la nueva posición del heap (???)
            return

    def llenarHeap(self, apuntador, generador, lista):
        for x in lista:
            generador.addExpresion(apuntador, apuntador, '1', '+')
            if isinstance(x, list):
                self.llenarHeap(apuntador, generador, x)
            else:
                for a in x.valor:
                    generador.setHeap(apuntador, a.valor)
                    generador.addExpresion(apuntador, apuntador, '1', '+')