
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDnonassocMAYORMENORIGUALMENORMAYORIGUALIGUALACIONDISTINTOleftMASMENOSleftPORDIVIDIDOMODULOrightNOTUMENOSAND ANY ARRAY BOOLEAN BREAK CADENA COMA CONCAT CONSOLE CONTINUE CORDER CORIZQ DECIMAL DECREMENTO DISTINTO DIVIDIDO DOSPUNTOS ELSE ENTERO FALSE FOR FUNCTION ID IF IGUAL IGUALACION INTERFACE LET LLADER LLAIZQ LOG MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MODULO NOT NULL NUMBER OF OR PARDER PARIZQ POR POTENCIA PTOYCOMA PUNTO RETURN SPLIT STRING TOEXPONENTIAL TOFIXED TOLOWERCASE TOSTRING TOUPPERCASE TRUE WHILE\n    instrucciones : instrucciones instruccion\n    \n    instrucciones : instruccion\n    \n    instruccion : instruccion2 PTOYCOMA\n                | instruccion2\n    \n    instruccion3 : instruccion3 instruccion2\n    \n    instruccion3 : instruccion3 instruccion2 PTOYCOMA\n    \n    instruccion3 : instruccion2\n    \n    instruccion3 : instruccion2 PTOYCOMA\n    \n    bloque : LLAIZQ instruccion3 LLADER\n    \n    bloque : LLAIZQ LLADER\n    \n    instruccion2 : declaracion\n                 | asignacion\n                 | impresion\n                 | return\n                 | break\n                 | continue\n                 | condicional_if\n                 | ciclo_while\n                 | ciclo_for\n                 | ciclo_for_of\n    \n    declaracion : LET ID DOSPUNTOS tipo IGUAL expresion\n    \n    declaracion : LET ID IGUAL expresion\n    \n    asignacion : ID IGUAL expresion\n    \n    impresion : CONSOLE PUNTO LOG PARIZQ expresion PARDER\n    \n    expresion : expresion MAS expresion\n            | expresion MENOS expresion\n            | expresion POR expresion\n            | expresion DIVIDIDO expresion\n            | expresion POTENCIA expresion\n            | expresion MODULO expresion\n            | MENOS expresion %prec UMENOS\n            | PARIZQ expresion PARDER\n    \n    expresion : expresion MAYOR expresion\n            | expresion MENOR expresion\n            | expresion MAYORIGUAL expresion\n            | expresion MENORIGUAL expresion\n            | expresion IGUALACION expresion\n            | expresion DISTINTO expresion\n    \n    expresion : expresion AND expresion\n            | expresion OR expresion\n            | NOT expresion\n    \n    expresion : ENTERO\n            | DECIMAL\n            | CADENA\n            | ID\n            | TRUE\n            | FALSE\n    \n    expresion : ID MAS MAS\n            | ID DECREMENTO\n            | MAS MAS ID\n            | DECREMENTO ID\n    \n    expresion : aproximacion\n            | exponencial\n            | to_string\n            | to_minusculas\n            | to_mayusculas\n            | separador\n            | concatenacion\n    \n    aproximacion : expresion PUNTO TOFIXED PARIZQ expresion PARDER\n    \n    exponencial : expresion PUNTO TOEXPONENTIAL PARIZQ expresion PARDER\n    \n    to_string : expresion PUNTO TOSTRING PARIZQ PARDER\n    \n    to_minusculas : expresion PUNTO TOLOWERCASE PARIZQ PARDER\n    \n    to_mayusculas : expresion PUNTO TOUPPERCASE PARIZQ PARDER\n    \n    separador : expresion PUNTO SPLIT PARIZQ expresion PARDER\n    \n    concatenacion : expresion PUNTO CONCAT PARIZQ expresion PARDER\n    \n    tipo : NUMBER\n        | STRING\n        | BOOLEAN\n        | ANY\n    \n    return : RETURN\n           | RETURN expresion\n    \n    continue : CONTINUE\n    \n    break : BREAK\n    \n    condicional_if : IF PARIZQ expresion PARDER bloque\n    \n    condicional_if : IF PARIZQ expresion PARDER bloque ELSE bloque\n    \n    condicional_if : IF PARIZQ expresion PARDER bloque lista_elif\n    \n    condicional_if : IF PARIZQ expresion PARDER bloque lista_elif ELSE bloque\n    \n    lista_elif : lista_elif elif\n    \n    lista_elif : elif\n    \n    elif : ELSE IF PARIZQ expresion PARDER bloque\n    \n    ciclo_while : WHILE PARIZQ expresion PARDER bloque\n    \n    ciclo_for : FOR PARIZQ declaracion PTOYCOMA expresion PTOYCOMA asignacion PARDER bloque\n    \n    ciclo_for : FOR PARIZQ asignacion PTOYCOMA expresion PTOYCOMA asignacion PARDER bloque\n    \n    ciclo_for : FOR PARIZQ declaracion PTOYCOMA expresion PTOYCOMA expresion PARDER bloque\n    \n    ciclo_for : FOR PARIZQ asignacion PTOYCOMA expresion PTOYCOMA expresion PARDER bloque\n    \n    ciclo_for_of : FOR PARIZQ LET ID OF expresion PARDER bloque\n    \n    instruccion : error PTOYCOMA\n    '
    
