
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDnonassocMAYORMENORIGUALMENORMAYORIGUALIGUALACIONDISTINTOleftMASMENOSleftPORDIVIDIDOMODULOrightNOTUMENOSAND ANY ARRAY BOOLEAN BREAK CADENA COMA CONCAT CONSOLE CONTINUE CORDER CORIZQ DISTINTO DIVIDIDO DOSPUNTOS ELSE FALSE FOR FUNCTION ID IF IGUAL IGUALACION INTERFACE LET LLADER LLAIZQ LOG MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MODULO NOT NULL NUMBER NUMERO OF OR PARDER PARIZQ POR POTENCIA PTOYCOMA PUNTO RETURN SPLIT STRING TOEXPONENTIAL TOFIXED TOLOWERCASE TOSTRING TOUPPERCASE TRUE WHILE\n    instrucciones : instrucciones instruccion\n    \n    instrucciones : instruccion\n    \n    instruccion : instruccion2 PTOYCOMA\n                | instruccion2\n    \n    instruccion3 : instruccion3 instruccion2\n    \n    instruccion3 : instruccion3 instruccion2 PTOYCOMA\n    \n    instruccion3 : instruccion2\n    \n    instruccion3 : instruccion2 PTOYCOMA\n    \n    bloque : LLAIZQ instruccion3 LLADER\n    \n    bloque : LLAIZQ LLADER\n    \n    instruccion2 : declaracion\n                 | asignacion\n                 | impresion\n                 | return\n                 | break\n                 | continue\n                 | condicional_if\n                 | ciclo_while\n    \n    declaracion : LET ID DOSPUNTOS tipo IGUAL expresion\n    \n    declaracion : LET ID IGUAL expresion\n    \n    asignacion : ID IGUAL expresion\n    \n    impresion : CONSOLE PUNTO LOG PARIZQ expresion PARDER\n    \n    expresion : expresion MAS expresion\n            | expresion MENOS expresion\n            | expresion POR expresion\n            | expresion DIVIDIDO expresion\n            | expresion POTENCIA expresion\n            | expresion MODULO expresion\n            | MENOS expresion %prec UMENOS\n            | PARIZQ expresion PARDER\n    \n    expresion : expresion MAYOR expresion\n            | expresion MENOR expresion\n            | expresion MAYORIGUAL expresion\n            | expresion MENORIGUAL expresion\n            | expresion IGUALACION expresion\n            | expresion DISTINTO expresion\n    \n    expresion : expresion AND expresion\n            | expresion OR expresion\n            | NOT expresion\n    \n    expresion : NUMERO\n            | CADENA\n            | ID\n            | TRUE\n            | FALSE\n    \n    tipo : NUMBER\n        | STRING\n        | BOOLEAN\n        | ANY\n    \n    return : RETURN\n           | RETURN expresion\n    \n    continue : CONTINUE\n    \n    break : BREAK\n    \n    condicional_if : IF PARIZQ expresion PARDER bloque\n    \n    condicional_if : IF PARIZQ expresion PARDER bloque ELSE bloque\n    \n    condicional_if : IF PARIZQ expresion PARDER bloque lista_elif\n    \n    condicional_if : IF PARIZQ expresion PARDER bloque lista_elif ELSE bloque\n    \n    lista_elif : lista_elif elif\n    \n    lista_elif : elif\n    \n    elif : ELSE IF PARIZQ expresion PARDER bloque\n    \n    ciclo_while : WHILE PARIZQ expresion PARDER bloque\n    \n    instruccion : error PTOYCOMA\n    '
    
