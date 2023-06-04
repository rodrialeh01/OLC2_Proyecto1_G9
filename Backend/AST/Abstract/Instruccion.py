from abc import ABC, abstractmethod


class Instruccion(ABC):
    
    @abstractmethod
    def ejecutar(self, entorno, helper):
        pass