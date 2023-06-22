from AST.Simbolos.Enums import TIPO_DATO


class C3DSimbolo:
    def __init__(self, nombre, tipo, posicion, globalVar, inHeap):
        self.nombre = nombre
        self.tipo = tipo
        self.posicion = posicion
        #print('global var: ', globalVar)
        self.globalVar = globalVar
        self.inHeap = inHeap

        self.valor = None
        self.tipoAux = ''
        self.length = 0
        self.esRef = False
        self.params = None
    
