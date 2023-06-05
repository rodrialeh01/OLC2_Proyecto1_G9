import datetime

class Error:
    def __init__(self, fila, columna, tipo, desc):
        self.fila = fila
        self.column = columna
        self.tipo = tipo
        self.desc = desc
        self.fechaHora = datetime.datetime.now()
