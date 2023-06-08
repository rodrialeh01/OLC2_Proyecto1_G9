# ************* IMPORTACIONES *************
from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Expresiones.Dec import Dec
from AST.Expresiones.Identificador import Identificador
from AST.Expresiones.Inc import Inc
from AST.Expresiones.Logica import Logica
from AST.Expresiones.Nativas.Cast_String import Cast_String
from AST.Expresiones.Nativas.Concat import Concat
from AST.Expresiones.Nativas.Split import Split
from AST.Expresiones.Nativas.toExponential import ToExponential
from AST.Expresiones.Nativas.toFixed import ToFixed
from AST.Expresiones.Nativas.toLowerCase import ToLowerCase
from AST.Expresiones.Nativas.toString import ToString
from AST.Expresiones.Nativas.toUpperCase import ToUpperCase
from AST.Expresiones.Operacion import Operacion
from AST.Expresiones.Primitivo import Primitivo
from AST.Expresiones.Relacional import Relacional
from AST.Instrucciones.Asignacion import Asignacion
from AST.Instrucciones.Ciclos.For import For
from AST.Instrucciones.Ciclos.ForOf import ForOf
from AST.Instrucciones.Ciclos.While import While
from AST.Instrucciones.Comentarios import Comentarios
from AST.Instrucciones.Condicional.If import If
from AST.Instrucciones.Consolelog import Consolelog
from AST.Instrucciones.Declaracion import Declaracion
from AST.Instrucciones.Transferencia.Break import Break
from AST.Instrucciones.Transferencia.Continue import Continue
from AST.Instrucciones.Transferencia.Return import Return
from AST.ListadoI import ListadoI
from AST.Simbolos.Enums import (TIPO_DATO, TIPO_OPERACION_ARITMETICA,
                                TIPO_OPERACION_LOGICA,
                                TIPO_OPERACION_RELACIONAL)
from AST.SingletonErrores import SingletonErrores

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
    'String' : 'CAST_STRING',
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
    'DECREMENTO',
    'INCREMENTO',

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
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'COMENTARIO',
    'COMENTARIO_MULTILINEA',

] + list(reservadas.values())

# Definicion de tokens
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIVIDIDO = r'\/'
t_POTENCIA = r'\^'
t_MODULO = r'\%'
t_DECREMENTO = r'\-\-'
t_INCREMENTO = r'\+\+'

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
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("F")
        t.value = 0
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("F")
        t.value = 0.0

def t_CADENA(t):
    r'\"[^\"\n]*\"'
    t.value = t.value[1:-1] #quita las comillas
    return t

def t_ID(t):
    r'[a-zA-Z_]([a-zA-Z0-9_])*'
    t.type = reservadas.get(t.value,'ID')
    return t
    
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

#cometarios de linea
def t_COMENTARIO(t):
    r'\/\/.*\n'
    t.lexer.lineno += 1
    print("Comentario de linea")

#comentarios de bloque
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def f_columna(input,token):
    line_s = input.rfind('\n',0,token.lexpos) + 1
    return (token.lexpos - line_s) + 1

#Errores lexicos
def t_error(t):
    #singleton:
    s = SingletonErrores.getInstance()
    columna = f_columna(entrada, t)
    s.addError(Error(str(t.lexer.lineno), str(columna) ,"Error Lexico", "No se reconoce "+t.value[0]+" como parte del lenguaje") )
    #print(f"AAAAAAAAAAAAAAAAAAAAAAAA Se encontro un error lexico '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = " \t\r"

import ply.lex as lex

lex.lex()

# ********** ANALIZADOR SINTACTICO *****************

