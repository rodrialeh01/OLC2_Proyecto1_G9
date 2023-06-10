from abc import ABC, abstractmethod

from AST.Nodo import Nodo


class Instruccion(ABC):
    
    @abstractmethod
    def ejecutar(self, entorno, helper):
        pass

    @abstractmethod
    def genArbol(self) -> Nodo:
        pass