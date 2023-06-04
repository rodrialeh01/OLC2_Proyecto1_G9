from abc import ABC, abstractmethod

from AST.Simbolos.Retorno import Retorno


class Expresion(ABC):
    @abstractmethod
    def ejecutar(self, entorno, helper) -> Retorno:
        pass