_lr_action_items = {'error':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,18,19,20,24,25,26,30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,74,76,77,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,128,130,134,135,138,139,140,144,145,147,152,153,154,155,157,159,160,170,176,178,179,180,181,183,],[4,4,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-70,-73,-72,-1,-3,-87,-71,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,-23,-31,-41,-49,-51,-22,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,-74,-81,-21,-24,-61,-62,-63,-76,-79,-10,-59,-60,-64,-65,-75,-78,-9,-77,-86,-84,-82,-83,-85,-80,]),'LET':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,18,19,20,24,25,26,30,35,36,37,38,39,40,42,43,44,45,46,47,48,51,54,72,74,76,77,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,128,129,130,134,135,138,139,140,144,145,146,147,148,152,153,154,155,157,159,160,161,162,170,171,176,178,179,180,181,183,],[15,15,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-70,-73,-72,-1,-3,-87,-71,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,82,-23,-31,-41,-49,-51,-22,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,-74,15,-81,-21,-24,-61,-62,-63,-76,-79,15,-10,-7,-59,-60,-64,-65,-75,-78,-9,-5,-8,-77,-6,-86,-84,-82,-83,-85,-80,]),'ID':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,18,19,20,24,25,26,28,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,76,77,82,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,116,117,119,121,122,126,127,128,129,130,133,134,135,138,139,140,144,145,146,147,148,149,150,152,153,154,155,157,159,160,161,162,169,170,171,176,178,179,180,181,183,],[16,16,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,27,38,-73,-72,-1,-3,-87,38,-71,38,38,38,-42,-43,-44,-45,-46,-47,77,-52,-53,-54,-55,-56,-57,-58,38,38,16,38,-23,38,38,38,38,38,38,38,38,38,38,38,38,38,38,111,-31,-41,-49,-51,118,-22,38,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,38,38,38,38,38,38,38,-74,16,-81,38,-21,-24,-61,-62,-63,-76,-79,16,-10,-7,165,165,-59,-60,-64,-65,-75,-78,-9,-5,-8,38,-77,-6,-86,-84,-82,-83,-85,-80,]),'CONSOLE':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,18,19,20,24,25,26,30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,74,76,77,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,128,129,130,134,135,138,139,140,144,145,146,147,148,152,153,154,155,157,159,160,161,162,170,171,176,178,179,180,181,183,],[17,17,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-70,-73,-72,-1,-3,-87,-71,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,-23,-31,-41,-49,-51,-22,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,-74,17,-81,-21,-24,-61,-62,-63,-76,-79,17,-10,-7,-59,-60,-64,-65,-75,-78,-9,-5,-8,-77,-6,-86,-84,-82,-83,-85,-80,]),'RETURN':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,18,19,20,24,25,26,30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,74,76,77,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,128,129,130,134,135,138,139,140,144,145,146,147,148,152,153,154,155,157,159,160,161,162,170,171,176,178,179,180,181,183,],[18,18,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-70,-73,-72,-1,-3,-87,-71,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,-23,-31,-41,-49,-51,-22,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,-74,18,-81,-21,-24,-61,-62,-63,-76,-79,18,-10,-7,-59,-60,-64,-65,-75,-78,-9,-5,-8,-77,-6,-86,-84,-82,-83,-85,-80,]),'BREAK':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,18,19,20,24,25,26,30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,74,76,77,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,128,129,130,134,135,138,139,140,144,145,146,147,148,152,153,154,155,157,159,160,161,162,170,171,176,178,179,180,181,183,],[19,19,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-70,-73,-72,-1,-3,-87,-71,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,-23,-31,-41,-49,-51,-22,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,-74,19,-81,-21,-24,-61,-62,-63,-76,-79,19,-10,-7,-59,-60,-64,-65,-75,-78,-9,-5,-8,-77,-6,-86,-84,-82,-83,-85,-80,]),'CONTINUE':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,18,19,20,24,25,26,30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,74,76,77,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,128,129,130,134,135,138,139,140,144,145,146,147,148,152,153,154,155,157,159,160,161,162,170,171,176,178,179,180,181,183,],[20,20,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-70,-73,-72,-1,-3,-87,-71,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,-23,-31,-41,-49,-51,-22,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,-74,20,-81,-21,-24,-61,-62,-63,-76,-79,20,-10,-7,-59,-60,-64,-65,-75,-78,-9,-5,-8,-77,-6,-86,-84,-82,-83,-85,-80,]),'IF':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,18,19,20,24,25,26,30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,74,76,77,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,128,129,130,134,135,138,139,140,143,144,145,146,147,148,152,153,154,155,157,158,159,160,161,162,170,171,176,178,179,180,181,183,],[21,21,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-70,-73,-72,-1,-3,-87,-71,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,-23,-31,-41,-49,-51,-22,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,-74,21,-81,-21,-24,-61,-62,-63,156,-76,-79,21,-10,-7,-59,-60,-64,-65,-75,156,-78,-9,-5,-8,-77,-6,-86,-84,-82,-83,-85,-80,]),'WHILE':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,18,19,20,24,25,26,30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,74,76,77,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,128,129,130,134,135,138,139,140,144,145,146,147,148,152,153,154,155,157,159,160,161,162,170,171,176,178,179,180,181,183,],[22,22,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-70,-73,-72,-1,-3,-87,-71,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,-23,-31,-41,-49,-51,-22,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,-74,22,-81,-21,-24,-61,-62,-63,-76,-79,22,-10,-7,-59,-60,-64,-65,-75,-78,-9,-5,-8,-77,-6,-86,-84,-82,-83,-85,-80,]),'FOR':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,18,19,20,24,25,26,30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,74,76,77,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,128,129,130,134,135,138,139,140,144,145,146,147,148,152,153,154,155,157,159,160,161,162,170,171,176,178,179,180,181,183,],[23,23,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-70,-73,-72,-1,-3,-87,-71,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,-23,-31,-41,-49,-51,-22,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,-74,23,-81,-21,-24,-61,-62,-63,-76,-79,23,-10,-7,-59,-60,-64,-65,-75,-78,-9,-5,-8,-77,-6,-86,-84,-82,-83,-85,-80,]),'$end':([1,2,3,5,6,7,8,9,10,11,12,13,14,18,19,20,24,25,26,30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,74,76,77,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,128,130,134,135,138,139,140,144,145,147,152,153,154,155,157,159,160,170,176,178,179,180,181,183,],[0,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-70,-73,-72,-1,-3,-87,-71,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,-23,-31,-41,-49,-51,-22,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,-74,-81,-21,-24,-61,-62,-63,-76,-79,-10,-59,-60,-64,-65,-75,-78,-9,-77,-86,-84,-82,-83,-85,-80,]),'PTOYCOMA':([3,4,5,6,7,8,9,10,11,12,13,14,18,19,20,30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,74,76,77,80,81,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,128,130,131,132,134,135,138,139,140,144,145,147,148,152,153,154,155,157,159,160,161,170,176,178,179,180,181,183,],[25,26,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-70,-73,-72,-71,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,-23,-31,-41,-49,-51,116,117,-22,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,-74,-81,149,150,-21,-24,-61,-62,-63,-76,-79,-10,162,-59,-60,-64,-65,-75,-78,-9,171,-77,-86,-84,-82,-83,-85,-80,]),'LLADER':([5,6,7,8,9,10,11,12,13,14,18,19,20,30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,74,76,77,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,128,129,130,134,135,138,139,140,144,145,146,147,148,152,153,154,155,157,159,160,161,162,170,171,176,178,179,180,181,183,],[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-70,-73,-72,-71,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,-23,-31,-41,-49,-51,-22,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,-74,147,-81,-21,-24,-61,-62,-63,-76,-79,160,-10,-7,-59,-60,-64,-65,-75,-78,-9,-5,-8,-77,-6,-86,-84,-82,-83,-85,-80,]),'IGUAL':([16,27,83,84,85,86,87,118,165,],[28,53,119,-66,-67,-68,-69,53,28,]),'PUNTO':([17,30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[29,70,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,70,-31,70,-41,-49,-51,70,70,70,-25,-26,-27,-28,70,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,70,70,70,70,70,70,-61,-62,-63,70,70,70,-59,-60,-64,-65,70,-45,70,70,]),'MENOS':([18,28,30,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,53,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,72,73,74,76,77,78,79,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,116,117,119,120,121,122,126,127,131,132,133,134,136,137,138,139,140,141,142,149,150,151,152,153,154,155,163,165,167,169,177,],[32,32,57,32,32,32,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,32,32,32,57,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-31,57,-41,-49,-51,57,57,57,32,-25,-26,-27,-28,57,-30,57,57,57,57,57,57,57,57,-50,-32,-48,32,32,32,57,32,32,32,32,57,57,32,57,57,57,-61,-62,-63,57,57,32,32,57,-59,-60,-64,-65,57,-45,57,32,57,]),'PARIZQ':([18,21,22,23,28,32,33,34,49,50,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,104,105,106,107,108,109,110,116,117,119,121,122,126,127,133,149,150,156,169,],[33,49,50,51,33,33,33,33,33,33,33,89,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,121,122,123,124,125,126,127,33,33,33,33,33,33,33,33,33,33,169,33,]),'NOT':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'ENTERO':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'DECIMAL':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'CADENA':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'TRUE':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'FALSE':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'MAS':([18,28,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,53,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,72,73,74,75,76,77,78,79,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,116,117,119,120,121,122,126,127,131,132,133,134,136,137,138,139,140,141,142,149,150,151,152,153,154,155,163,165,167,169,177,],[31,31,56,71,31,31,31,-42,-43,-44,75,-46,-47,-52,-53,-54,-55,-56,-57,-58,31,31,31,56,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-31,56,-41,113,-49,-51,56,56,56,31,-25,-26,-27,-28,56,-30,56,56,56,56,56,56,56,56,-50,-32,-48,31,31,31,56,31,31,31,31,56,56,31,56,56,56,-61,-62,-63,56,56,31,31,56,-59,-60,-64,-65,56,75,56,31,56,]),'DECREMENTO':([18,28,32,33,34,38,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,165,169,],[41,41,41,41,41,76,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,76,41,]),'DOSPUNTOS':([27,118,],[52,52,]),'LOG':([29,],[55,]),'POR':([30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[58,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,58,-31,58,-41,-49,-51,58,58,58,58,58,-27,-28,58,-30,58,58,58,58,58,58,58,58,-50,-32,-48,58,58,58,58,58,58,-61,-62,-63,58,58,58,-59,-60,-64,-65,58,-45,58,58,]),'DIVIDIDO':([30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[59,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,59,-31,59,-41,-49,-51,59,59,59,59,59,-27,-28,59,-30,59,59,59,59,59,59,59,59,-50,-32,-48,59,59,59,59,59,59,-61,-62,-63,59,59,59,-59,-60,-64,-65,59,-45,59,59,]),'POTENCIA':([30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[60,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,60,-31,60,-41,-49,-51,60,60,60,-25,-26,-27,-28,60,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,60,60,60,60,60,60,-61,-62,-63,60,60,60,-59,-60,-64,-65,60,-45,60,60,]),'MODULO':([30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[61,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,61,-31,61,-41,-49,-51,61,61,61,61,61,-27,-28,61,-30,61,61,61,61,61,61,61,61,-50,-32,-48,61,61,61,61,61,61,-61,-62,-63,61,61,61,-59,-60,-64,-65,61,-45,61,61,]),'MAYOR':([30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[62,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,62,-31,62,-41,-49,-51,62,62,62,-25,-26,-27,-28,62,-30,None,None,None,None,None,None,62,62,-50,-32,-48,62,62,62,62,62,62,-61,-62,-63,62,62,62,-59,-60,-64,-65,62,-45,62,62,]),'MENOR':([30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[63,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,63,-31,63,-41,-49,-51,63,63,63,-25,-26,-27,-28,63,-30,None,None,None,None,None,None,63,63,-50,-32,-48,63,63,63,63,63,63,-61,-62,-63,63,63,63,-59,-60,-64,-65,63,-45,63,63,]),'MAYORIGUAL':([30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[64,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,64,-31,64,-41,-49,-51,64,64,64,-25,-26,-27,-28,64,-30,None,None,None,None,None,None,64,64,-50,-32,-48,64,64,64,64,64,64,-61,-62,-63,64,64,64,-59,-60,-64,-65,64,-45,64,64,]),'MENORIGUAL':([30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[65,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,65,-31,65,-41,-49,-51,65,65,65,-25,-26,-27,-28,65,-30,None,None,None,None,None,None,65,65,-50,-32,-48,65,65,65,65,65,65,-61,-62,-63,65,65,65,-59,-60,-64,-65,65,-45,65,65,]),'IGUALACION':([30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[66,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,66,-31,66,-41,-49,-51,66,66,66,-25,-26,-27,-28,66,-30,None,None,None,None,None,None,66,66,-50,-32,-48,66,66,66,66,66,66,-61,-62,-63,66,66,66,-59,-60,-64,-65,66,-45,66,66,]),'DISTINTO':([30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[67,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,67,-31,67,-41,-49,-51,67,67,67,-25,-26,-27,-28,67,-30,None,None,None,None,None,None,67,67,-50,-32,-48,67,67,67,67,67,67,-61,-62,-63,67,67,67,-59,-60,-64,-65,67,-45,67,67,]),'AND':([30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[68,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,68,-31,68,-41,-49,-51,68,68,68,-25,-26,-27,-28,68,-30,-33,-34,-35,-36,-37,-38,-39,68,-50,-32,-48,68,68,68,68,68,68,-61,-62,-63,68,68,68,-59,-60,-64,-65,68,-45,68,68,]),'OR':([30,35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,131,132,134,136,137,138,139,140,141,142,151,152,153,154,155,163,165,167,177,],[69,-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,69,-31,69,-41,-49,-51,69,69,69,-25,-26,-27,-28,69,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,69,69,69,69,69,69,-61,-62,-63,69,69,69,-59,-60,-64,-65,69,-45,69,69,]),'PARDER':([35,36,37,38,39,40,42,43,44,45,46,47,48,54,72,73,74,76,77,78,79,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,120,123,124,125,136,137,138,139,140,141,142,151,152,153,154,155,163,164,165,166,167,177,],[-42,-43,-44,-45,-46,-47,-52,-53,-54,-55,-56,-57,-58,-23,-31,112,-41,-49,-51,114,115,-25,-26,-27,-28,-29,-30,-33,-34,-35,-36,-37,-38,-39,-40,-50,-32,-48,135,138,139,140,152,153,-61,-62,-63,154,155,168,-59,-60,-64,-65,172,173,-45,174,175,182,]),'NUMBER':([52,],[84,]),'STRING':([52,],[85,]),'BOOLEAN':([52,],[86,]),'ANY':([52,],[87,]),'TOFIXED':([70,],[104,]),'TOEXPONENTIAL':([70,],[105,]),'TOSTRING':([70,],[106,]),'TOLOWERCASE':([70,],[107,]),'TOUPPERCASE':([70,],[108,]),'SPLIT':([70,],[109,]),'CONCAT':([70,],[110,]),'LLAIZQ':([114,115,143,158,168,172,173,174,175,182,],[129,129,129,129,129,129,129,129,129,129,]),'OF':([118,],[133,]),'ELSE':([128,144,145,147,159,160,183,],[143,158,-79,-10,-78,-9,-80,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,],[1,]),'instruccion':([0,1,],[2,24,]),'instruccion2':([0,1,129,146,],[3,3,148,161,]),'declaracion':([0,1,51,129,146,],[5,5,80,5,5,]),'asignacion':([0,1,51,129,146,149,150,],[6,6,81,6,6,164,166,]),'impresion':([0,1,129,146,],[7,7,7,7,]),'return':([0,1,129,146,],[8,8,8,8,]),'break':([0,1,129,146,],[9,9,9,9,]),'continue':([0,1,129,146,],[10,10,10,10,]),'condicional_if':([0,1,129,146,],[11,11,11,11,]),'ciclo_while':([0,1,129,146,],[12,12,12,12,]),'ciclo_for':([0,1,129,146,],[13,13,13,13,]),'ciclo_for_of':([0,1,129,146,],[14,14,14,14,]),'expresion':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[30,54,72,73,74,78,79,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,120,131,132,134,136,137,141,142,151,163,167,177,]),'aproximacion':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'exponencial':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'to_string':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'to_minusculas':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'to_mayusculas':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'separador':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'concatenacion':([18,28,32,33,34,49,50,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,89,116,117,119,121,122,126,127,133,149,150,169,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'tipo':([52,],[83,]),'bloque':([114,115,143,158,168,172,173,174,175,182,],[128,130,157,170,176,178,179,180,181,183,]),'lista_elif':([128,],[144,]),'elif':([128,144,],[145,159,]),'instruccion3':([129,],[146,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',223),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',231),
  ('instruccion -> instruccion2 PTOYCOMA','instruccion',2,'p_instruccion','gramatica.py',239),
  ('instruccion -> instruccion2','instruccion',1,'p_instruccion','gramatica.py',240),
  ('instruccion3 -> instruccion3 instruccion2','instruccion3',2,'p_instruccion3','gramatica.py',247),
  ('instruccion3 -> instruccion3 instruccion2 PTOYCOMA','instruccion3',3,'p_instruccion3_ptcoma','gramatica.py',255),
  ('instruccion3 -> instruccion2','instruccion3',1,'p_instruccion3_instruccion2','gramatica.py',263),
  ('instruccion3 -> instruccion2 PTOYCOMA','instruccion3',2,'p_instruccion3_instruccion2_ptcoma','gramatica.py',270),
  ('bloque -> LLAIZQ instruccion3 LLADER','bloque',3,'p_bloque','gramatica.py',277),
  ('bloque -> LLAIZQ LLADER','bloque',2,'p_bloque2','gramatica.py',284),
  ('instruccion2 -> declaracion','instruccion2',1,'p_instruccion2','gramatica.py',301),
  ('instruccion2 -> asignacion','instruccion2',1,'p_instruccion2','gramatica.py',302),
  ('instruccion2 -> impresion','instruccion2',1,'p_instruccion2','gramatica.py',303),
  ('instruccion2 -> return','instruccion2',1,'p_instruccion2','gramatica.py',304),
  ('instruccion2 -> break','instruccion2',1,'p_instruccion2','gramatica.py',305),
  ('instruccion2 -> continue','instruccion2',1,'p_instruccion2','gramatica.py',306),
  ('instruccion2 -> condicional_if','instruccion2',1,'p_instruccion2','gramatica.py',307),
  ('instruccion2 -> ciclo_while','instruccion2',1,'p_instruccion2','gramatica.py',308),
  ('instruccion2 -> ciclo_for','instruccion2',1,'p_instruccion2','gramatica.py',309),
  ('instruccion2 -> ciclo_for_of','instruccion2',1,'p_instruccion2','gramatica.py',310),
  ('declaracion -> LET ID DOSPUNTOS tipo IGUAL expresion','declaracion',6,'p_declaracion1','gramatica.py',317),
  ('declaracion -> LET ID IGUAL expresion','declaracion',4,'p_declaracion2','gramatica.py',325),
  ('asignacion -> ID IGUAL expresion','asignacion',3,'p_asignacion','gramatica.py',333),
  ('impresion -> CONSOLE PUNTO LOG PARIZQ expresion PARDER','impresion',6,'p_impresion','gramatica.py',340),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',354),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',355),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',356),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',357),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',358),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',359),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_aritmetica','gramatica.py',360),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_aritmetica','gramatica.py',361),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_relacional','gramatica.py',389),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion_relacional','gramatica.py',390),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',391),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',392),
  ('expresion -> expresion IGUALACION expresion','expresion',3,'p_expresion_relacional','gramatica.py',393),
  ('expresion -> expresion DISTINTO expresion','expresion',3,'p_expresion_relacional','gramatica.py',394),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_logica','gramatica.py',416),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_logica','gramatica.py',417),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_logica','gramatica.py',418),
  ('expresion -> ENTERO','expresion',1,'p_expresion_primitiva','gramatica.py',437),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_primitiva','gramatica.py',438),
  ('expresion -> CADENA','expresion',1,'p_expresion_primitiva','gramatica.py',439),
  ('expresion -> ID','expresion',1,'p_expresion_primitiva','gramatica.py',440),
  ('expresion -> TRUE','expresion',1,'p_expresion_primitiva','gramatica.py',441),
  ('expresion -> FALSE','expresion',1,'p_expresion_primitiva','gramatica.py',442),
  ('expresion -> ID MAS MAS','expresion',3,'p_expresion_incremento_decremento','gramatica.py',466),
  ('expresion -> ID DECREMENTO','expresion',2,'p_expresion_incremento_decremento','gramatica.py',467),
  ('expresion -> MAS MAS ID','expresion',3,'p_expresion_incremento_decremento','gramatica.py',468),
  ('expresion -> DECREMENTO ID','expresion',2,'p_expresion_incremento_decremento','gramatica.py',469),
  ('expresion -> aproximacion','expresion',1,'p_expresion_nativa','gramatica.py',492),
  ('expresion -> exponencial','expresion',1,'p_expresion_nativa','gramatica.py',493),
  ('expresion -> to_string','expresion',1,'p_expresion_nativa','gramatica.py',494),
  ('expresion -> to_minusculas','expresion',1,'p_expresion_nativa','gramatica.py',495),
  ('expresion -> to_mayusculas','expresion',1,'p_expresion_nativa','gramatica.py',496),
  ('expresion -> separador','expresion',1,'p_expresion_nativa','gramatica.py',497),
  ('expresion -> concatenacion','expresion',1,'p_expresion_nativa','gramatica.py',498),
  ('aproximacion -> expresion PUNTO TOFIXED PARIZQ expresion PARDER','aproximacion',6,'p_aproximacion','gramatica.py',505),
  ('exponencial -> expresion PUNTO TOEXPONENTIAL PARIZQ expresion PARDER','exponencial',6,'p_exponencial','gramatica.py',512),
  ('to_string -> expresion PUNTO TOSTRING PARIZQ PARDER','to_string',5,'p_to_string','gramatica.py',519),
  ('to_minusculas -> expresion PUNTO TOLOWERCASE PARIZQ PARDER','to_minusculas',5,'p_to_minusculas','gramatica.py',526),
  ('to_mayusculas -> expresion PUNTO TOUPPERCASE PARIZQ PARDER','to_mayusculas',5,'p_to_mayusculas','gramatica.py',533),
  ('separador -> expresion PUNTO SPLIT PARIZQ expresion PARDER','separador',6,'p_separador','gramatica.py',540),
  ('concatenacion -> expresion PUNTO CONCAT PARIZQ expresion PARDER','concatenacion',6,'p_concatenacion','gramatica.py',547),
  ('tipo -> NUMBER','tipo',1,'p_tipo','gramatica.py',559),
  ('tipo -> STRING','tipo',1,'p_tipo','gramatica.py',560),
  ('tipo -> BOOLEAN','tipo',1,'p_tipo','gramatica.py',561),
  ('tipo -> ANY','tipo',1,'p_tipo','gramatica.py',562),
  ('return -> RETURN','return',1,'p_retorno','gramatica.py',578),
  ('return -> RETURN expresion','return',2,'p_retorno','gramatica.py',579),
  ('continue -> CONTINUE','continue',1,'p_continue','gramatica.py',589),
  ('break -> BREAK','break',1,'p_break','gramatica.py',596),
  ('condicional_if -> IF PARIZQ expresion PARDER bloque','condicional_if',5,'p_condicional_if','gramatica.py',603),
  ('condicional_if -> IF PARIZQ expresion PARDER bloque ELSE bloque','condicional_if',7,'p_condicional_if_else','gramatica.py',609),
  ('condicional_if -> IF PARIZQ expresion PARDER bloque lista_elif','condicional_if',6,'p_condicional_if_elif','gramatica.py',616),
  ('condicional_if -> IF PARIZQ expresion PARDER bloque lista_elif ELSE bloque','condicional_if',8,'p_condicional_if_elif_else','gramatica.py',622),
  ('lista_elif -> lista_elif elif','lista_elif',2,'p_lista_elif','gramatica.py',629),
  ('lista_elif -> elif','lista_elif',1,'p_lista_elif_else','gramatica.py',637),
  ('elif -> ELSE IF PARIZQ expresion PARDER bloque','elif',6,'p_lista_elif_elif','gramatica.py',643),
  ('ciclo_while -> WHILE PARIZQ expresion PARDER bloque','ciclo_while',5,'p_ciclo_while','gramatica.py',651),
  ('ciclo_for -> FOR PARIZQ declaracion PTOYCOMA expresion PTOYCOMA asignacion PARDER bloque','ciclo_for',9,'p_ciclo_for','gramatica.py',658),
  ('ciclo_for -> FOR PARIZQ asignacion PTOYCOMA expresion PTOYCOMA asignacion PARDER bloque','ciclo_for',9,'p_ciclo_for2','gramatica.py',665),
  ('ciclo_for -> FOR PARIZQ declaracion PTOYCOMA expresion PTOYCOMA expresion PARDER bloque','ciclo_for',9,'p_ciclo_for3','gramatica.py',672),
  ('ciclo_for -> FOR PARIZQ asignacion PTOYCOMA expresion PTOYCOMA expresion PARDER bloque','ciclo_for',9,'p_ciclo_for4','gramatica.py',679),
  ('ciclo_for_of -> FOR PARIZQ LET ID OF expresion PARDER bloque','ciclo_for_of',8,'p_ciclo_for_of','gramatica.py',686),
  ('instruccion -> error PTOYCOMA','instruccion',2,'p_error_inst','gramatica.py',695),
]
