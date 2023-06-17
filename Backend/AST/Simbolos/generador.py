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
        if libreria not in self.importaciones2:
            self.importaciones2.remove(libreria)
        else:
            return
        
        code = f'import (\n\t"{libreria}"\n)\n'

    # ? ------------------------------------------------------------

    def obtEncabezado(self):
        code = '''
/*----------- HEADER -----------*/
package main;\n \n'''
        if len(self.importaciones) > 0:
            for imp in self.importaciones:
                code += imp
        if len(self.temporales) > 0:
            code += 'var '
            for temporal in self.temporales:
                code += temporal + ', '
            code = code[:-2]
            code += ' float64; \n'
        code+= '''
var P, H float64;\n
var stack[30101999] float64;\n
var heap[30101999] float64;\n
\n'''
        return code
    
    def obtCodigo(self):   
        return f'{self.obtEncabezado()}{self.natives}{self.funcs}\nfunc main() {{\n{self.codigo}}}' 
    

    def addCodigo(self, codigo, tab='\t'):
        if self.inNative:
            if self.natives == '':
                self.natives = self.natives + "\* --- NATIVAS --- */"
            self.natives += tab + codigo
        elif self.inFunc:
            if self.funcs == '':
                self.funcs = self.funcs + "\* --- FUNCIONES --- */"
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
        self.codigo += f'heap[int({pos})]= {valor};\n'
    
    def getHeap(self, place, pos): #obtiene un valor del heap
        self.codigo += f'{place} = heap[int({pos})];\n'

    def nextHeap(self): #obtiene la siguiente posicion del heap
        self.codigo += f'H = H + 1;\n'

    #* 
    #* MANEJO DE LABELS
    #*

    def newLabel(self): #crea una nueva etiqueta
        label = f'L{self.L}'
        self.L += 1
        return label
    
    def putLabel(self, label): #agrega una etiqueta
        self.addCodigo(f'{label}:\n')

    def addIndent(self):
        self.addCodigo("")

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


    #! --------------------------------------------------!
    #!                    FUNCIONES                        !
    #! --------------------------------------------------!

    def addBeginFunc(self, id):
        if not self.inNatives:
            self.inFunc = True
        
        self.addCodigo(f'/*----------- FUNCION {id} -----------*/\n')
        self.addCodigo(f'func {id}() {{\n')

    def addEndFunc(self):
        if not self.inNatives:
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
        self.inNatives = True #se marca que se esta en una funcion nativa

        self.addBeginFunc('printString')
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.newLabel()
        # Temporal puntero a Stack
        tempP = self.addTemp()
        # Temporal puntero a Heap
        tempH = self.addTemp()
        self.addExpresion(tempP, 'P', '1', '+')
        self.getStack(tempH, tempP)
        # Temporal para comparar
        tempC = self.addTemp()
        self.putLabel(compareLbl)
        self.addIndent()
        self.getHeap(tempC, tempH)
        self.addIndent()
        self.addIf(tempC, '-1', '==', returnLbl)
        self.addIndent()
        self.addPrint('c', tempC)
        self.addIndent()
        self.addExpresion(tempH, tempH, '1', '+')
        self.addIndent()
        self.addGoto(compareLbl)
        self.putLabel(returnLbl)
        self.addEndFunc()
        self.inNatives = False