# ************* IMPORTACIONES *************
from AST.Expresiones.Logica import Logica
from AST.Expresiones.Operacion import Operacion
from AST.Expresiones.Primitivo import Primitivo
from AST.Expresiones.Relacional import Relacional
from AST.Instrucciones.Consolelog import Consolelog
from AST.ListadoI import ListadoI
from AST.Simbolos.Enums import (TIPO_DATO, TIPO_OPERACION_ARITMETICA,
                                TIPO_OPERACION_LOGICA,
                                TIPO_OPERACION_RELACIONAL)

# ********** ANALIZADOR LEXICO *****************

reservadas = {
    'null' : 'NULL',
    'number' : 'NUMBER',
    'boolean' : 'BOOLEAN',
    'string' : 'STRING',
    'any' : 'ANY',
    'interface' : 'INTERFACE',
    'let' : 'LET',
    'toUpperCase' : 'TOUPPERCASE',
    'toLowerCase' : 'TOLOWERCASE',
    'toFixed' : 'TOFIXED',
    'toExponential' : 'TOEXPONENTIAL',
    'toString'  : 'TOSTRING',
    'split' : 'SPLIT',
    'concat' : 'CONCAT',
    'console' : 'CONSOLE',
    'log' : 'LOG',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'function' : 'FUNCTION',
    'else' : 'ELSE',
    'if' : 'IF',
    'while' : 'WHILE',
    'for' : 'FOR',
    'of' : 'OF',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'Array' : 'ARRAY',
}

tokens = [
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'POTENCIA',
    'MODULO',
    'IGUAL',

    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    'COMA',
    'PTOYCOMA',
    'DOSPUNTOS',
    'PUNTO',

    'MAYORIGUAL',
    'MENORIGUAL',
    'MAYOR',
    'MENOR',
    'IGUALACION',
    'DISTINTO',

    'AND',
    'OR',
    'NOT',
    
    'ID',
    'NUMERO',
    'CADENA',

] + list(reservadas.values())

# Definicion de tokens
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_POTENCIA = r'\^'
t_MODULO = r'\%'

t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_COMA = r'\,'
t_PTOYCOMA = r';'
t_DOSPUNTOS = r':'
t_PUNTO = r'\.'
t_IGUAL = r'\='

t_MAYORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
t_MAYOR = r'\>'
t_MENOR = r'\<'
t_IGUALACION = r'\=\=\='
t_DISTINTO = r'\!\=\='

t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'

#Expresiones regulares
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("F")
        t.value = 0
    return t

def t_CADENA(t):
    r'\"[^\"\n]*\"'
    t.value = t.value[1:-1] #quita las comillas
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value,'ID')
    return t
    
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

#cometarios de linea
def t_COMENTARIO(t):
    r'//.*\n'
    t.lexer.lineno += 1

#comentarios de bloque
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