_lr_action_items = {'error':([0,1,2,3,5,6,7,8,9,10,11,12,16,17,18,21,22,23,27,31,32,33,34,35,40,56,58,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,89,90,91,93,94,96,99,101,102,106,110,],[4,4,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-49,-52,-51,-1,-3,-61,-50,-40,-41,-42,-43,-44,-21,-29,-39,-20,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,-53,-60,-19,-22,-55,-58,-10,-54,-57,-9,-56,-59,]),'LET':([0,1,2,3,5,6,7,8,9,10,11,12,16,17,18,21,22,23,27,31,32,33,34,35,40,56,58,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,88,89,90,91,93,94,95,96,97,99,101,102,103,104,106,107,110,],[13,13,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-49,-52,-51,-1,-3,-61,-50,-40,-41,-42,-43,-44,-21,-29,-39,-20,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,-53,13,-60,-19,-22,-55,-58,13,-10,-7,-54,-57,-9,-5,-8,-56,-6,-59,]),'ID':([0,1,2,3,5,6,7,8,9,10,11,12,13,16,17,18,21,22,23,25,27,28,29,30,31,32,33,34,35,36,37,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,87,88,89,90,91,93,94,95,96,97,99,101,102,103,104,105,106,107,110,],[14,14,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,24,33,-52,-51,-1,-3,-61,33,-50,33,33,33,-40,-41,-42,-43,-44,33,33,33,-21,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-29,-39,-20,33,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,33,-53,14,-60,-19,-22,-55,-58,14,-10,-7,-54,-57,-9,-5,-8,33,-56,-6,-59,]),'CONSOLE':([0,1,2,3,5,6,7,8,9,10,11,12,16,17,18,21,22,23,27,31,32,33,34,35,40,56,58,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,88,89,90,91,93,94,95,96,97,99,101,102,103,104,106,107,110,],[15,15,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-49,-52,-51,-1,-3,-61,-50,-40,-41,-42,-43,-44,-21,-29,-39,-20,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,-53,15,-60,-19,-22,-55,-58,15,-10,-7,-54,-57,-9,-5,-8,-56,-6,-59,]),'RETURN':([0,1,2,3,5,6,7,8,9,10,11,12,16,17,18,21,22,23,27,31,32,33,34,35,40,56,58,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,88,89,90,91,93,94,95,96,97,99,101,102,103,104,106,107,110,],[16,16,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-49,-52,-51,-1,-3,-61,-50,-40,-41,-42,-43,-44,-21,-29,-39,-20,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,-53,16,-60,-19,-22,-55,-58,16,-10,-7,-54,-57,-9,-5,-8,-56,-6,-59,]),'BREAK':([0,1,2,3,5,6,7,8,9,10,11,12,16,17,18,21,22,23,27,31,32,33,34,35,40,56,58,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,88,89,90,91,93,94,95,96,97,99,101,102,103,104,106,107,110,],[17,17,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-49,-52,-51,-1,-3,-61,-50,-40,-41,-42,-43,-44,-21,-29,-39,-20,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,-53,17,-60,-19,-22,-55,-58,17,-10,-7,-54,-57,-9,-5,-8,-56,-6,-59,]),'CONTINUE':([0,1,2,3,5,6,7,8,9,10,11,12,16,17,18,21,22,23,27,31,32,33,34,35,40,56,58,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,88,89,90,91,93,94,95,96,97,99,101,102,103,104,106,107,110,],[18,18,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-49,-52,-51,-1,-3,-61,-50,-40,-41,-42,-43,-44,-21,-29,-39,-20,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,-53,18,-60,-19,-22,-55,-58,18,-10,-7,-54,-57,-9,-5,-8,-56,-6,-59,]),'IF':([0,1,2,3,5,6,7,8,9,10,11,12,16,17,18,21,22,23,27,31,32,33,34,35,40,56,58,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,104,106,107,110,],[19,19,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-49,-52,-51,-1,-3,-61,-50,-40,-41,-42,-43,-44,-21,-29,-39,-20,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,-53,19,-60,-19,-22,98,-55,-58,19,-10,-7,-54,98,-57,-9,-5,-8,-56,-6,-59,]),'WHILE':([0,1,2,3,5,6,7,8,9,10,11,12,16,17,18,21,22,23,27,31,32,33,34,35,40,56,58,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,88,89,90,91,93,94,95,96,97,99,101,102,103,104,106,107,110,],[20,20,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-49,-52,-51,-1,-3,-61,-50,-40,-41,-42,-43,-44,-21,-29,-39,-20,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,-53,20,-60,-19,-22,-55,-58,20,-10,-7,-54,-57,-9,-5,-8,-56,-6,-59,]),'$end':([1,2,3,5,6,7,8,9,10,11,12,16,17,18,21,22,23,27,31,32,33,34,35,40,56,58,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,89,90,91,93,94,96,99,101,102,106,110,],[0,-2,-4,-11,-12,-13,-14,-15,-16,-17,-18,-49,-52,-51,-1,-3,-61,-50,-40,-41,-42,-43,-44,-21,-29,-39,-20,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,-53,-60,-19,-22,-55,-58,-10,-54,-57,-9,-56,-59,]),'PTOYCOMA':([3,4,5,6,7,8,9,10,11,12,16,17,18,27,31,32,33,34,35,40,56,58,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,89,90,91,93,94,96,97,99,101,102,103,106,110,],[22,23,-11,-12,-13,-14,-15,-16,-17,-18,-49,-52,-51,-50,-40,-41,-42,-43,-44,-21,-29,-39,-20,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,-53,-60,-19,-22,-55,-58,-10,104,-54,-57,-9,107,-56,-59,]),'LLADER':([5,6,7,8,9,10,11,12,16,17,18,27,31,32,33,34,35,40,56,58,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,88,89,90,91,93,94,95,96,97,99,101,102,103,104,106,107,110,],[-11,-12,-13,-14,-15,-16,-17,-18,-49,-52,-51,-50,-40,-41,-42,-43,-44,-21,-29,-39,-20,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,-53,96,-60,-19,-22,-55,-58,102,-10,-7,-54,-57,-9,-5,-8,-56,-6,-59,]),'IGUAL':([14,24,61,62,63,64,65,],[25,39,85,-45,-46,-47,-48,]),'PUNTO':([15,],[26,]),'MENOS':([16,25,27,28,29,30,31,32,33,34,35,36,37,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,90,105,108,],[28,28,43,28,28,28,-40,-41,-42,-43,-44,28,28,28,43,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-29,43,-39,43,43,43,28,-23,-24,-25,-26,43,-28,43,43,43,43,43,43,43,43,-30,28,43,43,28,43,]),'PARIZQ':([16,19,20,25,28,29,30,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,67,85,98,105,],[29,36,37,29,29,29,29,29,29,29,67,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,105,29,]),'NOT':([16,25,28,29,30,36,37,39,42,43,44,45,46,47,48,49,50,51,52,53,54,55,67,85,105,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'NUMERO':([16,25,28,29,30,36,37,39,42,43,44,45,46,47,48,49,50,51,52,53,54,55,67,85,105,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'CADENA':([16,25,28,29,30,36,37,39,42,43,44,45,46,47,48,49,50,51,52,53,54,55,67,85,105,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'TRUE':([16,25,28,29,30,36,37,39,42,43,44,45,46,47,48,49,50,51,52,53,54,55,67,85,105,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'FALSE':([16,25,28,29,30,36,37,39,42,43,44,45,46,47,48,49,50,51,52,53,54,55,67,85,105,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'DOSPUNTOS':([24,],[38,]),'LOG':([26,],[41,]),'MAS':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[42,-40,-41,-42,-43,-44,42,-29,42,-39,42,42,42,-23,-24,-25,-26,42,-28,42,42,42,42,42,42,42,42,-30,42,42,42,]),'POR':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[44,-40,-41,-42,-43,-44,44,-29,44,-39,44,44,44,44,44,-25,-26,44,-28,44,44,44,44,44,44,44,44,-30,44,44,44,]),'DIVIDIDO':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[45,-40,-41,-42,-43,-44,45,-29,45,-39,45,45,45,45,45,-25,-26,45,-28,45,45,45,45,45,45,45,45,-30,45,45,45,]),'POTENCIA':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[46,-40,-41,-42,-43,-44,46,-29,46,-39,46,46,46,-23,-24,-25,-26,46,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,46,46,46,]),'MODULO':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[47,-40,-41,-42,-43,-44,47,-29,47,-39,47,47,47,47,47,-25,-26,47,-28,47,47,47,47,47,47,47,47,-30,47,47,47,]),'MAYOR':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[48,-40,-41,-42,-43,-44,48,-29,48,-39,48,48,48,-23,-24,-25,-26,48,-28,None,None,None,None,None,None,48,48,-30,48,48,48,]),'MENOR':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[49,-40,-41,-42,-43,-44,49,-29,49,-39,49,49,49,-23,-24,-25,-26,49,-28,None,None,None,None,None,None,49,49,-30,49,49,49,]),'MAYORIGUAL':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[50,-40,-41,-42,-43,-44,50,-29,50,-39,50,50,50,-23,-24,-25,-26,50,-28,None,None,None,None,None,None,50,50,-30,50,50,50,]),'MENORIGUAL':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[51,-40,-41,-42,-43,-44,51,-29,51,-39,51,51,51,-23,-24,-25,-26,51,-28,None,None,None,None,None,None,51,51,-30,51,51,51,]),'IGUALACION':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[52,-40,-41,-42,-43,-44,52,-29,52,-39,52,52,52,-23,-24,-25,-26,52,-28,None,None,None,None,None,None,52,52,-30,52,52,52,]),'DISTINTO':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[53,-40,-41,-42,-43,-44,53,-29,53,-39,53,53,53,-23,-24,-25,-26,53,-28,None,None,None,None,None,None,53,53,-30,53,53,53,]),'AND':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[54,-40,-41,-42,-43,-44,54,-29,54,-39,54,54,54,-23,-24,-25,-26,54,-28,-31,-32,-33,-34,-35,-36,-37,54,-30,54,54,54,]),'OR':([27,31,32,33,34,35,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,90,108,],[55,-40,-41,-42,-43,-44,55,-29,55,-39,55,55,55,-23,-24,-25,-26,55,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,55,55,55,]),'PARDER':([31,32,33,34,35,56,57,58,59,60,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,86,108,],[-40,-41,-42,-43,-44,-29,82,-39,83,84,-23,-24,-25,-26,-27,-28,-31,-32,-33,-34,-35,-36,-37,-38,-30,91,109,]),'NUMBER':([38,],[62,]),'STRING':([38,],[63,]),'BOOLEAN':([38,],[64,]),'ANY':([38,],[65,]),'LLAIZQ':([83,84,92,100,109,],[88,88,88,88,88,]),'ELSE':([87,93,94,96,101,102,110,],[92,100,-58,-10,-57,-9,-59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,],[1,]),'instruccion':([0,1,],[2,21,]),'instruccion2':([0,1,88,95,],[3,3,97,103,]),'declaracion':([0,1,88,95,],[5,5,5,5,]),'asignacion':([0,1,88,95,],[6,6,6,6,]),'impresion':([0,1,88,95,],[7,7,7,7,]),'return':([0,1,88,95,],[8,8,8,8,]),'break':([0,1,88,95,],[9,9,9,9,]),'continue':([0,1,88,95,],[10,10,10,10,]),'condicional_if':([0,1,88,95,],[11,11,11,11,]),'ciclo_while':([0,1,88,95,],[12,12,12,12,]),'expresion':([16,25,28,29,30,36,37,39,42,43,44,45,46,47,48,49,50,51,52,53,54,55,67,85,105,],[27,40,56,57,58,59,60,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,90,108,]),'tipo':([38,],[61,]),'bloque':([83,84,92,100,109,],[87,89,99,106,110,]),'lista_elif':([87,],[93,]),'elif':([87,93,],[94,101,]),'instruccion3':([88,],[95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',201),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',209),
  ('instruccion -> instruccion2 PTOYCOMA','instruccion',2,'p_instruccion','gramatica.py',217),
  ('instruccion -> instruccion2','instruccion',1,'p_instruccion','gramatica.py',218),
  ('instruccion3 -> instruccion3 instruccion2','instruccion3',2,'p_instruccion3','gramatica.py',225),
  ('instruccion3 -> instruccion3 instruccion2 PTOYCOMA','instruccion3',3,'p_instruccion3_ptcoma','gramatica.py',233),
  ('instruccion3 -> instruccion2','instruccion3',1,'p_instruccion3_instruccion2','gramatica.py',241),
  ('instruccion3 -> instruccion2 PTOYCOMA','instruccion3',2,'p_instruccion3_instruccion2_ptcoma','gramatica.py',248),
  ('bloque -> LLAIZQ instruccion3 LLADER','bloque',3,'p_bloque','gramatica.py',255),
  ('bloque -> LLAIZQ LLADER','bloque',2,'p_bloque2','gramatica.py',262),
  ('instruccion2 -> declaracion','instruccion2',1,'p_instruccion2','gramatica.py',279),
  ('instruccion2 -> asignacion','instruccion2',1,'p_instruccion2','gramatica.py',280),
  ('instruccion2 -> impresion','instruccion2',1,'p_instruccion2','gramatica.py',281),
  ('instruccion2 -> return','instruccion2',1,'p_instruccion2','gramatica.py',282),
  ('instruccion2 -> break','instruccion2',1,'p_instruccion2','gramatica.py',283),
  ('instruccion2 -> continue','instruccion2',1,'p_instruccion2','gramatica.py',284),
  ('instruccion2 -> condicional_if','instruccion2',1,'p_instruccion2','gramatica.py',285),
  ('instruccion2 -> ciclo_while','instruccion2',1,'p_instruccion2','gramatica.py',286),
  ('declaracion -> LET ID DOSPUNTOS tipo IGUAL expresion','declaracion',6,'p_declaracion1','gramatica.py',293),
  ('declaracion -> LET ID IGUAL expresion','declaracion',4,'p_declaracion2','gramatica.py',300),
  ('asignacion -> ID IGUAL expresion','asignacion',3,'p_asignacion','gramatica.py',307),
  ('impresion -> CONSOLE PUNTO LOG PARIZQ expresion PARDER','impresion',6,'p_impresion','gramatica.py',314),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',329),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',330),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',331),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',332),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',333),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',334),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_aritmetica','gramatica.py',335),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_aritmetica','gramatica.py',336),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_relacional','gramatica.py',364),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion_relacional','gramatica.py',365),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',366),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',367),
  ('expresion -> expresion IGUALACION expresion','expresion',3,'p_expresion_relacional','gramatica.py',368),
  ('expresion -> expresion DISTINTO expresion','expresion',3,'p_expresion_relacional','gramatica.py',369),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_logica','gramatica.py',391),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_logica','gramatica.py',392),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_logica','gramatica.py',393),
  ('expresion -> NUMERO','expresion',1,'p_expresion_primitiva','gramatica.py',410),
  ('expresion -> CADENA','expresion',1,'p_expresion_primitiva','gramatica.py',411),
  ('expresion -> ID','expresion',1,'p_expresion_primitiva','gramatica.py',412),
  ('expresion -> TRUE','expresion',1,'p_expresion_primitiva','gramatica.py',413),
  ('expresion -> FALSE','expresion',1,'p_expresion_primitiva','gramatica.py',414),
  ('tipo -> NUMBER','tipo',1,'p_tipo','gramatica.py',436),
  ('tipo -> STRING','tipo',1,'p_tipo','gramatica.py',437),
  ('tipo -> BOOLEAN','tipo',1,'p_tipo','gramatica.py',438),
  ('tipo -> ANY','tipo',1,'p_tipo','gramatica.py',439),
  ('return -> RETURN','return',1,'p_retorno','gramatica.py',455),
  ('return -> RETURN expresion','return',2,'p_retorno','gramatica.py',456),
  ('continue -> CONTINUE','continue',1,'p_continue','gramatica.py',466),
  ('break -> BREAK','break',1,'p_break','gramatica.py',473),
  ('condicional_if -> IF PARIZQ expresion PARDER bloque','condicional_if',5,'p_condicional_if','gramatica.py',480),
  ('condicional_if -> IF PARIZQ expresion PARDER bloque ELSE bloque','condicional_if',7,'p_condicional_if_else','gramatica.py',487),
  ('condicional_if -> IF PARIZQ expresion PARDER bloque lista_elif','condicional_if',6,'p_condicional_if_elif','gramatica.py',495),
  ('condicional_if -> IF PARIZQ expresion PARDER bloque lista_elif ELSE bloque','condicional_if',8,'p_condicional_if_elif_else','gramatica.py',502),
  ('lista_elif -> lista_elif elif','lista_elif',2,'p_lista_elif','gramatica.py',510),
  ('lista_elif -> elif','lista_elif',1,'p_lista_elif_else','gramatica.py',518),
  ('elif -> ELSE IF PARIZQ expresion PARDER bloque','elif',6,'p_lista_elif_elif','gramatica.py',524),
  ('ciclo_while -> WHILE PARIZQ expresion PARDER bloque','ciclo_while',5,'p_ciclo_while','gramatica.py',532),
  ('instruccion -> error PTOYCOMA','instruccion',2,'p_error_inst','gramatica.py',540),
]
