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
                if i != len(self.importaciones) - 1:
                    code += '\t\"' + self.importaciones[i] + '\",\n'
                else:
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
                self.funcs = self.funcs + "/* --- FUNCIONES --- */"
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
        print("ORDEN2")
        self.addCodigo(f'{place} = heap[int({pos})];\n')

    def nextHeap(self): #obtiene la siguiente posicion del heap
        print("ORDEN1")
        self.addCodigo(f'H = H + 1;\n')

    #* 
    #* MANEJO DE LABELS
    #*

    def newLabel(self): #crea una nueva etiqueta
        label = f'L{self.L}'
        self.L += 1
        return label
    
    def putLabel(self, label): #agrega una etiqueta
        print("LABEEEEEEEEEL")
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
    def addPrint(self, type, valor):
        self.setImport('fmt')
        self.addCodigo(f'fmt.Printf("%{type}", {valor});\n')

    #para imprimir el string
    def addPrintString(self, type, valor):
        self.setImport('fmt')
        self.addCodigo(f'fmt.Printf("%{type}", int({valor}));\n')

    #! --------------------------------------------------!
    #!                    FUNCIONES                        !
    #! --------------------------------------------------!

    def addBeginFunc(self, id):
        if not self.inNative:
            self.inFunc = True
        
        self.addCodigo(f'/*----------- FUNCION {id} -----------*/\n')
        self.addCodigo(f'func {id}() {{\n')

    def addEndFunc(self):
        if not self.inNative:
            self.inFunc = False
        self.addCodigo('}\n\n')

    #! --------------------------------------------------!
    #!                    NATIVAS                         !
    #! --------------------------------------------------!

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
        print("RETURN LABEL", returnLbl) #L0
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.newLabel()
        print("COMPARE LABEL", compareLbl) #L1
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