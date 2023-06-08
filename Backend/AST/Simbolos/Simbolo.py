from AST.Simbolos.Enums import TIPO_DATO


class Simbolo:
    def __init__(self):
        self.linea = 0
        self.columna = 0
        self.nombre = ""
        self.tipo = TIPO_DATO.ERROR
        self.valor = None
        self.entorno = None
        self.valorRef = None
    
    def crearFuncion(self, nombre, params, listaInstrucciones, linea, columna):
        self.nombre = nombre
        self.params = params
        self.listaInstrucciones = listaInstrucciones
        self.linea = linea
        self.columna = columna

    def crearInterface(self, nombre, params, linea, columna):
        self.nombre = nombre
        self.params = params
        self.linea = linea
        self.columna = columna

        print("ESTE ES EL NOMBRE DE LA INTERFAZ: ", self.nombre)
        print("ESTOS SON LOS PARAMETROS DE LA INTERFAZ: :")
        for param in self.params:
            param.ejecutar(None,None)
        