precedence = (
    ('right','INCREMENTO','DECREMENTO'),
    ('left','OR'),
    ('left','AND'),
    ('right','NOT'),
    ('left', 'MAYOR', 'MENORIGUAL', 'MENOR', 'MAYORIGUAL', 'IGUALACION', 'DISTINTO'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO', 'MODULO'),
    ('left','POTENCIA'),
    ('nonassoc','PARIZQ','PARDER'),
    ('right', 'UMENOS')
)

# !----------------------- PRODUCCIONES------------

# ? init : instrucciones
def __init__(t):
    '''
    init : instrucciones
    '''
    t[0] = ListadoI(t[1])

# ? instrucciones : instrucciones instruccion
def p_instrucciones(t):
    '''
    instrucciones : instrucciones instruccion
    '''
    t[1].append(t[2])
    t[0] = t[1]

# ? instrucciones : instruccion
def p_instrucciones_instruccion(t):
    '''
    instrucciones : instruccion
    '''
    t[0] = [t[1]]

# ? instruccion : instruccion2
def p_instruccion(t):
    '''
    instruccion : instruccion2
    '''
    t[0] = t[1]

# ? instruccion : funcion
def p_instruccion_funcion(t):
    '''
    instruccion : funcion
    '''
    t[0] = t[1]

# ? instruccion : comentarios
def p_instruccion_comentarios(t):
    '''
    instruccion : comentarios
    '''
    t[0] = t[1]

# ? instruccion2 : instruccion3 PTOYCOMA
def p_instruccion2(t):
    '''
    instruccion2 : instruccion3 PTOYCOMA
    '''
    t[0] = t[1]

# ? instruccion2 : instruccion3
def p_instruccion2_instruccion3(t):
    '''
    instruccion2 : instruccion3
    '''
    t[0] = t[1]

# ? instruccion4 : instruccion4 instruccion2
def p_instruccion4(t):
    '''
    instruccion4 : instruccion4 instruccion2
    '''
    t[1].append(t[2])
    t[0] = t[1]

# ? instruccion4 : instruccion2
def p_instruccion4_instruccion2(t):
    '''
    instruccion4 : instruccion2
    '''
    t[0] = [t[1]]

# ? bloque : LLAIZQ instruccion4 LLADER
def p_bloque(t):
    '''
    bloque : LLAIZQ instruccion4 LLADER
    '''
    t[0] = t[2]

# ? bloque : LLAIZQ LLADER
def p_bloque2(t):
    '''
    bloque : LLAIZQ LLADER
    '''
    t[0] = []

# ? instruccion3 : declaracion
# ?              | asignacion
# ?              | impresion
# ?              | condicional
# ?              | ciclo_while
# ?              | ciclo_for
# ?              | ciclo_for_of
# ?              | llamada_funcion
# ?              | return
# ?              | break
# ?              | continue
def p_instruccion3(t):
    '''
    instruccion3 : declaracion
                 | asignacion
                 | impresion
                 | condicional
                 | ciclo_while
                 | ciclo_for
                 | ciclo_for_of
                 | llamada_funcion
                 | return
                 | break
                 | continue
                 | comentarios
    '''
    t[0] = t[1]

# ? instruccion : COMENTARIO
def p_instruccion_comentario(t):
    '''
    comentarios : COMENTARIO
    '''
    print("comentario")
    t[0] = Comentarios(t[1], t.lineno(1), t.lexpos(1))

# ? instruccion : COMENTARIO_MULTILINEA
def p_instruccion_comentario_multilinea(t):
    '''
    comentarios : COMENTARIO_MULTILINEA
    '''
    t[0] = Comentarios(t[1], t.lineno(1), t.lexpos(1))

# ? declaracion : LET ID IGUAL expresion
# ?             | LET ID
# ?             | LET ID DOSPUNTOS tipo IGUAL expresion
# ?             | LET ID DOSPUNTOS tipo
def p_declaracion(t):
    '''
    declaracion : LET ID IGUAL expresion
    '''
    t[0] = Declaracion(t[2],None, t[4], t.lineno(1), t.lexpos(1))

def p_declaracion_1(t):
    '''
    declaracion : LET ID
    '''
    t[0] = Declaracion(t[2],None, None, t.lineno(1), t.lexpos(1))

def p_declaracion_2(t):
    '''
    declaracion : LET ID DOSPUNTOS tipo IGUAL expresion
    '''
    t[0] = Declaracion(t[2],t[4], t[6], t.lineno(1), t.lexpos(1))

def p_declaracion_3(t):
    '''
    declaracion : LET ID DOSPUNTOS tipo
    '''
    t[0] = Declaracion(t[2],t[4], None, t.lineno(1), t.lexpos(1))

# ? asignacion : ID IGUAL expresion
# ?         | dec
# ?         | inc
def p_asignacion(t):
    '''
    asignacion : ID IGUAL expresion
    '''
    t[0] = Asignacion(t[1], t[3], t.lineno(1), t.lexpos(1))

def p_asignacion_1(t):
    '''
    asignacion : dec
    '''
    t[0] = t[1]

def p_asignacion_2(t):
    '''
    asignacion : inc
    '''
    t[0] = t[1]

# ? dec : ID DECREMENTO
# ?     | DECREMENTO ID
def p_dec(t):
    '''
    dec : ID DECREMENTO
    '''
    t[0] = Dec(t[1],"postDec", t.lineno(1), t.lexpos(1))

def p_dec_1(t):
    '''
    dec : DECREMENTO ID
    '''
    t[0] = Dec(t[2],"preDec", t.lineno(1), t.lexpos(1))

# ? inc : ID INCREMENTO
# ?     | INCREMENTO ID
def p_inc(t):
    '''
    inc : ID INCREMENTO
    '''
    t[0] = Inc(t[1],"postInc", t.lineno(1), t.lexpos(1))

def p_inc_1(t):
    '''
    inc : INCREMENTO ID
    '''
    t[0] = Inc(t[2],"preInc", t.lineno(1), t.lexpos(1))

# ? impresion : CONSOLE PUNTO LOG PARIZQ expresion PARDER
def p_impresion(t):
    '''
    impresion : CONSOLE PUNTO LOG PARIZQ expresion PARDER
    '''
    t[0] = Consolelog(t[5], t.lineno(1), t.lexpos(1))

# ? condicional : IF PARIZQ expresion PARDER bloque
# ?             | IF PARIZQ expresion PARDER bloque ELSE bloque
# ?             | IF PARIZQ expresion PARDER bloque lista_elif
# ?             | IF PARIZQ expresion PARDER bloque lista_elif ELSE bloque

def p_condicional(t):
    '''
    condicional : IF PARIZQ expresion PARDER bloque
    '''
    t[0] = If(t[3], t[5], None, None, t.lineno(1), t.lexpos(1))

def p_condicional_1(t):
    '''
    condicional : IF PARIZQ expresion PARDER bloque ELSE bloque
    '''
    t[0] = If(t[3], t[5], None, t[7], t.lineno(1), t.lexpos(1))

def p_condicional_2(t):
    '''
    condicional : IF PARIZQ expresion PARDER bloque lista_elif
    '''
    t[0] = If(t[3], t[5], t[6], None, t.lineno(1), t.lexpos(1))

def p_condicional_3(t):
    '''
    condicional : IF PARIZQ expresion PARDER bloque lista_elif ELSE bloque
    '''
    t[0] = If(t[3], t[5], t[6], t[8], t.lineno(1), t.lexpos(1))

# ? lista_elif : lista_elif elseif
# ?             | elseif
def p_lista_elif(t):
    '''
    lista_elif : lista_elif elseif
    '''
    t[1].append(t[2])
    t[0] = t[1]

def p_lista_elif_1(t):
    '''
    lista_elif : elseif
    '''
    t[0] = [t[1]]

# ? elseif : ELSE IF PARIZQ expresion PARDER bloque
def p_elseif(t):
    '''
    elseif : ELSE IF PARIZQ expresion PARDER bloque
    '''
    t[0] =If(t[4],t[6],None,None,t.lineno(1),t.lexpos(1))

# ? ciclo_while : WHILE PARIZQ expresion PARDER bloque
def p_ciclo_while(t):
    '''
    ciclo_while : WHILE PARIZQ expresion PARDER bloque
    '''
    t[0] = While(t[3], t[5], t.lineno(1), t.lexpos(1))

# ? ciclo_for : FOR PARIZQ declaracion PTOYCOMA expresion PTOYCOMA asignacion PARDER bloque
# ?             | FOR PARIZQ asignacion PTOYCOMA expresion PTOYCOMA asignacion PARDER bloque
# ?             | FOR PARIZQ asignacion PTOYCOMA expresion PTOYCOMA expresion PARDER bloque
# ?             | FOR PARIZQ declaracion PTOYCOMA expresion PTOYCOMA expresion PARDER bloque
def p_ciclo_for(t):
    '''
    ciclo_for : FOR PARIZQ declaracion PTOYCOMA expresion PTOYCOMA asignacion PARDER bloque
    '''
    t[0] = For(t[3], t[5], t[7], t[9], t.lineno(1), t.lexpos(1))

def p_ciclo_for_1(t):
    '''
    ciclo_for : FOR PARIZQ asignacion PTOYCOMA expresion PTOYCOMA asignacion PARDER bloque
    '''
    t[0] = For(t[3], t[5], t[7], t[9], t.lineno(1), t.lexpos(1))

# ? ciclo_for_of : FOR PARIZQ LET ID OF expresion PARDER bloque
def p_ciclo_for_of(t):
    '''
    ciclo_for_of : FOR PARIZQ LET ID OF expresion PARDER bloque
    '''
    t[0] = ForOf(t[3], t[5], t[6], t[8], t.lineno(1), t.lexpos(1))

# ? funcion : FUNCTION ID PARIZQ lista_parametros PARDER bloque
# ?     | FUNCTION ID PARIZQ lista_parametros PARDER DOSPUNTOS tipo bloque
# ?     | FUNCTION ID PARIZQ PARDER bloque
# ?     | FUNCTION ID PARIZQ PARDER DOSPUNTOS tipo bloque
def p_funcion(t):
    '''
    funcion : FUNCTION ID PARIZQ lista_parametros PARDER bloque
    '''

def p_funcion_1(t):
    '''
    funcion : FUNCTION ID PARIZQ lista_parametros PARDER DOSPUNTOS tipo bloque
    '''

def p_funcion_2(t):
    '''
    funcion : FUNCTION ID PARIZQ PARDER bloque
    '''

def p_funcion_3(t):
    '''
    funcion : FUNCTION ID PARIZQ PARDER DOSPUNTOS tipo bloque
    '''

# ? lista_parametros : lista_parametros COMA ID DOSPUNTOS tipo
# ?                  | ID DOSPUNTOS tipo
def p_lista_parametros(t):
    '''
    lista_parametros : lista_parametros COMA ID DOSPUNTOS tipo
    '''

def p_lista_parametros_1(t):
    '''
    lista_parametros : ID DOSPUNTOS tipo
    '''

# ? llamada_funcion : ID PARIZQ lista_argumentos PARDER
# ?                 | ID PARIZQ PARDER
def p_llamada_funcion(t):
    '''
    llamada_funcion : ID PARIZQ lista_argumentos PARDER
    '''

def p_llamada_funcion_1(t):
    '''
    llamada_funcion : ID PARIZQ PARDER
    '''

# ? lista_argumentos : lista_argumentos COMA expresion
# ?                  | expresion
def p_lista_argumentos(t):
    '''
    lista_argumentos : lista_argumentos COMA expresion
    '''

def p_lista_argumentos_1(t):
    '''
    lista_argumentos : expresion
    '''

# ? tipo : NUMBER
# ?     | STRING
# ?     | BOOLEAN
# ?     | ANY
def p_tipo(t):
    '''
    tipo : NUMBER
    '''
    t[0] = TIPO_DATO.NUMERO

def p_tipo_1(t):
    '''
    tipo : STRING
    '''
    t[0] = TIPO_DATO.CADENA

def p_tipo_2(t):
    '''
    tipo : BOOLEAN
    '''
    t[0] = TIPO_DATO.BOOLEANO

def p_tipo_3(t):
    '''
    tipo : ANY
    '''
    t[0] = TIPO_DATO.ANY

# ? expresion : expresion MAS expresion
# ?             | expresion MENOS expresion
# ?             | expresion POR expresion
# ?             | expresion DIVIDIDO expresion
# ?             | expresion MODULO expresion
# ?             | expresion POTENCIA expresion
# ?             | MENOS expresion %prec UMENOS
# ?             | expresion MENOR expresion
# ?             | expresion MAYOR expresion
# ?             | expresion MENORIGUAL expresion
# ?             | expresion MAYORIGUAL expresion
# ?             | expresion IGUALACION expresion
# ?             | expresion DISTINTO expresion
# ?             | expresion AND expresion
# ?             | expresion OR expresion
# ?             | NOT expresion
# ?             | dec
# ?             | inc
# ?             | funciones_nativas
# ?             | casteo
# ?             | PARIZQ expresion PARDER
# ?             | ENTERO
# ?             | DECIMAL
# ?             | CADENA
# ?             | booleano
# ?             | ID
def p_expresion_aritmetica(t):
    '''
    expresion : expresion MAS expresion
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion DIVIDIDO expresion
            | expresion MODULO expresion
            | expresion POTENCIA expresion
            | MENOS expresion %prec UMENOS
    '''
    if len(t) == 3:
        t[0] = Operacion(t[2], None, TIPO_OPERACION_ARITMETICA.NEGATIVO, t.lineno(1), t.lexpos(1),True)
    elif t[2] == '+':
        print("entro a suma")
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

def p_expresion_incdecremento(t):
    '''
    expresion : dec
            | inc
    '''
    t[0] = t[1]

def p_expresion_funciones_nativas(t):
    '''
    expresion : funciones_nativas
    '''
    t[0] = t[1]

def p_expresion_casteo(t):
    '''
    expresion : casteo
    '''
    t[0] = t[1]

def p_expresion_parentesis(t):
    '''
    expresion : PARIZQ expresion PARDER
    '''
    t[0] = t[2]

def p_expresion_primitiva(t):
    '''
    expresion : ENTERO
            | DECIMAL
            | CADENA
    '''

    if t.slice[1].type == 'ENTERO':
        t[0] = Primitivo(TIPO_DATO.NUMERO, t[1], t.lineno(1), t.lexpos(1))
    elif t.slice[1].type == 'DECIMAL':
        t[0] = Primitivo(TIPO_DATO.NUMERO, t[1], t.lineno(1), t.lexpos(1))
    elif t.slice[1].type == 'CADENA':
        t[0] = Primitivo(TIPO_DATO.CADENA, t[1], t.lineno(1), t.lexpos(1))

def p_expresion_booleana(t):
    '''
    expresion : booleano
    '''
    t[0] = t[1]

def p_expresion_identificador(t):
    '''
    expresion : ID
    '''
    t[0] = Identificador(t[1], t.lineno(1), t.lexpos(1))

# ? booleano : TRUE
# ?         | FALSE

def p_booleano(t):
    '''
    booleano : TRUE
            | FALSE
    '''
    if t.slice[1].type == 'TRUE':
        t[0] = Primitivo(TIPO_DATO.BOOLEANO, True, t.lineno(1), t.lexpos(1))
    elif t.slice[1].type == 'FALSE':
        t[0] = Primitivo(TIPO_DATO.BOOLEANO, False, t.lineno(1), t.lexpos(1))

# ? funciones_nativas : aproximacion
# ?                   | exponencial
# ?                   | to_mayusculas
# ?                   | to_minusculas
# ?                   | separador
# ?                   | concatenacion
def p_funciones_nativas(t):
    '''
    funciones_nativas : aproximacion
                    | exponencial
                    | to_mayusculas
                    | to_minusculas
                    | separador
                    | concatenacion
    '''
    t[0] = t[1]

# ? aproximacion : expresion PUNTO TOFIXED PARIZQ expresion PARDER
def p_aproximacion(t):
    '''
    aproximacion : expresion PUNTO TOFIXED PARIZQ expresion PARDER
    '''
    t[0] = ToFixed(t[1], t[5], t.lineno(1), t.lexpos(1))

# ? exponencial : expresion PUNTO TOEXPONENTIAL PARIZQ expresion PARDER
def p_exponencial(t):
    '''
    exponencial : expresion PUNTO TOEXPONENTIAL PARIZQ expresion PARDER
    '''
    t[0] = ToExponential(t[1], t[5], t.lineno(1), t.lexpos(1))

# ? to_mayusculas : expresion PUNTO TOUPPERCASE PARIZQ PARDER
def p_to_mayusculas(t):
    '''
    to_mayusculas : expresion PUNTO TOUPPERCASE PARIZQ PARDER
    '''
    t[0] = ToUpperCase(t[1], t.lineno(1), t.lexpos(1))

# ? to_minusculas : expresion PUNTO TOLOWERCASE PARIZQ PARDER
def p_to_minusculas(t):
    '''
    to_minusculas : expresion PUNTO TOLOWERCASE PARIZQ PARDER
    '''
    t[0] = ToLowerCase(t[1], t.lineno(1), t.lexpos(1))

# ? separador : expresion PUNTO SPLIT PARIZQ expresion PARDER
def p_separador(t):
    '''
    separador : expresion PUNTO SPLIT PARIZQ expresion PARDER
    '''
    t[0] = Split(t[1], t[5], t.lineno(1), t.lexpos(1))

# ? concatenacion : expresion PUNTO CONCAT PARIZQ expresion PARDER
def p_concatenacion(t):
    '''
    concatenacion : expresion PUNTO CONCAT PARIZQ expresion PARDER
    '''
    t[0] = Concat(t[1], t[5], t.lineno(1), t.lexpos(1))

# ? casteo : expresion PUNTO TOSTRING PARIZQ PARDER
# ?        | CAST_STRING PARIZQ expresion PARDER
def p_casteo(t):
    '''
    casteo : expresion PUNTO TOSTRING PARIZQ PARDER
    '''
    t[0] = ToString(t[1], t.lineno(1), t.lexpos(1))

def p_casteo_1(t):
    '''
    casteo : CAST_STRING PARIZQ expresion PARDER
    '''
    t[0] = ToString(t[3], t.lineno(1), t.lexpos(1))

# ? return : RETURN expresion
# ?        | RETURN
def p_return(t):
    '''
    return : RETURN expresion
            | RETURN
    '''
    if len(t) == 2: 
        t[0] = Return(None, t.lineno(1), t.lexpos(1));
    else:
        t[0] = Return(t[2], t.lineno(1), t.lexpos(1));

# ? break : BREAK
def p_break(t):
    '''
    break : BREAK
    '''
    t[0] = Break(t.lineno(1), t.lexpos(1))

# ? continue : CONTINUE
def p_continue(t):
    '''
    continue : CONTINUE
    '''
    t[0] = Continue(t.lineno(1), t.lexpos(1))


#errores sintacticos
def p_error_inst(t):
    '''
    instruccion : error PTOYCOMA
    '''
    t[0] = -1
    print(str(t[1].value))
    s = SingletonErrores.getInstance()
    s.addError(Error(str(t.lineno(1)), str(f_columna(entrada, t.slice[1])) , "Error Sintáctico", "No se esperaba " + str(t[1].value) + " en esa posición") )
    
def p_error(t):
    s = SingletonErrores.getInstance()
    s.addError(Error("str(t.lineno(1))", "str(t.lexpos(1))" , "Error Sintáctico", "No se esperaba " + "str(t.value)" + " en esa posición") )
    print("Error sintáctico")

import ply.yacc as yacc

parser = yacc.yacc()

def parse(input) :
    global entrada
    entrada = input
    return parser.parse(input)

