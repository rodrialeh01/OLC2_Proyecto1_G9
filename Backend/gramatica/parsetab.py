
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDnonassocMAYORMENORIGUALMENORMAYORIGUALIGUALACIONDISTINTOleftMASMENOSleftPORDIVIDIDOMODULOrightNOTUMENOSAND ANY ARRAY BOOLEAN BREAK CADENA COMA CONCAT CONSOLE CONTINUE CORDER CORIZQ DECREMENTO DISTINTO DIVIDIDO DOSPUNTOS ELSE FALSE FOR FUNCTION ID IF IGUAL IGUALACION INTERFACE LET LLADER LLAIZQ LOG MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MODULO NOT NULL NUMBER NUMERO OF OR PARDER PARIZQ POR POTENCIA PTOYCOMA PUNTO RETURN SPLIT STRING TOEXPONENTIAL TOFIXED TOLOWERCASE TOSTRING TOUPPERCASE TRUE WHILE\n    instrucciones : instrucciones instruccion\n    \n    instrucciones : instruccion\n    \n    instruccion : instruccion2 PTOYCOMA\n                | instruccion2\n    \n    instruccion3 : instruccion3 instruccion2\n    \n    instruccion3 : instruccion3 instruccion2 PTOYCOMA\n    \n    instruccion3 : instruccion2\n    \n    instruccion3 : instruccion2 PTOYCOMA\n    \n    bloque : LLAIZQ instruccion3 LLADER\n    \n    bloque : LLAIZQ LLADER\n    \n    instruccion2 : declaracion\n                 | asignacion\n                 | impresion\n                 | return\n                 | break\n                 | continue\n                 | condicional_if\n                 | ciclo_while\n                 | ciclo_for\n    \n    declaracion : LET ID DOSPUNTOS tipo IGUAL expresion\n    \n    declaracion : LET ID IGUAL expresion\n    \n    asignacion : ID IGUAL expresion\n    \n    impresion : CONSOLE PUNTO LOG PARIZQ expresion PARDER\n    \n    expresion : expresion MAS expresion\n            | expresion MENOS expresion\n            | expresion POR expresion\n            | expresion DIVIDIDO expresion\n            | expresion POTENCIA expresion\n            | expresion MODULO expresion\n            | MENOS expresion %prec UMENOS\n            | PARIZQ expresion PARDER\n    \n    expresion : expresion MAYOR expresion\n            | expresion MENOR expresion\n            | expresion MAYORIGUAL expresion\n            | expresion MENORIGUAL expresion\n            | expresion IGUALACION expresion\n            | expresion DISTINTO expresion\n    \n    expresion : expresion AND expresion\n            | expresion OR expresion\n            | NOT expresion\n    \n    expresion : NUMERO\n            | CADENA\n            | ID\n            | TRUE\n            | FALSE\n    \n    expresion : ID MAS MAS\n            | ID DECREMENTO\n            | MAS MAS ID\n            | DECREMENTO ID\n    \n    tipo : NUMBER\n        | STRING\n        | BOOLEAN\n        | ANY\n    \n    return : RETURN\n           | RETURN expresion\n    \n    continue : CONTINUE\n    \n    break : BREAK\n    \n    condicional_if : IF PARIZQ expresion PARDER bloque\n    \n    condicional_if : IF PARIZQ expresion PARDER bloque ELSE bloque\n    \n    condicional_if : IF PARIZQ expresion PARDER bloque lista_elif\n    \n    condicional_if : IF PARIZQ expresion PARDER bloque lista_elif ELSE bloque\n    \n    lista_elif : lista_elif elif\n    \n    lista_elif : elif\n    \n    elif : ELSE IF PARIZQ expresion PARDER bloque\n    \n    ciclo_while : WHILE PARIZQ expresion PARDER bloque\n    \n    ciclo_for : FOR PARIZQ declaracion PTOYCOMA expresion PTOYCOMA asignacion PARDER bloque\n    \n    ciclo_for : FOR PARIZQ asignacion PTOYCOMA expresion PTOYCOMA asignacion PARDER bloque\n    \n    ciclo_for : FOR PARIZQ declaracion PTOYCOMA expresion PTOYCOMA expresion PARDER bloque\n    \n    ciclo_for : FOR PARIZQ asignacion PTOYCOMA expresion PTOYCOMA expresion PARDER bloque\n    \n    instruccion : error PTOYCOMA\n    '
    
