class Entorno:
    def __init__ (self, anterior = None):
        self.anterior = anterior
        self.tablaSimbolos = {}
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
        self.tablaSimbolos[id] = simbolo

    #obtener simbolo:
    def ObtenerSimbolo(self, id):
        env = self
        while env != None:
            if id in env.tablaSimbolos:
                return env.tablaSimbolos[id]
            env = env.anterior
        return None
    
    #actualizar simbolo:
    def ActualizarSimbolo(self, id, simbolo):
        env = self
        while env != None:
            if id in env.tablaSimbolos:
                env.tablaSimbolos[id] = simbolo
            env = env.anterior


