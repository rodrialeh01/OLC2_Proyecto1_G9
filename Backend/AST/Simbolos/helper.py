class Helper:
    def __init__(self):
        self.ciclo = ""
        self.funcion = ""
        self.consola = ""

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
    
    def setConsola(self, consola):
        self.consola += str(consola) + "\n"
        