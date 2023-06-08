from AST.Simbolos.Simbolo import Simbolo


class Interface(Simbolo):
    def __init__(self, id, listaParametros, linea, columna):
        super().__init__()
        super().crearInterface(id, listaParametros, linea, columna);
    
        