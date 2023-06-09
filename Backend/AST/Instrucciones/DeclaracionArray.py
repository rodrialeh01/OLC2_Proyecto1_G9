from AST.Abstract.Instruccion import Instruccion
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Simbolo import Simbolo


class DeclaracionArray(Instruccion):
    def __init__(self, id, tipo, expresion, linea, columna):
        self.id = id
        self.tipo = tipo
        self.expresion = expresion
        self.linea = linea
        self.columna = columna

    
    def ejecutar(self, entorno, helper):
        exp = self.expresion.ejecutar(entorno, helper) #obtiene objeto Array
        bandera = True
        bandera = self.Verificar_Tipos_array(exp.valor, self.tipo, bandera)
        if bandera == None:
            bandera = True
        
        if not bandera:
            #error semantico
            return
        
        #crear el simbolo
        simbolo = Simbolo()
        simbolo.nombre = self.id
        if self.tipo == TIPO_DATO.NUMERO:
            simbolo.tipo = TIPO_DATO.ARRAY_NUMBER
        elif self.tipo == TIPO_DATO.STRING:
            simbolo.tipo = TIPO_DATO.ARRAY_STRING
        elif self.tipo == TIPO_DATO.BOOLEAN:
            simbolo.tipo = TIPO_DATO.ARRAY_BOOLEAN
        elif self.tipo == TIPO_DATO.ANY:
            simbolo.tipo = TIPO_DATO.ANY
        simbolo.valor = exp.valor
        simbolo.linea = self.linea
        simbolo.columna = self.columna

        #agregar el simbolo al entorno
        verifExistencia = entorno.ExisteSimbolo(simbolo.nombre)
        if verifExistencia:
            #error semantico
            return
        print("se va a agregar")
        entorno.AgregarSimbolo(self.id,simbolo)


    
    def Verificar_Tipos_array(self,arr, tipo, bandera):
        if isinstance(arr,list):
            for a in arr:
                if a.tipo == TIPO_DATO.ARRAY:
                    bandera = self.Verificar_Tipos_array(a.valor, tipo, bandera)
                    if bandera == False:
                        return False
                else:
                    bandera = self.Verificar_Tipos_array(a, tipo, bandera)
                    if bandera == False:
                        return False
        else:
            if arr.tipo != tipo:
                if tipo != TIPO_DATO.ANY:
                    bandera = False
                    return bandera
                else:
                    bandera = True
            else:
                bandera = True
