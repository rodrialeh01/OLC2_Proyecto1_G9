from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores


class DeclaracionArray(Instruccion):
    def __init__(self, id, tipo, expresion, linea, columna):
        self.id = id
        self.tipo = tipo
        self.expresion = expresion
        self.linea = linea
        self.columna = columna

    
    def ejecutar(self, entorno, helper):
        exp = self.expresion.ejecutar(entorno, helper) #obtiene objeto Array
        if isinstance(self.tipo, TIPO_DATO):
            bandera = True
            if self.tipo != TIPO_DATO.ANY or self.tipo != TIPO_DATO.ARRAY:
                bandera = self.Verificar_Tipos_array(exp.valor, self.tipo, bandera, entorno)
                if bandera == None:
                    bandera = True
                if not bandera:
                    #error semantico
                    s = SingletonErrores.getInstance()
                    err = Error(self.linea, self.columna, "Error Semántico", "El tipo de dato del array no coincide con el tipo de dato declarado")
                    helper.setConsola("[ERROR] El tipo de dato del array no coincide con el tipo de dato declarado en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                    s.addError(err)
            #crear el simbolo
            simbolo = Simbolo()
            simbolo.nombre = self.id
            if self.tipo == TIPO_DATO.NUMERO:
                simbolo.tipo = TIPO_DATO.ARRAY_NUMBER
            elif self.tipo == TIPO_DATO.CADENA:
                simbolo.tipo = TIPO_DATO.ARRAY_STRING

            elif self.tipo == TIPO_DATO.BOOLEANO:
                simbolo.tipo = TIPO_DATO.ARRAY_BOOLEAN
            elif self.tipo == TIPO_DATO.ANY or self.tipo == TIPO_DATO.ARRAY:
                simbolo.tipo = TIPO_DATO.ARRAY
            else:
                print("entro al else")
            simbolo.valor = exp.valor
            simbolo.linea = self.linea
            simbolo.columna = self.columna

            #agregar el simbolo al entorno
            verifExistencia = entorno.BuscarSimboloLocal(simbolo.nombre)
            if not verifExistencia:
                verifExistencia = entorno.BuscarInterfaceDeclaradaLocal(simbolo.nombre)
                if not verifExistencia:
                    verifExistencia = entorno.BuscarInterfaceLocal(simbolo.nombre)
            if verifExistencia:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.linea, self.columna, "Error Semántico", "La variable " + simbolo.nombre + " ya existe en el entorno actual")
                s.addError(err)
                helper.setConsola("[ERROR] La variable " + simbolo.nombre + " ya existe en el entorno actual en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                return
            entorno.AgregarSimbolo(self.id,simbolo)
        else:
            tipo_interface = entorno.ExisteInterface(self.tipo)
            if not tipo_interface:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.linea, self.columna, "Error Semántico", "La interface " + self.id_interface + " no existe en el entorno actual")
                s.addError(err)
                helper.setConsola("[ERROR] La interface " + self.id_interface + " no existe en el entorno actual en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                return
            
            #crear el simbolo
            bandera = True
            if self.tipo != TIPO_DATO.ANY or self.tipo != TIPO_DATO.ARRAY:
                bandera = self.Verificar_Tipos_array(exp.valor, self.tipo, bandera, entorno)
                if bandera == None:
                    bandera = True
                if not bandera:
                    #error semantico
                    s = SingletonErrores.getInstance()
                    err = Error(self.linea, self.columna, "Error Semántico", "El tipo de dato del array no coincide con el tipo de dato declarado se esperaba " + self.tipo +  " y se obtuvo " + str(obtTipoDato(exp.valor)) )
                    helper.setConsola("[ERROR] El tipo de dato del array no coincide con el tipo de dato declarado en la línea "+ str(self.linea) +" y columna " + str(self.columna) + " se esperaba " + self.tipo +  " y se obtuvo " + str(obtTipoDato(exp.valor)))
                    s.addError(err)
                    return
                
            simbolo = Simbolo()
            simbolo.nombre = self.id
            simbolo.tipo = TIPO_DATO.ARRAY_INTERFACE
            simbolo.valor = exp.valor
            simbolo.linea = self.linea
            simbolo.columna = self.columna
            verifExistencia = entorno.ExisteSimbolo(simbolo.nombre)
            if verifExistencia:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.linea, self.columna, "Error Semántico", "La variable " + simbolo.nombre + " ya existe en el entorno actual")
                s.addError(err)
                helper.setConsola("[ERROR] La variable " + simbolo.nombre + " ya existe en el entorno actual en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                return

            entorno.AgregarSimbolo(self.id,simbolo)



    
    def Verificar_Tipos_array(self,arr, tipo, bandera, entorno):
        if isinstance(arr,list):
            for a in arr:
                if a.tipo == TIPO_DATO.ARRAY:
                    bandera = self.Verificar_Tipos_array(a.valor, tipo, bandera,entorno)
                    if bandera == False:
                        return False
                else:
                    bandera = self.Verificar_Tipos_array(a, tipo, bandera, entorno)
                    if bandera == False:
                        return False
        else:
            if arr.tipo != tipo:
                if arr.tipo == TIPO_DATO.INTERFACE:
                    return entorno.ExisteInterface(tipo)
                elif tipo != TIPO_DATO.ANY:
                    bandera = False
                    return bandera
                else:
                    bandera = True
            else:
                bandera = True

    def genArbol(self) -> Nodo:
        nodo = Nodo("DECLARACION ARRAY")
        nodo.agregarHijo(Nodo(str(self.id)))
        nodo.agregarHijo(Nodo(str(self.tipo)))
        nodo.agregarHijo(self.expresion.genArbol())
        return nodo