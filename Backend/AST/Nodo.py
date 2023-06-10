class Nodo:
    def __init__(self, valor):
        self.id = 0
        self.valor = valor
        self.listaH = []
        
    def agregarHijo(self, hijo):
        self.listaH.append(hijo)
    
    