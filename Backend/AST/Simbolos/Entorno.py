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



# para la tabla de simbolos HTML:
    def getSimbolos(self):

        actual = self
        print(actual.getActual())

        codigo_html = ""
        codigo_html += '''
        <table align="center" class="table table-striped "> \n
        <thead><tr> <th colspan="5">TABLA DE SÍMBOLOS</th> </tr></thead>\n
        <tr class="table-dark"><th>Nombre</th><th>Tipo</th><th>Ámbito</th><th>Fila</th><th>Columna</th></tr>\n
        '''
        while actual != None:
            for i in actual.tablaSimbolos:
                print("-*-*-*-*-", str(actual.tablaSimbolos[i].tipo))
                codigo_html += "<tr>"
                codigo_html += "<td>" + str(i) + "</td>\n"
                codigo_html += "<td>" + str(actual.tablaSimbolos[i].tipo) + "</td>\n"
                codigo_html += "<td>" + str(actual.actual) + "</td>\n"
                codigo_html += "<td>" + str(actual.tablaSimbolos[i].linea) + "</td>\n"
                codigo_html += "<td>" + str(actual.tablaSimbolos[i].columna) + "</td>\n"
                codigo_html += "</tr>"
            actual = actual.anterior


        codigo_html += "</table>"


        return codigo_html