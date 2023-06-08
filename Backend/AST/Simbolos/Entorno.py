class Entorno:
    def __init__ (self, anterior = None):
        self.anterior = anterior
        self.tablaSimbolos = {}
        self.tablaFunciones = {}
        self.tablaInterfaces = {}
        self.actual = ""

    def getActual(self):
        return self.actual
    
    def setActual(self, actual):
        self.actual = actual

# -------------------------------- símbolos --------------------------------
    #verificacion de existencia:
    def ExisteSimbolo(self, id):
        entorno = self
        while entorno != None:
            if id in entorno.tablaSimbolos:
                return True
            entorno = entorno.anterior
        return False
    
    #agregar simbolo:
    def AgregarSimbolo(self, id, simbolo):
        print("agregando simbolo: " + id)
        self.tablaSimbolos[id] = simbolo

    #obtener simbolo:
    def ObtenerSimbolo(self, id):
        env = self
        while env != None:
            if id in env.tablaSimbolos:
                return env.tablaSimbolos[id]
            env = env.anterior
        return None
    
    #buscar simbolo local:
    def BuscarSimboloLocal(self, id):
        if id in self.tablaSimbolos:
            return True
        return False


    #actualizar simbolo:
    def ActualizarSimbolo(self, id, simbolo):
        env = self
        while env != None:
            if id in env.tablaSimbolos:
                env.tablaSimbolos[id] = simbolo
            env = env.anterior

# -------------------------------- funciones --------------------------------
    #verificacion de existencia:
    def ExisteFuncion(self, id):
        print("Buscando funcion: " + id)
        env = self
        while env != None:
            if id in env.tablaFunciones:
                return True
            env = env.anterior
        return False
    
    #agregar funcion:

    def ObtenerFuncion(self, id):
        env = self
        while env != None:
            if id in env.tablaFunciones:
                return env.tablaFunciones[id]
            env = env.anterior
        return None
    

    def AgregarFuncion(self, id, funcion):
        self.tablaFunciones[id] = funcion

# -------------------------------- interfaces --------------------------------

#guardar interface:
    def AgregarInterface(self, id, interface):
        self.tablaInterfaces[id] = interface

#verificar existencia:
    def ExisteInterface(self, id):
        env = self
        while env != None:
            if id in env.tablaInterfaces:
                return True
            env = env.anterior
        return False

#obtener interface:
    def ObtenerInterface(self, id):
        env = self
        while env != None:
            if id in env.tablaInterfaces:
                return env.tablaInterfaces[id]
            env = env.anterior
        return None