_lr_action_items = {'error':([0,1,2,3,5,6,7,8,9,10,11,12,13,17,18,19,23,24,25,29,34,35,36,37,38,45,62,64,66,67,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,102,104,107,108,110,111,113,118,120,121,130,137,138,139,140,142,],[4,4,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-54,-57,-56,-1,-3,-70,-55,-41,-42,-43,-44,-45,-22,-30,-40,-47,-49,-21,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,-58,-65,-20,-23,-60,-63,-10,-59,-62,-9,-61,-68,-66,-67,-69,-64,]),'LET':([0,1,2,3,5,6,7,8,9,10,11,12,13,17,18,19,23,24,25,29,34,35,36,37,38,42,45,62,64,66,67,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,102,103,104,107,108,110,111,112,113,114,118,120,121,122,123,130,131,137,138,139,140,142,],[14,14,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-54,-57,-56,-1,-3,-70,-55,-41,-42,-43,-44,-45,14,-22,-30,-40,-47,-49,-21,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,-58,14,-65,-20,-23,-60,-63,14,-10,-7,-59,-62,-9,-5,-8,-61,-6,-68,-66,-67,-69,-64,]),'ID':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,17,18,19,23,24,25,27,29,31,32,33,34,35,36,37,38,39,40,41,42,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,67,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,99,100,102,103,104,107,108,110,111,112,113,114,115,116,118,120,121,122,123,129,130,131,137,138,139,140,142,],[15,15,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,26,36,-57,-56,-1,-3,-70,36,-55,36,36,36,-41,-42,-43,-44,-45,67,36,36,15,36,-22,36,36,36,36,36,36,36,36,36,36,36,36,36,36,93,-30,-40,-47,-49,-21,36,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,36,36,36,-58,15,-65,-20,-23,-60,-63,15,-10,-7,126,126,-59,-62,-9,-5,-8,36,-61,-6,-68,-66,-67,-69,-64,]),'CONSOLE':([0,1,2,3,5,6,7,8,9,10,11,12,13,17,18,19,23,24,25,29,34,35,36,37,38,45,62,64,66,67,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,102,103,104,107,108,110,111,112,113,114,118,120,121,122,123,130,131,137,138,139,140,142,],[16,16,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-54,-57,-56,-1,-3,-70,-55,-41,-42,-43,-44,-45,-22,-30,-40,-47,-49,-21,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,-58,16,-65,-20,-23,-60,-63,16,-10,-7,-59,-62,-9,-5,-8,-61,-6,-68,-66,-67,-69,-64,]),'RETURN':([0,1,2,3,5,6,7,8,9,10,11,12,13,17,18,19,23,24,25,29,34,35,36,37,38,45,62,64,66,67,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,102,103,104,107,108,110,111,112,113,114,118,120,121,122,123,130,131,137,138,139,140,142,],[17,17,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-54,-57,-56,-1,-3,-70,-55,-41,-42,-43,-44,-45,-22,-30,-40,-47,-49,-21,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,-58,17,-65,-20,-23,-60,-63,17,-10,-7,-59,-62,-9,-5,-8,-61,-6,-68,-66,-67,-69,-64,]),'BREAK':([0,1,2,3,5,6,7,8,9,10,11,12,13,17,18,19,23,24,25,29,34,35,36,37,38,45,62,64,66,67,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,102,103,104,107,108,110,111,112,113,114,118,120,121,122,123,130,131,137,138,139,140,142,],[18,18,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-54,-57,-56,-1,-3,-70,-55,-41,-42,-43,-44,-45,-22,-30,-40,-47,-49,-21,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,-58,18,-65,-20,-23,-60,-63,18,-10,-7,-59,-62,-9,-5,-8,-61,-6,-68,-66,-67,-69,-64,]),'CONTINUE':([0,1,2,3,5,6,7,8,9,10,11,12,13,17,18,19,23,24,25,29,34,35,36,37,38,45,62,64,66,67,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,102,103,104,107,108,110,111,112,113,114,118,120,121,122,123,130,131,137,138,139,140,142,],[19,19,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-54,-57,-56,-1,-3,-70,-55,-41,-42,-43,-44,-45,-22,-30,-40,-47,-49,-21,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,-58,19,-65,-20,-23,-60,-63,19,-10,-7,-59,-62,-9,-5,-8,-61,-6,-68,-66,-67,-69,-64,]),'IF':([0,1,2,3,5,6,7,8,9,10,11,12,13,17,18,19,23,24,25,29,34,35,36,37,38,45,62,64,66,67,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,102,103,104,107,108,109,110,111,112,113,114,118,119,120,121,122,123,130,131,137,138,139,140,142,],[20,20,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-54,-57,-56,-1,-3,-70,-55,-41,-42,-43,-44,-45,-22,-30,-40,-47,-49,-21,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,-58,20,-65,-20,-23,117,-60,-63,20,-10,-7,-59,117,-62,-9,-5,-8,-61,-6,-68,-66,-67,-69,-64,]),'WHILE':([0,1,2,3,5,6,7,8,9,10,11,12,13,17,18,19,23,24,25,29,34,35,36,37,38,45,62,64,66,67,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,102,103,104,107,108,110,111,112,113,114,118,120,121,122,123,130,131,137,138,139,140,142,],[21,21,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-54,-57,-56,-1,-3,-70,-55,-41,-42,-43,-44,-45,-22,-30,-40,-47,-49,-21,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,-58,21,-65,-20,-23,-60,-63,21,-10,-7,-59,-62,-9,-5,-8,-61,-6,-68,-66,-67,-69,-64,]),'FOR':([0,1,2,3,5,6,7,8,9,10,11,12,13,17,18,19,23,24,25,29,34,35,36,37,38,45,62,64,66,67,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,102,103,104,107,108,110,111,112,113,114,118,120,121,122,123,130,131,137,138,139,140,142,],[22,22,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-54,-57,-56,-1,-3,-70,-55,-41,-42,-43,-44,-45,-22,-30,-40,-47,-49,-21,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,-58,22,-65,-20,-23,-60,-63,22,-10,-7,-59,-62,-9,-5,-8,-61,-6,-68,-66,-67,-69,-64,]),'$end':([1,2,3,5,6,7,8,9,10,11,12,13,17,18,19,23,24,25,29,34,35,36,37,38,45,62,64,66,67,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,102,104,107,108,110,111,113,118,120,121,130,137,138,139,140,142,],[0,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-19,-54,-57,-56,-1,-3,-70,-55,-41,-42,-43,-44,-45,-22,-30,-40,-47,-49,-21,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,-58,-65,-20,-23,-60,-63,-10,-59,-62,-9,-61,-68,-66,-67,-69,-64,]),'PTOYCOMA':([3,4,5,6,7,8,9,10,11,12,13,17,18,19,29,34,35,36,37,38,45,62,64,66,67,70,71,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,102,104,105,106,107,108,110,111,113,114,118,120,121,122,130,137,138,139,140,142,],[24,25,-11,-12,-13,-14,-15,-16,-17,-18,-19,-54,-57,-56,-55,-41,-42,-43,-44,-45,-22,-30,-40,-47,-49,98,99,-21,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,-58,-65,115,116,-20,-23,-60,-63,-10,123,-59,-62,-9,131,-61,-68,-66,-67,-69,-64,]),'LLADER':([5,6,7,8,9,10,11,12,13,17,18,19,29,34,35,36,37,38,45,62,64,66,67,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,102,103,104,107,108,110,111,112,113,114,118,120,121,122,123,130,131,137,138,139,140,142,],[-11,-12,-13,-14,-15,-16,-17,-18,-19,-54,-57,-56,-55,-41,-42,-43,-44,-45,-22,-30,-40,-47,-49,-21,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,-58,113,-65,-20,-23,-60,-63,121,-10,-7,-59,-62,-9,-5,-8,-61,-6,-68,-66,-67,-69,-64,]),'IGUAL':([15,26,72,73,74,75,76,126,],[27,44,100,-50,-51,-52,-53,27,]),'PUNTO':([16,],[28,]),'MENOS':([17,27,29,31,32,33,34,35,36,37,38,40,41,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,66,67,68,69,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,99,100,101,105,106,107,115,116,124,126,128,129,136,],[31,31,48,31,31,31,-41,-42,-43,-44,-45,31,31,31,48,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-30,48,-40,-47,-49,48,48,48,31,-24,-25,-26,-27,48,-29,48,48,48,48,48,48,48,48,-48,-31,-46,31,31,31,48,48,48,48,31,31,48,-43,48,31,48,]),'PARIZQ':([17,20,21,22,27,31,32,33,40,41,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,78,98,99,100,115,116,117,129,],[32,40,41,42,32,32,32,32,32,32,32,78,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,129,32,]),'NOT':([17,27,31,32,33,40,41,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,78,98,99,100,115,116,129,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'NUMERO':([17,27,31,32,33,40,41,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,78,98,99,100,115,116,129,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'CADENA':([17,27,31,32,33,40,41,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,78,98,99,100,115,116,129,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'TRUE':([17,27,31,32,33,40,41,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,78,98,99,100,115,116,129,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'FALSE':([17,27,31,32,33,40,41,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,78,98,99,100,115,116,129,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'MAS':([17,27,29,30,31,32,33,34,35,36,37,38,40,41,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,68,69,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,99,100,101,105,106,107,115,116,124,126,128,129,136,],[30,30,47,61,30,30,30,-41,-42,65,-44,-45,30,30,30,47,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-30,47,-40,95,-47,-49,47,47,47,30,-24,-25,-26,-27,47,-29,47,47,47,47,47,47,47,47,-48,-31,-46,30,30,30,47,47,47,47,30,30,47,65,47,30,47,]),'DECREMENTO':([17,27,31,32,33,36,40,41,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,78,98,99,100,115,116,126,129,],[39,39,39,39,39,66,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,66,39,]),'DOSPUNTOS':([26,],[43,]),'LOG':([28,],[46,]),'POR':([29,34,35,36,37,38,45,62,63,64,66,67,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,105,106,107,124,126,128,136,],[49,-41,-42,-43,-44,-45,49,-30,49,-40,-47,-49,49,49,49,49,49,-26,-27,49,-29,49,49,49,49,49,49,49,49,-48,-31,-46,49,49,49,49,49,-43,49,49,]),'DIVIDIDO':([29,34,35,36,37,38,45,62,63,64,66,67,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,105,106,107,124,126,128,136,],[50,-41,-42,-43,-44,-45,50,-30,50,-40,-47,-49,50,50,50,50,50,-26,-27,50,-29,50,50,50,50,50,50,50,50,-48,-31,-46,50,50,50,50,50,-43,50,50,]),'POTENCIA':([29,34,35,36,37,38,45,62,63,64,66,67,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,105,106,107,124,126,128,136,],[51,-41,-42,-43,-44,-45,51,-30,51,-40,-47,-49,51,51,51,-24,-25,-26,-27,51,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,51,51,51,51,51,-43,51,51,]),'MODULO':([29,34,35,36,37,38,45,62,63,64,66,67,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,105,106,107,124,126,128,136,],[52,-41,-42,-43,-44,-45,52,-30,52,-40,-47,-49,52,52,52,52,52,-26,-27,52,-29,52,52,52,52,52,52,52,52,-48,-31,-46,52,52,52,52,52,-43,52,52,]),'MAYOR':([29,34,35,36,37,38,45,62,63,64,66,67,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,105,106,107,124,126,128,136,],[53,-41,-42,-43,-44,-45,53,-30,53,-40,-47,-49,53,53,53,-24,-25,-26,-27,53,-29,None,None,None,None,None,None,53,53,-48,-31,-46,53,53,53,53,53,-43,53,53,]),'MENOR':([29,34,35,36,37,38,45,62,63,64,66,67,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,105,106,107,124,126,128,136,],[54,-41,-42,-43,-44,-45,54,-30,54,-40,-47,-49,54,54,54,-24,-25,-26,-27,54,-29,None,None,None,None,None,None,54,54,-48,-31,-46,54,54,54,54,54,-43,54,54,]),'MAYORIGUAL':([29,34,35,36,37,38,45,62,63,64,66,67,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,105,106,107,124,126,128,136,],[55,-41,-42,-43,-44,-45,55,-30,55,-40,-47,-49,55,55,55,-24,-25,-26,-27,55,-29,None,None,None,None,None,None,55,55,-48,-31,-46,55,55,55,55,55,-43,55,55,]),'MENORIGUAL':([29,34,35,36,37,38,45,62,63,64,66,67,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,105,106,107,124,126,128,136,],[56,-41,-42,-43,-44,-45,56,-30,56,-40,-47,-49,56,56,56,-24,-25,-26,-27,56,-29,None,None,None,None,None,None,56,56,-48,-31,-46,56,56,56,56,56,-43,56,56,]),'IGUALACION':([29,34,35,36,37,38,45,62,63,64,66,67,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,105,106,107,124,126,128,136,],[57,-41,-42,-43,-44,-45,57,-30,57,-40,-47,-49,57,57,57,-24,-25,-26,-27,57,-29,None,None,None,None,None,None,57,57,-48,-31,-46,57,57,57,57,57,-43,57,57,]),'DISTINTO':([29,34,35,36,37,38,45,62,63,64,66,67,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,105,106,107,124,126,128,136,],[58,-41,-42,-43,-44,-45,58,-30,58,-40,-47,-49,58,58,58,-24,-25,-26,-27,58,-29,None,None,None,None,None,None,58,58,-48,-31,-46,58,58,58,58,58,-43,58,58,]),'AND':([29,34,35,36,37,38,45,62,63,64,66,67,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,105,106,107,124,126,128,136,],[59,-41,-42,-43,-44,-45,59,-30,59,-40,-47,-49,59,59,59,-24,-25,-26,-27,59,-29,-32,-33,-34,-35,-36,-37,-38,59,-48,-31,-46,59,59,59,59,59,-43,59,59,]),'OR':([29,34,35,36,37,38,45,62,63,64,66,67,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,105,106,107,124,126,128,136,],[60,-41,-42,-43,-44,-45,60,-30,60,-40,-47,-49,60,60,60,-24,-25,-26,-27,60,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,60,60,60,60,60,-43,60,60,]),'PARDER':([34,35,36,37,38,45,62,63,64,66,67,68,69,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,124,125,126,127,128,136,],[-41,-42,-43,-44,-45,-22,-30,94,-40,-47,-49,96,97,-24,-25,-26,-27,-28,-29,-32,-33,-34,-35,-36,-37,-38,-39,-48,-31,-46,108,132,133,-43,134,135,141,]),'NUMBER':([43,],[73,]),'STRING':([43,],[74,]),'BOOLEAN':([43,],[75,]),'ANY':([43,],[76,]),'LLAIZQ':([96,97,109,119,132,133,134,135,141,],[103,103,103,103,103,103,103,103,103,]),'ELSE':([102,110,111,113,120,121,142,],[109,119,-63,-10,-62,-9,-64,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,],[1,]),'instruccion':([0,1,],[2,23,]),'instruccion2':([0,1,103,112,],[3,3,114,122,]),'declaracion':([0,1,42,103,112,],[5,5,70,5,5,]),'asignacion':([0,1,42,103,112,115,116,],[6,6,71,6,6,125,127,]),'impresion':([0,1,103,112,],[7,7,7,7,]),'return':([0,1,103,112,],[8,8,8,8,]),'break':([0,1,103,112,],[9,9,9,9,]),'continue':([0,1,103,112,],[10,10,10,10,]),'condicional_if':([0,1,103,112,],[11,11,11,11,]),'ciclo_while':([0,1,103,112,],[12,12,12,12,]),'ciclo_for':([0,1,103,112,],[13,13,13,13,]),'expresion':([17,27,31,32,33,40,41,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,78,98,99,100,115,116,129,],[29,45,62,63,64,68,69,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,101,105,106,107,124,128,136,]),'tipo':([43,],[72,]),'bloque':([96,97,109,119,132,133,134,135,141,],[102,104,118,130,137,138,139,140,142,]),'lista_elif':([102,],[110,]),'elif':([102,110,],[111,120,]),'instruccion3':([103,],[112,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',206),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',214),
  ('instruccion -> instruccion2 PTOYCOMA','instruccion',2,'p_instruccion','gramatica.py',222),
  ('instruccion -> instruccion2','instruccion',1,'p_instruccion','gramatica.py',223),
  ('instruccion3 -> instruccion3 instruccion2','instruccion3',2,'p_instruccion3','gramatica.py',230),
  ('instruccion3 -> instruccion3 instruccion2 PTOYCOMA','instruccion3',3,'p_instruccion3_ptcoma','gramatica.py',238),
  ('instruccion3 -> instruccion2','instruccion3',1,'p_instruccion3_instruccion2','gramatica.py',246),
  ('instruccion3 -> instruccion2 PTOYCOMA','instruccion3',2,'p_instruccion3_instruccion2_ptcoma','gramatica.py',253),
  ('bloque -> LLAIZQ instruccion3 LLADER','bloque',3,'p_bloque','gramatica.py',260),
  ('bloque -> LLAIZQ LLADER','bloque',2,'p_bloque2','gramatica.py',267),
  ('instruccion2 -> declaracion','instruccion2',1,'p_instruccion2','gramatica.py',284),
  ('instruccion2 -> asignacion','instruccion2',1,'p_instruccion2','gramatica.py',285),
  ('instruccion2 -> impresion','instruccion2',1,'p_instruccion2','gramatica.py',286),
  ('instruccion2 -> return','instruccion2',1,'p_instruccion2','gramatica.py',287),
  ('instruccion2 -> break','instruccion2',1,'p_instruccion2','gramatica.py',288),
  ('instruccion2 -> continue','instruccion2',1,'p_instruccion2','gramatica.py',289),
  ('instruccion2 -> condicional_if','instruccion2',1,'p_instruccion2','gramatica.py',290),
  ('instruccion2 -> ciclo_while','instruccion2',1,'p_instruccion2','gramatica.py',291),
  ('instruccion2 -> ciclo_for','instruccion2',1,'p_instruccion2','gramatica.py',292),
  ('declaracion -> LET ID DOSPUNTOS tipo IGUAL expresion','declaracion',6,'p_declaracion1','gramatica.py',299),
  ('declaracion -> LET ID IGUAL expresion','declaracion',4,'p_declaracion2','gramatica.py',306),
  ('asignacion -> ID IGUAL expresion','asignacion',3,'p_asignacion','gramatica.py',313),
  ('impresion -> CONSOLE PUNTO LOG PARIZQ expresion PARDER','impresion',6,'p_impresion','gramatica.py',320),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',334),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',335),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',336),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',337),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',338),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',339),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_aritmetica','gramatica.py',340),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_aritmetica','gramatica.py',341),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_relacional','gramatica.py',369),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion_relacional','gramatica.py',370),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',371),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',372),
  ('expresion -> expresion IGUALACION expresion','expresion',3,'p_expresion_relacional','gramatica.py',373),
  ('expresion -> expresion DISTINTO expresion','expresion',3,'p_expresion_relacional','gramatica.py',374),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_logica','gramatica.py',396),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_logica','gramatica.py',397),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_logica','gramatica.py',398),
  ('expresion -> NUMERO','expresion',1,'p_expresion_primitiva','gramatica.py',415),
  ('expresion -> CADENA','expresion',1,'p_expresion_primitiva','gramatica.py',416),
  ('expresion -> ID','expresion',1,'p_expresion_primitiva','gramatica.py',417),
  ('expresion -> TRUE','expresion',1,'p_expresion_primitiva','gramatica.py',418),
  ('expresion -> FALSE','expresion',1,'p_expresion_primitiva','gramatica.py',419),
  ('expresion -> ID MAS MAS','expresion',3,'p_expresion_incremento_decremento','gramatica.py',440),
  ('expresion -> ID DECREMENTO','expresion',2,'p_expresion_incremento_decremento','gramatica.py',441),
  ('expresion -> MAS MAS ID','expresion',3,'p_expresion_incremento_decremento','gramatica.py',442),
  ('expresion -> DECREMENTO ID','expresion',2,'p_expresion_incremento_decremento','gramatica.py',443),
  ('tipo -> NUMBER','tipo',1,'p_tipo','gramatica.py',465),
  ('tipo -> STRING','tipo',1,'p_tipo','gramatica.py',466),
  ('tipo -> BOOLEAN','tipo',1,'p_tipo','gramatica.py',467),
  ('tipo -> ANY','tipo',1,'p_tipo','gramatica.py',468),
  ('return -> RETURN','return',1,'p_retorno','gramatica.py',484),
  ('return -> RETURN expresion','return',2,'p_retorno','gramatica.py',485),
  ('continue -> CONTINUE','continue',1,'p_continue','gramatica.py',495),
  ('break -> BREAK','break',1,'p_break','gramatica.py',502),
  ('condicional_if -> IF PARIZQ expresion PARDER bloque','condicional_if',5,'p_condicional_if','gramatica.py',509),
  ('condicional_if -> IF PARIZQ expresion PARDER bloque ELSE bloque','condicional_if',7,'p_condicional_if_else','gramatica.py',515),
  ('condicional_if -> IF PARIZQ expresion PARDER bloque lista_elif','condicional_if',6,'p_condicional_if_elif','gramatica.py',522),
  ('condicional_if -> IF PARIZQ expresion PARDER bloque lista_elif ELSE bloque','condicional_if',8,'p_condicional_if_elif_else','gramatica.py',528),
  ('lista_elif -> lista_elif elif','lista_elif',2,'p_lista_elif','gramatica.py',535),
  ('lista_elif -> elif','lista_elif',1,'p_lista_elif_else','gramatica.py',543),
  ('elif -> ELSE IF PARIZQ expresion PARDER bloque','elif',6,'p_lista_elif_elif','gramatica.py',549),
  ('ciclo_while -> WHILE PARIZQ expresion PARDER bloque','ciclo_while',5,'p_ciclo_while','gramatica.py',557),
  ('ciclo_for -> FOR PARIZQ declaracion PTOYCOMA expresion PTOYCOMA asignacion PARDER bloque','ciclo_for',9,'p_ciclo_for','gramatica.py',564),
  ('ciclo_for -> FOR PARIZQ asignacion PTOYCOMA expresion PTOYCOMA asignacion PARDER bloque','ciclo_for',9,'p_ciclo_for2','gramatica.py',571),
  ('ciclo_for -> FOR PARIZQ declaracion PTOYCOMA expresion PTOYCOMA expresion PARDER bloque','ciclo_for',9,'p_ciclo_for3','gramatica.py',578),
  ('ciclo_for -> FOR PARIZQ asignacion PTOYCOMA expresion PTOYCOMA expresion PARDER bloque','ciclo_for',9,'p_ciclo_for4','gramatica.py',585),
  ('instruccion -> error PTOYCOMA','instruccion',2,'p_error_inst','gramatica.py',594),
]
