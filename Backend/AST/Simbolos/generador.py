class Generador:
    generador = None
    def __init__(self):
        self.T = 0 #contador de temporales
        self.L = 0 #contador de etiquetas

        # ---------------------------------
        self.codigo = ""
        self.funcs = ''
        self.natives = ''
        self.inFunc = False #¿Estoy en una funcion?
        self.inNative = False #¿Estoy en una funcion nativa?
        #-------------------------------------


        self.temporales = [] #lista de temporales

        # ? Nativas:
        self.printString = False
        self.compareString = False
        self.length = False
        self.concatString = False
        self.toNumber = False
        self.toString = False
        self.typeOf = False
        self.uppercase = False
        self.lowercase = False
        self.toFixed = False
        self.strNumber = False
        self.strBoolean = False
        self.strString = False
        self.printArray = False
        self.importaciones = [] #lista de importaciones
        self.importaciones2 = ['fmt', 'math']

    def getInstance(self):
        if Generador.generador == None:
            Generador.generador = Generador()
        return Generador.generador

    def clean(self): #limpia los valores
        self.T = 0
        self.L = 0
        self.codigo = ""
        self.temporales = []
        self.importaciones = []
        self.importaciones2 = ['fmt', 'math']

        # ? Limpieza de Nativas:
        self.printString = False
        self.compareString = False
        self.length = False
        self.concatString = False
        self.toNumber = False
        self.toString = False
        self.typeOf = False
        self.uppercase = False
        self.lowercase = False
        self.toFixed = False
        self.strNumber = False
        self.strBoolean = False
        self.strString = False
        self.printArray = False
        Generador.generador = Generador()

    #*
    #* IMPORTS
    #*

    def setImport(self, libreria):
        #si no esta en la lista de importaciones, la agrega, sino no hace nada
        if libreria not in self.importaciones:
            self.importaciones.append(libreria)
        else:
            return
        
        code = f'import (\n\t"{libreria}"\n)\n'

    # ? ------------------------------------------------------------

    def obtEncabezado(self):
        code = '''
/*----------- HEADER -----------*/
package main;\n \n'''
        if len(self.importaciones) > 0:
            code += 'import (\n'
            for i in range(len(self.importaciones)):
                code += '\t\"' + self.importaciones[i] + '\"\n'
            code += ')\n\n'
        if len(self.temporales) > 0:
            code += 'var '
            for temporal in self.temporales:
                code += temporal + ', '
            code = code[:-2]
            code += ' float64; \n'
        code+= '''
var P, H float64;
var stack[30101999] float64;
var heap[30101999] float64;
'''
        return code
    
    def obtCodigo(self):   
        return f'{self.obtEncabezado()}{self.natives}{self.funcs}\nfunc main() {{\n{self.codigo}}}' 
    

    def addCodigo(self, codigo, tab='\t'):
        if self.inNative:
            if self.natives == '':
                self.natives = self.natives + "/* --- NATIVAS --- */\n"
            self.natives += codigo
        elif self.inFunc:
            if self.funcs == '':
                self.funcs = self.funcs + "/* --- FUNCIONES --- */\n"
            self.funcs += tab + codigo
        else:
            self.codigo += tab + codigo



    def addComment(self, comment):
        self.addCodigo(f'/* {comment}*/\n')
    
    def espacio(self):
        self.addCodigo('\n')

    # ? ------------------------------------------------------------


    #*
    #* TEMPORALES
    #*

    def addTemp(self): #agrega un temporal a la lista de temporales
        temp = f't{self.T}'
        self.T += 1
        self.temporales.append(temp)
        return temp
    
    #*
    #* MANEJO DEL STACK
    #*

    def setStack(self, pos, valor): #agrega un valor al stack
        self.addCodigo(f'stack[int({pos})]= {valor};\n')

    def getStack(self, place, pos): #obtiene un valor del stack
        self.addCodigo(f'{place} = stack[int({pos})];\n')


    # * 
    # * MANEJO DEL HEAP
    # *

    def setHeap(self, pos, valor): #agrega un valor al heap
        self.addCodigo(f'heap[int({pos})]= {valor};\n')
    
    def getHeap(self, place, pos): #obtiene un valor del heap
        #print("ORDEN2")
        self.addCodigo(f'{place} = heap[int({pos})];\n')

    def nextHeap(self): #obtiene la siguiente posicion del heap
        #print("ORDEN1")
        self.addCodigo(f'H = H + 1;\n')

    #* 
    #* MANEJO DE LABELS
    #*

    def newLabel(self): #crea una nueva etiqueta
        label = f'L{self.L}'
        self.L += 1
        return label
    
    def putLabel(self, label): #agrega una etiqueta
        #print("LABEEEEEEEEEL")
        self.addCodigo(f'{label}:\n')

    def addIndent(self):
        self.addCodigo("\t")

    #*
    #* GOTO
    #*

    def addGoto(self, label): #agrega un goto
        self.addCodigo(f'goto {label};\n')

    #*
    #* IF
    #*
    def addIf(self, left, right, operador, label): #agrega un if
        self.addCodigo(f'if {left} {operador} {right} {{goto {label};}}\n')


    # ! --------------------------------------------------!
    # !                   EXPRESIONES                     !
    # ! --------------------------------------------------!

    def addExpresion(self, res, left, right, operador):
        self.addCodigo(f'{res} = {left} {operador} {right};\n')

    def addAsignacion(self, res, left):
        self.addCodigo(f'{res} = {left};\n')


    # ! --------------------------------------------------!
    # !                   ENTORNO                         !
    # ! --------------------------------------------------!

    def crearEntorno(self, tamaño):

        self.addCodigo('/*----------- NUEVO ENTORNO -----------*/\n')
        self.addCodigo(f'P = P + {tamaño};\n')

    #& LLAMADA A FUNCION
    def callFun(self, id):
        print(f'{id}();\n')
        self.addCodigo(f'{id}();\n')


    def retornarEntorno(self, tamaño):
        self.addCodigo(f'P = P - {tamaño};\n')
        self.addCodigo('/*----------- RETORNA ENTORNO -----------*/\n\n')


    # ! --------------------------------------------------!
    # !                   INSTRUCCIONES                   !
    # ! --------------------------------------------------!

    #*
    #* PRINT
    #*

    def fotmatPrint(self,temp, presicion, num):
        self.setImport('math')
        self.addCodigo(f'{temp} = math.Round({num})/({presicion});\n')

    def addPrint(self, type, valor):
        self.setImport('fmt')
        self.addCodigo(f'fmt.Printf("%{type}", float64({valor}));\n')

    #para imprimir el string
    def addPrintString(self, type, valor):
        self.setImport('fmt')
        self.addCodigo(f'fmt.Printf("%{type}", int({valor}));\n')

    def addPrintChar(self, valor):
        self.setImport('fmt')
        self.addCodigo(f'fmt.Printf("%c", int({valor}));\n')

    def printTrue(self):
        self.setImport('fmt')
        self.addIndent()
        self.addPrintString('c', '116')
        self.addIndent()
        self.addPrintString('c', '114')
        self.addIndent()
        self.addPrintString('c', '117')
        self.addIndent()
        self.addPrintString('c', '101')
        self.addIndent()


    def printFalse(self):
        self.setImport('fmt')
        self.addIndent()
        self.addPrintString('c', '102')
        self.addIndent()
        self.addPrintString('c', '97')
        self.addIndent()
        self.addPrintString('c', '108')
        self.addIndent()
        self.addPrintString('c', '115')
        self.addIndent()
        self.addPrintString('c', '101')
        self.addIndent()

    def addPotencia(self, res, left, right):
        self.setImport('math')
        self.addCodigo(f'{res} = math.Pow({left},{right});\n')

    def addModulo(self, res, left, right):
        self.setImport('math')
        self.addCodigo(f'{res} = math.Mod({left},{right});\n')

    #! --------------------------------------------------!
    #!                    FUNCIONES                        !
    #! --------------------------------------------------!

    def addBeginFunc(self, id):
        print("ENTRO A ADD BEGIN FUNC CON ID:", id)
        if not self.inNative:
            self.inFunc = True
        
        self.addCodigo(f'/*----------- FUNCION {id} -----------*/\n')
        self.addCodigo(f'func {id}() {{\n')
        print("INICIO DE FUNCION")
        print("NOMBRE DE LA FUNCIÓN A AGREGAR: ", id)

    def addEndFunc(self):
        self.addCodigo('return;\n}\n')
        if not self.inNative:
            self.inFunc = False

    #! --------------------------------------------------!
    #!                    NATIVAS                        !
    #! --------------------------------------------------!
    
    # ? typeof()
    def fTypeOf(self):
        if self.typeOf:
            return
        self.inNative = True
        self.typeOf = True
        self.addBeginFunc('typeOf')

        

        self.addEndFunc()
        self.inNative = False


    # ? ToFixed()
    def fToFixed(self):
        if self.toFixed:
            return
        self.inNative = True
        self.toFixed = True
        self.addBeginFunc('toFixed')
        self.addEndFunc()
        self.inNative = False

    # ? Number()
    def fNumber(self):
        if self.toNumber:
            return
        self.toNumber = True
        self.inNative = True
        self.addBeginFunc('fNumber')
        tempReinicio = self.addTemp()
        print("XD: ", tempReinicio)
        self.addAsignacion(tempReinicio, 'H')
        temp = self.addTemp()
        tempCont = self.addTemp()
        self.addAsignacion(tempCont, '0')
        labelInic = self.newLabel()
        labelFin = self.newLabel()
        self.putLabel(labelInic)
        self.getHeap(temp,'H')
        self.addIf(temp, "-1", "==", labelFin)
        self.addExpresion(tempCont, tempCont,'1',  "+")
        self.addExpresion('H', 'H','1',  "+")
        self.addGoto(labelInic)
        self.putLabel(labelFin)
        self.addAsignacion('H', tempReinicio)
        tempExp = self.addTemp()
        tempOp = self.addTemp()

        labelCont = self.newLabel()
        labelContFin = self.newLabel()
        tempRes = self.addTemp() #resultado de la operacion
        tempTest = self.addTemp()
        tempRes2 = self.addTemp()
        self.addAsignacion(tempTest, '0')
        self.putLabel(labelCont)
        self.getHeap(tempTest, 'H')
        self.addIf(tempTest, '-1', '==', labelContFin)
        
        self.addExpresion(tempOp, tempTest, '48', '-')
        
        self.addIf(tempOp, '9', '>', labelContFin)
        self.addIf(tempOp, '0', '<', labelContFin)

        self.addExpresion(tempCont, tempCont, '1', '-')
        self.addPotencia(tempExp, '10', tempCont)
        #self.addExpresion(tempExp, '10', tempReal, '^')
        self.addExpresion(tempRes, tempOp, tempExp, '*')
        self.addExpresion(tempRes2, tempRes2, tempRes, '+')

        self.addExpresion('H', 'H', '1', '+')
        self.addGoto(labelCont)
        self.putLabel(labelContFin)

        self.setStack('P', tempRes2)
        self.addCodigo('\n') 
        self.addEndFunc()
        self.inNative = False

    # ? Length
    def flength(self):
        if self.length:
            return
        self.length = True
        self.inNative = True
        self.addBeginFunc('length')
        
        temp = self.addTemp()
        tempCont = self.addTemp()
        self.addAsignacion(tempCont, '0')
        labelInic = self.newLabel()
        labelFin = self.newLabel()
        self.putLabel(labelInic)
        self.getHeap(temp,'H')
        self.addIf(temp, "-1", "==", labelFin)
        self.addExpresion(tempCont, tempCont,'1',  "+")
        self.addExpresion('H', 'H','1',  "+")
        self.addGoto(labelInic)
        self.putLabel(labelFin)
        self.setStack('P', tempCont)
        self.addCodigo('\n') 
        self.addEndFunc()
        self.inNative = False

    # ? Print String

    def fPrintString(self):
        self.setImport('fmt')
        if(self.printString): #se revisa si ya se ha creado la funcion, esto para solo agregarla una vez.
            return 
        self.printString = True #se marca que ya se ha creado la funcion
        self.inNative = True #se marca que se esta en una funcion nativa

        self.addBeginFunc('printString') # funcion printString (){
        print(self.inFunc)
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        compareLbl = self.newLabel()
        # Temporal puntero a Stack
        tempP = self.addTemp() # t1
        # Temporal puntero a Heap
        tempH = self.addTemp() # t2
        self.addIndent()
        self.addExpresion(tempP, 'P', '1', '+') # t1 = P + 1
        self.addIndent()
        self.getStack(tempH, tempP) # t2 = stack[t1]
        # Temporal para comparar
        tempC = self.addTemp() # t3
        self.putLabel(compareLbl) # L1: 
        self.addIndent()
        self.getHeap(tempC, tempH) # t3 = heap[t2]
        self.addIndent()
        self.addIf(tempC, '-1', '==', returnLbl) # if t3 == -1 goto L0
        self.addIndent()
        self.addPrintString('c', tempC) # printf("%c", t3)
        self.addIndent()
        self.addExpresion(tempH, tempH, '1', '+') # t2 = t2 + 1
        self.addIndent()
        self.addGoto(compareLbl) # goto L1
        self.putLabel(returnLbl) # L0:
        self.addCodigo('\n') # }
        self.addEndFunc() # }
        self.inNative = False

    # ?  fCompareString

    def fcompareString(self):
        if self.compareString:
            return
        self.compareString = True
        self.inNative = True

        self.addBeginFunc('compareString')

        returnLbl = self.newLabel()

        t2 = self.addTemp()
        print('compareString:', t2)
        self.addExpresion(t2, 'P', '1', '+')
        t3 = self.addTemp()
        self.getStack(t3,t2)
        self.addExpresion(t2, t2, '1', '+')
        t4 = self.addTemp()
        self.getStack(t4,t2)

        L1 = self.newLabel()
        L2 = self.newLabel()
        L3 = self.newLabel()
        self.putLabel(L1)
        t5 = self.addTemp()
        self.addIndent()
        self.getHeap(t5, t3)

        t6 = self.addTemp()
        self.addIndent()
        self.getHeap(t6, t4)

        self.addIndent()
        self.addIf(t5, t6, '!=', L3)
        self.addIndent()
        self.addIf(t5,'-1', '==', L2)

        self.addIndent()
        self.addExpresion(t3, t3, '1', '+')
        self.addIndent()
        self.addExpresion(t4, t4, '1', '+')
        self.addIndent()
        self.addGoto(L1)

        self.putLabel(L2)
        self.addIndent()
        self.setStack('P', '1')
        self.addIndent()
        self.addGoto(returnLbl)
        self.putLabel(L3)
        self.addIndent()
        self.setStack('P', '0')
        self.putLabel(returnLbl)
        self.addEndFunc()
        self.inNative = False

    # ? Concatenar String

    def fConcatString(self):
        if self.concatString:
            return
        self.concatString = True
        self.inNative = True
        self.addComment('Funcion concatenar String')
        self.addBeginFunc('ConcatString')

        Lblreturn = self.newLabel()
        L1 = self.newLabel()
        L2 = self.newLabel()
        L3 = self.newLabel()
        t0 = self.addTemp()
        t1 = self.addTemp()
        t2 = self.addTemp()
        t3 = self.addTemp()
        t4 = self.addTemp()

        self.addAsignacion(t0, 'H')
        self.addExpresion(t1, 'P', '1', '+')
        self.getStack(t2, t1)
        self.addExpresion(t3, 'P', '2', '+')
        
        self.putLabel(L1)
        self.addIndent()

        self.getHeap(t4, t2)
        self.addIndent()
        self.addIf(t4, '-1', '==', L2)
        self.addIndent()
        self.setHeap('H', t4)
        self.addIndent()
        self.addExpresion('H', 'H', '1', '+')
        self.addIndent()
        self.addExpresion(t2, t2, '1', '+')
        self.addIndent()
        self.addGoto(L1)

        self.putLabel(L2)
        self.addIndent()

        self.getStack(t2, t3)

        self.putLabel(L3)
        self.addIndent()

        self.getHeap(t4, t2)
        self.addIndent()
        self.addIf(t4, '-1', '==', Lblreturn)
        self.addIndent()
        self.setHeap('H', t4)
        self.addIndent()
        self.addExpresion('H', 'H', '1', '+')
        self.addIndent()
        self.addExpresion(t2, t2, '1', '+')
        self.addIndent()
        self.addGoto(L3)

        self.putLabel(Lblreturn)
        self.addIndent()

        self.setHeap('H', '-1')
        self.addIndent()
        self.addExpresion('H', 'H', '1', '+')
        self.addIndent()
        self.setStack('P', t0)
        self.addEndFunc()
        self.inNative = False

    # ? ftoString
    def ftoString(self):
        if self.toString:
            return
        self.toString = True
        self.inNative = True
        self.addComment('Funcion toString')
        self.addBeginFunc('toString')

        lblsalida = self.newLabel()

        L1 = self.newLabel()
        L2 = self.newLabel()
        t0 = self.addTemp()
        t1 = self.addTemp()
        t2 = self.addTemp()
        t3 = self.addTemp()
        t4 = self.addTemp()
        
        
        self.addAsignacion(t0, 'H')
        self.addExpresion(t1, 'P', '1', '+')
        self.getStack(t2, t1)

        self.putLabel(L1)
        self.addIndent()

        self.addIf(t2 ,0, '>', L2)
        self.addIndent()
        self.addGoto(lblsalida)

        self.putLabel(L2)
        self.addIndent()

        self.addExpresion(t3, t2, '10', '%')
        self.addIndent()
        self.setHeap('H', t3)
        self.addIndent()
        self.nextHeap()
        self.addIndent()
        self.addExpresion(t2, t2, '10', '/')
        self.addGoto(L1)
        # ! PENDIENTE....

    def ftoUpperCase(self):
        if self.uppercase:
            return
        self.uppercase = True
        self.inNative = True

        self.addComment('Funcion toUpperCase')
        self.addBeginFunc('toUpperCase')


        t0 = self.addTemp()
        t1 = self.addTemp()
        t2 = self.addTemp()

        self.addAsignacion(t0, 'H') # guarda la posicion del heap

        L1 = self.newLabel()
        L2 = self.newLabel()
        L3 = self.newLabel()
        L4 = self.newLabel()
        L5 = self.newLabel()
        L6 = self.newLabel()
        L7 = self.newLabel()

        #L1:
        self.putLabel(L1)
        self.addIndent()
        self.getHeap(t2, 'H') # guarda el valor del heap en th
        self.addIndent()
        self.addIf(t2, '-1', '!=', L2) # si es diferente de -1, continua
        self.addIndent()
        self.addGoto(L3) # si es -1, termina el ciclo

        #L2:
        self.putLabel(L2)
        self.addIndent()
        self.addIf(t2, 97, '>=', L4) # si es mayor o igual a 97, continua
        self.addIndent()
        self.addGoto(L5)

        #L4:
        self.putLabel(L4)
        self.addIndent()
        self.addIf(t2, 122, '<=', L6) # si es menor o igual a 122, continua
        self.addIndent()
        self.addGoto(L5)

        #L6:
        t3 = self.addTemp()
        self.putLabel(L6)
        self.addIndent()
        self.addExpresion(t3, t2, 32, '-')
        self.addIndent()
        self.setHeap('H', t3)
        self.addIndent()
        self.nextHeap()
        self.addIndent()
        self.addExpresion(t2, t2, 1, '+')
        self.addIndent()
        self.addGoto(L1)

        #L3
        self.putLabel(L3)
        self.addIndent()
        self.setHeap('H', '-1')
        self.addIndent()
        self.nextHeap()
        self.addIndent()

        self.setStack(t1, t0)
        self.addGoto(L7)

        #L5
        self.putLabel(L5)
        self.setHeap('H', t2)
        self.addIndent()
        self.nextHeap()
        self.addIndent()
        self.addExpresion(t2, t2, 1, '+')
        self.addIndent()
        self.addGoto(L1)

        #L7
        self.putLabel(L7)
        
        #fin funcion
        self.addEndFunc()
        self.inNative = False

    def ftoLowerCase(self):
        if self.lowercase:
            return
        self.lowercase = True
        self.inNative = True

        self.addComment('Funcion toLowerCase')
        self.addBeginFunc('toLowerCase')


        t0 = self.addTemp()
        t1 = self.addTemp()
        t2 = self.addTemp()

        self.addAsignacion(t0, 'H') # guarda la posicion del heap

        L1 = self.newLabel()
        L2 = self.newLabel()
        L3 = self.newLabel()
        L4 = self.newLabel()
        L5 = self.newLabel()
        L6 = self.newLabel()
        L7 = self.newLabel()

        #L1:
        self.putLabel(L1)
        self.addIndent()
        self.getHeap(t2, 'H') # guarda el valor del heap en th
        self.addIndent()
        self.addIf(t2, '-1', '!=', L2) # si es diferente de -1, continua
        self.addIndent()
        self.addGoto(L3) # si es -1, termina el ciclo

        #L2:
        self.putLabel(L2)
        self.addIndent()
        self.addIf(t2, 65, '>=', L4) # si es mayor o igual a 97, continua
        self.addIndent()
        self.addGoto(L5)

        #L4:
        self.putLabel(L4)
        self.addIndent()
        self.addIf(t2, 90, '<=', L6) # si es menor o igual a 122, continua
        self.addIndent()
        self.addGoto(L5)

        #L6:
        t3 = self.addTemp()
        self.putLabel(L6)
        self.addIndent()
        self.addExpresion(t3, t2, 32, '+')
        self.addIndent()
        self.setHeap('H', t3)
        self.addIndent()
        self.nextHeap()
        self.addIndent()
        self.addExpresion(t2, t2, 1, '+')
        self.addIndent()
        self.addGoto(L1)

        #L3
        self.putLabel(L3)
        self.addIndent()
        self.setHeap('H', '-1')
        self.addIndent()
        self.nextHeap()
        self.addIndent()

        self.setStack(t1, t0)
        self.addGoto(L7)

        #L5
        self.putLabel(L5)
        self.setHeap('H', t2)
        self.addIndent()
        self.nextHeap()
        self.addIndent()
        self.addExpresion(t2, t2, 1, '+')
        self.addIndent()
        self.addGoto(L1)

        #L7
        self.putLabel(L7)
        
        #fin funcion
        self.addEndFunc()
        self.inNative = False

    def fStringNumber(self):
        if self.strNumber:
            return
        self.strNumber = True
        self.inNative = True

        self.addComment('Funcion stringNumber')
        self.addBeginFunc('typeNumber')

        t0 = self.addTemp()
        t1 = self.addTemp()
        self.addAsignacion(t0, 'H') # guarda la posicion del heap

        
        self.setHeap('H', 78)#N
        self.nextHeap()
        self.setHeap('H', 117)#u
        self.nextHeap()
        self.setHeap('H', 109)#m
        self.nextHeap()
        self.setHeap('H', 98)#b
        self.nextHeap()
        self.setHeap('H', 101)#e
        self.nextHeap()
        self.setHeap('H', 114)#r
        self.nextHeap()
        self.setHeap('H', -1)#-1
        self.nextHeap()
        self.setStack(t1, t0)

        self.addEndFunc()
        self.inNative = False

    def fStringBoolean(self):
        if self.strBoolean:
            return
        self.strBoolean = True
        self.inNative = True

        self.addComment('Funcion typeBoolean')
        self.addBeginFunc('typeBoolean')

        t0 = self.addTemp()
        t1 = self.addTemp()
        self.addAsignacion(t0, 'H') # guarda la posicion del heap

        self.setHeap('H', 66)#B
        self.nextHeap()
        self.setHeap('H', 111)#o
        self.nextHeap()
        self.setHeap('H', 111)#o
        self.nextHeap()
        self.setHeap('H', 108)#l
        self.nextHeap()
        self.setHeap('H', 101)#e
        self.nextHeap()
        self.setHeap('H', 97)#a
        self.nextHeap()
        self.setHeap('H', 110)#n
        self.nextHeap()
        self.setHeap('H', -1)#-1
        self.nextHeap()
        self.setStack(t1, t0)

        self.addEndFunc()
        self.inNative = False

    def fStringString(self):
        if self.strString:
            return
        self.strString = True
        self.inNative = True

        self.addComment('Funcion typeString')
        self.addBeginFunc('typeString')

        t0 = self.addTemp()
        t1 = self.addTemp()
        self.addAsignacion(t0, 'H') # guarda la posicion del heap

        self.setHeap('H', 83)#S
        self.nextHeap()
        self.setHeap('H', 116)#t
        self.nextHeap()
        self.setHeap('H', 114)#r
        self.nextHeap()
        self.setHeap('H', 105)#i
        self.nextHeap()
        self.setHeap('H', 110)#n
        self.nextHeap()
        self.setHeap('H', 103)#g
        self.nextHeap()
        self.setHeap('H', -1)#-1
        self.nextHeap()
        self.setStack(t1, t0)

        self.addEndFunc()
        self.inNative = False

    def fPrintError(self):
        self.setImport('fmt')
        self.addIndent()
        self.addPrintString('c', '69')
        self.addIndent()
        self.addPrintString('c', '82')
        self.addIndent()
        self.addPrintString('c', '82')
        self.addIndent()
        self.addPrintString('c', '79')
        self.addIndent()
        self.addPrintString('c', '82')
        self.addIndent()
        self.addPrintString('c', '10')
        self.addIndent()

    def fPrintArrayNums(self):
        if self.printArray:
            return
        self.printArray = True
        self.inNative = True

        self.addComment('Funcion printArray')
        self.addBeginFunc('printArray')

        tempP = self.addTemp() # t1
        # Temporal puntero a Heap
        tempH = self.addTemp() # t2
        self.addIndent()
        self.addExpresion(tempP, 'P', '1', '+') # t1 = P + 1
        self.addIndent()
        self.getStack(tempH, tempP) # t2 = stack[t1]

        templen = self.addTemp() # t3
        self.getHeap(templen, tempH) # t3 = heap[t2]

        self.addPrintString('c', '91') # [
        
        tempPos = self.addTemp() # t4
        self.addIndent()
        self.addExpresion(tempPos, tempH, '1', '+') # t4 = t2 + 1

        tempContador = self.addTemp() # t5
        self.addAsignacion(tempContador, '0') # t5 = 0
        # L1
        L1 = self.newLabel()
        L2 = self.newLabel()
        L3 = self.newLabel()
        L4 = self.newLabel()
        self.putLabel(L1)

        self.addIndent()
        self.addIf(tempContador, templen, '!=', L2) # if t5 != t3 goto L2
        self.addIndent()
        self.addGoto(L4) # goto L3

        # L2
        self.putLabel(L2)
        self.addIndent()
        tp = self.addTemp() # t6
        self.getHeap(tp, tempPos) # t6 = heap[t4]
        self.addPrint('f',tp)
        self.addIndent()
        tp2 = self.addTemp() # t7
        self.addExpresion(tp2, templen, '1', '-') # t7 = t4 - 1
        self.addIndent()
        self.addIf(tp2, tempContador, '==', L3) # if t7 != t5 goto L3
        self.addIndent()
        self.addPrintString('c', '44') # ,
        self.addExpresion(tempContador, tempContador, '1', '+') # t5 = t5 + 1
        self.addIndent()
        self.addExpresion(tempPos, tempPos, '1', '+') # t4 = t4 + 1
        self.addIndent()
        self.addGoto(L1) # goto L1

        # L3
        self.putLabel(L3)
        self.addIndent()
        self.addPrintString('c', '93') # ]
        self.addExpresion(tempContador, tempContador, '1', '+') # t5 = t5 + 1
        self.addIndent()
        self.addExpresion(tempPos, tempPos, '1', '+') # t4 = t4 + 1
        self.addIndent()
        self.addGoto(L1) # goto L1

        # L4
        self.putLabel(L4)
        self.addIndent()

        self.addEndFunc()
        self.inNative = False




    #! --------------------------------------------------!
    #!                    EXTRAS                         !
    #! --------------------------------------------------!


    def visualizarHeap(self):
        self.setImport('fmt')
        self.addCodigo(f'fmt.Println("HEAP")\n')
        self.addCodigo(f'fmt.Println("posicion, valor")\n')
        self.addCodigo(f'for i := 0; i < 100; i++ {{\n')
        self.addCodigo(f'fmt.Println(i, " ", heap[i])\n')
        self.addCodigo(f'}}\n')
    
    def visualizarStack(self):
        self.setImport('fmt')
        self.addCodigo(f'fmt.Println("STACK")\n')
        self.addCodigo(f'fmt.Println("posicion, valor")\n')
        self.addCodigo(f'for i := 0; i < 100; i++ {{\n')
        self.addCodigo(f'fmt.Println(i, " ", stack[i])\n')
        self.addCodigo(f'}}\n')