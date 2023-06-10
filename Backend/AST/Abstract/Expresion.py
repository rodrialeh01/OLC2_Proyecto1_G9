from abc import ABC, abstractmethod
from AST.Nodo import Nodo
from AST.Simbolos.Retorno import Retorno


class Expresion(ABC):
    @abstractmethod
    def ejecutar(self, entorno, helper) -> Retorno:
        pass

    @abstractmethod
    def genArbol(self) -> Nodo:
        pass 