from abc import ABC, abstractmethod
from AST.Nodo import Nodo
from AST.Simbolos.Retorno import Retorno


class Expresion(ABC):

    def __init__(self):
        self.trueLabel = ''
        self.falseLabel = ''


    @abstractmethod
    def ejecutar(self, entorno, helper) -> Retorno:
        pass

    @abstractmethod
    def genC3D(self, entorno, helper):
        pass

    @abstractmethod
    def genArbol(self) -> Nodo:
        pass 

    def getTrueLabel(self):
        return self.trueLabel
    
    def setTrueLabel(self, trueLabel):
        self.trueLabel = trueLabel

    def getFalseLabel(self):
        return self.falseLabel
    
    def setFalseLabel(self, falseLabel):
        self.falseLabel = falseLabel
