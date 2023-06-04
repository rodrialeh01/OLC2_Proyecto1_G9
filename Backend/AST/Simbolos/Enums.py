from enum import Enum


class TIPO_DATO(Enum):
    NUMERO = 0,
    CADENA = 1,
    BOOLEANO = 2,
    NULL = 3,
    ERROR = 4,
    ANY = 5,

class ERROR(Enum):
    LEXICO = 1,
    SINTACTICO = 2,
    SEMANTICO = 3,

class TIPO_OPERACION_ARITMETICA(Enum):
    SUMA = 1,
    RESTA = 2,
    MULTIPLICACION = 3,
    DIVISION = 4,
    POTENCIA = 5,
    MODULO = 6,
    NEGATIVO = 7

class TIPO_OPERACION_RELACIONAL(Enum):
    MAYOR_QUE = 1,
    MENOR_QUE = 2,
    MAYOR_IGUAL_QUE = 3,
    MENOR_IGUAL_QUE = 4,
    IGUAL_IGUAL = 5,
    DIFERENTE = 6

class TIPO_OPERACION_LOGICA(Enum):
    AND = 1,
    OR = 2,
    NOT = 3