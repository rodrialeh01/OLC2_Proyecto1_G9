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
        print("==============================================")
        print("Desde DeclaracionArray : ")
        print(self.id)
        print(self.expresion)
        print(self.tipo)
        print("***********************************************")
        exp = self.expresion.ejecutar(entorno, helper) #obtiene objeto Array
        print(self.id)
        if isinstance(self.tipo, TIPO_DATO):
            bandera = True
            if self.tipo != TIPO_DATO.ANY or self.tipo != TIPO_DATO.ARRAY:
                bandera = self.Verificar_Tipos_array(exp.valor, self.tipo, bandera, entorno)
                if bandera == None:
                    bandera = True
                print("bandera: " + str(bandera))
                if not bandera:
                    #error semantico
                    s = SingletonErrores.getInstance()
                    err = Error(self.linea, self.columna, "Error Semántico", "El tipo de dato del array no coincide con el tipo de dato declarado")
                    s.addError(err)
            print("VOY A CREAAAAAAAAAAAAAR EL SIMBOLO")
            #crear el simbolo
            simbolo = Simbolo()
            simbolo.nombre = self.id
            if self.tipo == TIPO_DATO.NUMERO:
                print("OP1")
                simbolo.tipo = TIPO_DATO.ARRAY_NUMBER
            elif self.tipo == TIPO_DATO.CADENA:
                print("OP2")
                simbolo.tipo = TIPO_DATO.ARRAY_STRING

            elif self.tipo == TIPO_DATO.BOOLEANO:
                print("OP2")
                simbolo.tipo = TIPO_DATO.ARRAY_BOOLEAN
            elif self.tipo == TIPO_DATO.ANY or self.tipo == TIPO_DATO.ARRAY:
                print("entro al any")
                simbolo.tipo = TIPO_DATO.ARRAY
            else:
                print("entro al else")
            simbolo.valor = exp.valor
            simbolo.linea = self.linea
            simbolo.columna = self.columna
            print("se creo el simbolo: ")
            print(simbolo)
            #agregar el simbolo al entorno
            verifExistencia = entorno.ExisteSimbolo(simbolo.nombre)
            if verifExistencia:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.linea, self.columna, "Error Semántico", "La variable " + simbolo.nombre + " ya existe en el entorno actual")
                s.addError(err)
                return
            print("se va a agregar")
            entorno.AgregarSimbolo(self.id,simbolo)
        else:
            print("NO SOY UN TIPODATO")
            tipo_interface = entorno.ExisteInterface(self.tipo)
            print("tipo interface: " + str(tipo_interface))
            if not tipo_interface:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.linea, self.columna, "Error Semántico", "La interface " + self.id_interface + " no existe en el entorno actual")
                s.addError(err)
                return
            
            #crear el simbolo
            bandera = True
            if self.tipo != TIPO_DATO.ANY or self.tipo != TIPO_DATO.ARRAY:
                bandera = self.Verificar_Tipos_array(exp.valor, self.tipo, bandera, entorno)
                if bandera == None:
                    bandera = True
                print("bandera: " + str(bandera))
                if not bandera:
                    #error semantico
                    s = SingletonErrores.getInstance()
                    err = Error(self.linea, self.columna, "Error Semántico", "El tipo de dato del array no coincide con el tipo de dato declarado")
                    s.addError(err)
            print("VOY A CREAAAAAAAAAAAAAR EL SIMBOLO")
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
                return
            print("se va a agregar")
            entorno.AgregarSimbolo(self.id,simbolo)
            print("se creo el simbolo: ")



    
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