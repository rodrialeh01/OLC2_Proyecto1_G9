from AST.Simbolos.Enums import *


class Helper:
    def __init__(self):
        self.ciclo = ""
        self.funcion = ""
        self.consola = ""
        self.Ts =""

    def getFuncion(self):
        return self.funcion
    
    def setFuncion(self, funcion):
        self.funcion = funcion

    def getCiclo(self):
        return self.ciclo

    def setCiclo(self, ciclo):
        self.ciclo = ciclo

    def getConsola(self):
        return self.consola
    
    def getTs(self):
        return self.Ts
    
    def setTs(self, entorno):
        actual = entorno
        Ts = ""
        codigo_html = "\n"
        '''
        for i in actual.tablaSimbolos:
            codigo_html += "<tr>"
            codigo_html += "<td>" + str(i) + "</td>\n"
            #print("-------------- TIPO: ", actual.tablaSimbolos[i].tipo)
            codigo_html += "<td>" + obtTipoDato(actual.tablaSimbolos[i].tipo) + "</td>\n"
            codigo_html += "<td>" + str(actual.actual) + "</td>\n"
            codigo_html += "<td>" + str(actual.tablaSimbolos[i].linea) + "</td>\n"
            codigo_html += "<td>" + str(actual.tablaSimbolos[i].columna) + "</td>\n"
            codigo_html += "</tr>"

        for i in actual.tablaFunciones:
            codigo_html += "<tr>"
            codigo_html += "<td>" + str(actual.tablaFunciones[i].nombre) + "</td>\n"
            codigo_html += "<td> FALTA EL TIPO DE FUNCIÓN AAAAAAAAAAAAAAAAAAAAAAAAA </td>\n"
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
        '''

        self.Ts += Ts + codigo_html + "\n"


    def setConsola(self, consola):
        self.consola += str(consola) + "\n"
        
        