#Errores lexicos
def t_error(t):
    print(f"Se encontro un error lexico '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = " \t\r"

import ply.lex as lex

lex.lex()

# ********** ANALIZADOR SINTACTICO *****************

#PRECEDENCIA
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('nonassoc', 'MAYOR', 'MENORIGUAL', 'MENOR', 'MAYORIGUAL', 'IGUALACION', 'DISTINTO'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO', 'MODULO'),
    ('right', 'NOT', 'UMENOS')
)

# PRODUCCIONES
# init -> instrucciones
def __init__(t):
    '''
    init : instrucciones
    '''
    t[0] = ListadoI(t[1]) 

# instrucciones -> instrucciones instruccion
def p_instrucciones_lista(t):
    '''
    instrucciones : instrucciones instruccion
    '''
    t[1].append(t[2])
    t[0] = t[1]

# instrucciones -> instruccion
def p_instrucciones_instruccion(t):
    '''
    instrucciones : instruccion
    '''
    t[0] = [t[1]]

# instruccion -> instruccion2
#               |funcion
def p_instruccion(t):
    '''
    instruccion : instruccion2 PTOYCOMA
                | instruccion2
    '''
    t[0] = t[1]

# instruccion 2 -> declaracion
#                | asignacion
#                | condicional
#                | ciclo_while
#                | ciclo_for
#                | ciclo_for_of
#                | impresion
#                | llamada_funcion
#                | return
#                | break
#                | continue
def p_instruccion2(t):
    '''
    instruccion2 : declaracion
                 | asignacion
                 | impresion
    '''
    t[0] = t[1]

# declaracion -> LET ID DOSPUNTOS tipo IGUAL expresion
def p_declaracion1(t):
    '''
    declaracion : LET ID DOSPUNTOS tipo IGUAL expresion
    '''

# declaracion -> LET ID IGUAL expresion
def p_declaracion2(t):
    '''
    declaracion : LET ID IGUAL expresion
    '''

# asignacion -> ID IGUAL expresion
def p_asignacion(t):
    '''
    asignacion : ID IGUAL expresion
    '''

# impresion -> CONSOLE PUNTO LOG PARIZQ expresion PARDER
def p_impresion(t):
    '''
    impresion : CONSOLE PUNTO LOG PARIZQ expresion PARDER
    '''
    t[0] = Consolelog(t[5], t.lineno(1), t.lexpos(1))

#expresiones aritmeticas
# expresion -> expresion MAS expresion
#           | expresion MENOS expresion
#           | expresion POR expresion
#           | expresion DIVIDIDO expresion
#           | expresion POTENCIA expresion
#           | expresion MODULO expresion
#           | MENOS expresion %prec UMENOS
def p_expresion_aritmetica(t):
    '''
    expresion : expresion MAS expresion
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion DIVIDIDO expresion
            | expresion POTENCIA expresion
            | expresion MODULO expresion
            | MENOS expresion %prec UMENOS
    '''
    if len(t) == 3:
        t[0] = Operacion(t[2], None, TIPO_OPERACION_ARITMETICA.NEGATIVO, t.lineno(1), t.lexpos(1),True)
    elif t[2] == '+':
        t[0] = Operacion(t[1], t[3], TIPO_OPERACION_ARITMETICA.SUMA, t.lineno(1), t.lexpos(1),False)
    elif t[2] == '-':
        t[0] = Operacion(t[1], t[3], TIPO_OPERACION_ARITMETICA.RESTA, t.lineno(1), t.lexpos(1),False)
    elif t[2] == '*':
        t[0] = Operacion(t[1], t[3], TIPO_OPERACION_ARITMETICA.MULTIPLICACION, t.lineno(1), t.lexpos(1),False)
    elif t[2] == '/':
        t[0] = Operacion(t[1], t[3], TIPO_OPERACION_ARITMETICA.DIVISION, t.lineno(1), t.lexpos(1),False)
    elif t[2] == '^':
        t[0] = Operacion(t[1], t[3], TIPO_OPERACION_ARITMETICA.POTENCIA, t.lineno(1), t.lexpos(1),False)
    elif t[2] == '%':
        t[0] = Operacion(t[1], t[3], TIPO_OPERACION_ARITMETICA.POTENCIA, t.lineno(1), t.lexpos(1),False)

#expresiones relacionales
# expresion -> expresion MAYOR expresion
#           | expresion MENOR expresion
#           | expresion MAYORIGUAL expresion
#           | expresion MENORIGUAL expresion
#           | expresion IGUALACION expresion
#           | expresion DISTINTO expresion
def p_expresion_relacional(t):
    '''
    expresion : expresion MAYOR expresion
            | expresion MENOR expresion
            | expresion MAYORIGUAL expresion
            | expresion MENORIGUAL expresion
            | expresion IGUALACION expresion
            | expresion DISTINTO expresion
    '''
    if t[2] == '>':
        t[0] = Relacional(t[1], t[3], TIPO_OPERACION_RELACIONAL.MAYOR_QUE, t.lineno(1), t.lexpos(1))
    elif t[2] == '<':
        t[0] = Relacional(t[1], t[3], TIPO_OPERACION_RELACIONAL.MENOR_QUE, t.lineno(1), t.lexpos(1))
    elif t[2] == '>=':
        t[0] = Relacional(t[1], t[3], TIPO_OPERACION_RELACIONAL.MAYOR_IGUAL_QUE, t.lineno(1), t.lexpos(1))
    elif t[2] == '<=':
        t[0] = Relacional(t[1], t[3], TIPO_OPERACION_RELACIONAL.MENOR_IGUAL_QUE, t.lineno(1), t.lexpos(1))
    elif t[2] == '===':
        t[0] = Relacional(t[1], t[3], TIPO_OPERACION_RELACIONAL.IGUAL_IGUAL, t.lineno(1), t.lexpos(1))
    elif t[2] == '!==':
        t[0] = Relacional(t[1], t[3], TIPO_OPERACION_RELACIONAL.DIFERENTE, t.lineno(1), t.lexpos(1))
    

#expresiones logicas
# expresion -> expresion AND expresion
#           | expresion OR expresion
#           | NOT expresion
def p_expresion_logica(t):
    '''
    expresion : expresion AND expresion
            | expresion OR expresion
            | NOT expresion
    '''
    if len(t) == 3:
        t[0] = Logica(t[2], None, TIPO_OPERACION_LOGICA.NOT, t.lineno(1), t.lexpos(1), True)
    elif t[2] == '&&':
        t[0] = Logica(t[1], t[3], TIPO_OPERACION_LOGICA.AND, t.lineno(1), t.lexpos(1), False)
    elif t[2] == '||':
        t[0] = Logica(t[1], t[3], TIPO_OPERACION_LOGICA.OR, t.lineno(1), t.lexpos(1), False)

#expresiones primitivas
# expresion -> ENTERO
#           | DECIMAL
#           | CADENA
#           | ID

def p_expresion_primitiva(t):
    '''
    expresion : NUMERO
            | CADENA
            | ID
            | TRUE
            | FALSE
    '''

    if t.slice[1].type == 'NUMERO':
        t[0] = Primitivo(TIPO_DATO.NUMERO, t[1], t.lineno(1), t.lexpos(1))
    elif t.slice[1].type == 'CADENA':
        t[0] = Primitivo(TIPO_DATO.CADENA, t[1], t.lineno(1), t.lexpos(1))
    elif t.slice[1].type == 'ID':
        pass
    elif t.slice[1].type == 'TRUE':
        t[0] = Primitivo(TIPO_DATO.BOOLEANO, True, t.lineno(1), t.lexpos(1))
    elif t.slice[1].type == 'FALSE':
        t[0] = Primitivo(TIPO_DATO.BOOLEANO, False, t.lineno(1), t.lexpos(1))

#Listado de tipos
# tipo -> NUMBER
#      | STRING
#      | BOOLEAN
#      | ANY

def p_tipo(t):
    '''
    tipo : NUMBER
        | STRING
        | BOOLEAN
        | ANY
    '''
    if t[1] == 'number':
        t[0] = TIPO_DATO.NUMERO
    elif t[1] == 'string':
        t[0] = TIPO_DATO.CADENA
    elif t[1] == 'boolean':
        t[0] = TIPO_DATO.BOOLEANO
    elif t[1] == 'any':
        t[0] = TIPO_DATO.ANY

#errores sintacticos	
def p_error(t):
    print("Error sintáctico en '%s'" % t.value + " en la linea " + str(t.lineno) + " y columna " + str(t.lexpos))

import ply.yacc as yacc

parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)