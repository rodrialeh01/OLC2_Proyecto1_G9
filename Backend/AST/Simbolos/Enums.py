from enum import Enum


class TIPO_DATO(Enum):
    NUMERO = 0,
    CADENA = 1,
    BOOLEANO = 2,
    NULL = 3,
    ERROR = 4,
    ANY = 5,
    ARRAY = 6,
    ARRAY_NUMBER = 7,
    ARRAY_STRING = 8,
    ARRAY_BOOLEAN = 9,
    INTERFACE = 10,
    ARRAY_INTERFACE = 11,
    ARRAY_NULL = 12,
    CHAR = 13

def obtTipoDato(i):
    if i == TIPO_DATO.NUMERO:
        return "Number"
    elif i == TIPO_DATO.CADENA:
        return "String"
    elif i == TIPO_DATO.BOOLEANO:
        return "Boolean"
    elif i == TIPO_DATO.NULL:
        return "null"
    elif i == TIPO_DATO.ERROR:
        return "Error"
    elif i == TIPO_DATO.ANY:
        return "Any"
    elif i == TIPO_DATO.ARRAY:
        return "Array"
    elif i == TIPO_DATO.ARRAY_NUMBER:
        return "Array"
    elif i == TIPO_DATO.ARRAY_STRING:
        return "Array"
    elif i == TIPO_DATO.ARRAY_BOOLEAN:
        return "Array"
    elif i == TIPO_DATO.INTERFACE:
        return "interface"
    elif i == TIPO_DATO.ARRAY_INTERFACE:
        return "Array"
    elif i == TIPO_DATO.ARRAY_NULL:
        return "Array"
    

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