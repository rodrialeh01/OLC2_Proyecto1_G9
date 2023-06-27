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
    
    def crearFuncion(self, nombre, params, listaInstrucciones, linea, columna, tipo):
        self.nombre = nombre
        self.params = params
        self.listaInstrucciones = listaInstrucciones
        self.linea = linea
        self.columna = columna
        self.tipo = tipo

    def crearInterface(self, nombre, params, linea, columna):
        self.nombre = nombre
        self.params = params
        self.linea = linea
        self.columna = columna

        for param in self.params:
            param.ejecutar(None,None)
    
    def crearStructDeclarado(self, nombre, paramsDeclarados, objeto, linea, columna):
        
        self.nombre = nombre
        self.paramDeclarados = paramsDeclarados 
        self.objeto = objeto
        self.linea = linea
        self.columna = columna

    def crearsubInterface(self, id_padre, atributo, paramsDeclarados, linea, columna):
        self.id_padre = id_padre
        self.atributo = atributo
        self.paramDeclarados = paramsDeclarados
        self.linea = linea
        self.columna = columna