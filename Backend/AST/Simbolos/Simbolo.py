from AST.Simbolos.Enums import TIPO_DATO


class Simbolo:
    def __init__(self):
        self.linea = 0
        self.columna = 0
        self.nombre = ""
        self.tipo = TIPO_DATO.ERROR
        self.valor = None
        self.entorno = None
    
    