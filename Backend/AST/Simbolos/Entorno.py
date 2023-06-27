from AST.Simbolos.C3DSimbolo import C3DSimbolo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato


class Entorno:
    def __init__ (self, anterior):
        ##print("creando entorno")
        ##print("ANTERIOR; ", anterior)
        self.anterior = anterior
        self.tablaSimbolos = {}
        self.tablaFunciones = {}
        self.tablaInterfaces = {}
        self.tablaInterfacesDeclaradas = {}
        self.tablaSubinterfaces = {}
        self.actual = ""

        #! PARA EL C3D:
        self.breakLabel = ""
        self.returnLabel = ""
        self.continueLabel = ""
        self.retencionTemps = False
        self.size = 0 #? puntero que se va incrementando
        if anterior != None:
            self.size = self.anterior.size

    def getActual(self):
        return self.actual
    
    def setActual(self, actual):
        self.actual = actual

    def getAnterior(self):
        return self.anterior
    

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
        ##print("agregando simbolo: " + id)
        self.tablaSimbolos[id] = simbolo
        ##print("simbolo agregado: " + id)
        ###print("VALORES: ", self.tablaSimbolos[id].valor)
        

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
                return
            env = env.anterior


# -------------------------------- funciones --------------------------------
    #verificacion de existencia:
    def ExisteFuncion(self, id):
        ##print("Buscando funcion: " + id)
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
        print("agregue la interfaz: ", id)
        self.tablaInterfaces[id] = interface

    def BuscarInterfaceLocal(self, id):
        if id in self.tablaInterfaces:
            return True
        return False

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

# -------------------------------- interfaces declaradas --------------------------------
    def AgregarInterfaceDeclarada(self, id, interfazdeclarada):
        self.tablaInterfacesDeclaradas[id] = interfazdeclarada
    
    def ExisteInterfaceDeclarada(self, id):
        env = self
        while env != None:
            if id in env.tablaInterfacesDeclaradas:
                return True
            env = env.anterior
        return False
    
    def BuscarInterfaceDeclaradaLocal(self, id):
        if id in self.tablaInterfacesDeclaradas:
            return True
        return False

    def ObtenerInterfaceDeclarada(self, id):
        env = self
        while env != None:
            if id in env.tablaInterfacesDeclaradas:
                return env.tablaInterfacesDeclaradas[id]
            env = env.anterior
        return None

    def ActualizarInterfaceDeclarada(self, id, interfazdeclarada):
        env = self
        while env != None:
            if id in env.tablaInterfacesDeclaradas:
                env.tablaInterfacesDeclaradas[id] = interfazdeclarada
            env = env.anterior

# -------------------------------- SUB-INTERFACES --------------------------------
    def AgregarSubInterface(self, id_padre, atributo, subinterface):
        self.subinterfaces[id_padre + "-" + atributo] = subinterface

    def ExisteSubInterface(self, id_combinado):
        env = self
        while env != None:
            if id_combinado in env.tablaSubinterfaces:
                return True
            env = env.anterior
        return False
    
    def ObtenerSubInterface(self, id_combinado):
        env = self
        while env != None:
            if id_combinado in env.tablaSubinterfaces:
                return env.tablaSubinterfaces[id_combinado]
            env = env.anterior
        return None
    
    def ActualizarSubInterface(self, id_combinado, subinterface):
        env = self
        while env != None:
            if id_combinado in env.tablaSubinterfaces:
                env.tablaSubinterfaces[id_combinado] = subinterface
            env = env.anterior


# para la tabla de simbolos HTML:
    def getSimbolos(self):

        actual = self
        codigo_html = ""
        
        while actual != None:
            for i in actual.tablaSimbolos:
                codigo_html += "<tr>"
                codigo_html += "<td>" + str(i) + "</td>\n"
                codigo_html += "<td>" + obtTipoDato(actual.tablaSimbolos[i].tipo) + "</td>\n"
                codigo_html += "<td>" + str(actual.actual) + "</td>\n"
                codigo_html += "<td>" + str(actual.tablaSimbolos[i].linea) + "</td>\n"
                codigo_html += "<td>" + str(actual.tablaSimbolos[i].columna) + "</td>\n"
                codigo_html += "</tr>"

            for i in actual.tablaFunciones:
                codigo_html += "<tr>"
                codigo_html += "<td>" + str(actual.tablaFunciones[i].nombre) + "</td>\n"
                if actual.tablaFunciones[i].tipo != None:
                    if (isinstance(actual.tablaFunciones[i].tipo,TIPO_DATO)):
                        codigo_html += "<td> " +  obtTipoDato(actual.tablaFunciones[i].tipo) + " </td>\n"
                    else:
                        codigo_html += "<td> Interface: " +  actual.tablaFunciones[i].tipo + " </td>\n"
                else:
                    codigo_html += "<td> Void </td>\n"
                # codigo_html += "<td>" + str(actual.tablaFunciones[i].tipo) + "</td>\n"
                codigo_html += "<td>" + str(actual.actual) + "</td>\n"
                codigo_html += "<td>" + str(actual.tablaFunciones[i].linea) + "</td>\n"
                codigo_html += "<td>" + str(actual.tablaFunciones[i].columna) + "</td>\n"
                codigo_html += "</tr>"

            for i in actual.tablaInterfacesDeclaradas:
                codigo_html += "<tr>"
                codigo_html += "<td>" + str(actual.tablaInterfacesDeclaradas[i].nombreDeclarado) + "</td>\n"
                codigo_html += "<td>" + str(actual.tablaInterfacesDeclaradas[i].id_interface) + "</td>\n"
                codigo_html += "<td>" + str(actual.actual) + "</td>\n"
                codigo_html += "<td>" + str(actual.tablaInterfacesDeclaradas[i].linea) + "</td>\n"
                codigo_html += "<td>" + str(actual.tablaInterfacesDeclaradas[i].columna) + "</td>\n"
                codigo_html += "</tr>"
            actual = actual.getAnterior()

        
        #codigo_html += "</table>"

        return codigo_html
    

    #*---------------------------------------------------------------------------
    #*- C3D:
    def setEntorno(self, id, tipo, inHeap, find = True):
        if find:
            actual = self
            while actual != None:
                if id in actual.tablaSimbolos:
                    actual.tablaSimbolos[id].inHeap = inHeap
                    actual.tablaSimbolos[id].tipo = tipo
                    return actual.tablaSimbolos[id]
                else:
                    actual = actual.getAnterior()
        
        if id in self.tablaSimbolos:
            self.tablaSimbolos[id].inHeap = inHeap
            self.tablaSimbolos[id].tipo = tipo
            return self.tablaSimbolos[id]
        else:
            simbolo = C3DSimbolo(id, tipo, self.size, self.anterior == None, inHeap)
            self.size += 1 
            self.tablaSimbolos[id] = simbolo
            return self.tablaSimbolos[id]
    #!----- EN C3D TAMBIÉN SE UTILIZA Obtenersimbolo() y ExisteSimbolo() PARA VERIFICACIONES -----!