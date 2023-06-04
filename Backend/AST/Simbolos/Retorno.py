from AST.Simbolos.Enums import TIPO_DATO


class Retorno:
    def __init__(self, valor = None, tipo = TIPO_DATO.ERROR):
        self.valor = valor
        self.tipo = tipo
        