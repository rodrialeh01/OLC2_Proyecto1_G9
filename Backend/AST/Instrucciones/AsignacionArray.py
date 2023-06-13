from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class AsignacionArray(Instruccion):
    def __init__(self, id, accesos,expresion, linea, columna):
        self.id = id
        self.accesos = accesos
        self.expresion = expresion
        self.linea = linea
        self.columna = columna

    def ejecutar(self, entorno, helper):
        #print('---------------------------------------------------------')
        #print("Desde AsignacionArray : ")
        #buscar el id en el entorno
        existe = entorno.ExisteSimbolo(self.id)
        if not existe:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "La variable " + self.id + " no existe en el entorno actual" )
            s.addError(err)
            return
        
        #print("si existe el simbolo")
        simbolo = entorno.ObtenerSimbolo(self.id)
        listaAccesos = []
        #print(simbolo.valor)
        #verificar que sea un array
        
        for a in self.accesos:
            listaAccesos.append(a.ejecutar(entorno, helper).valor)
        sim = simbolo.valor
        print(simbolo.nombre)
        #print(sim)
        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        self.accesar(listaAccesos, sim,self.expresion,simbolo.tipo, entorno, helper)
        print('sim actualizado')
        print("ESTA ES LA PRUEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA:")
        print(simbolo.tipo)
        print(sim)
        simbolo.valor = sim
        entorno.ActualizarSimbolo(simbolo.nombre, simbolo)
        print('---------------------------------------------------------')

    def accesar(self, pila, lista, expresion,tipo, entorno, helper):
        if len(pila) == 0:
            print("se vacio la pila")
            print(lista)
            #expresion.ejecutar(entorno, helper).tipo 
            ex = expresion.ejecutar(entorno, helper)
            if tipo == TIPO_DATO.ARRAY:
                lista = ex
        else:
            #{0,3,2}
            index = pila.pop(0)
            try:
                valor = lista[index]
                print(valor.tipo)
            except:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.linea, self.columna, "Error Semántico", "El indice " + str(index) + " no existe en el array" )
                s.addError(err)
                return
            if valor.tipo == TIPO_DATO.ARRAY or valor.tipo == TIPO_DATO.ARRAY_NUMBER or valor.tipo == TIPO_DATO.ARRAY_STRING or valor.tipo == TIPO_DATO.ARRAY_BOOLEAN:
                self.accesar(pila, valor.valor, expresion,tipo, entorno, helper)
            else:
                if len(pila) == 0:

                    e = expresion.ejecutar(entorno, helper)
                    verif = False
                    if e.tipo == TIPO_DATO.ARRAY:
                        verif = self.Verificar_Tipos_array(e.valor, tipo, verif)
                    if verif == None:
                        verif = True
                
                    if tipo == TIPO_DATO.ARRAY or (tipo == TIPO_DATO.ARRAY_NUMBER and e.tipo == TIPO_DATO.NUMERO) or (tipo == TIPO_DATO.ARRAY_STRING and e.tipo == TIPO_DATO.CADENA) or (tipo == TIPO_DATO.ARRAY_BOOLEAN and e.tipo == TIPO_DATO.BOOLEANO) or (e.tipo == TIPO_DATO.ARRAY) or verif:
                        print('EXPRESION A LA CUAL VOY A ASIGNAR:')
                        print(e)
                        lista[index] = e
                    else:
                        #error semantico
                        s = SingletonErrores.getInstance()
                        err = Error(self.linea, self.columna, "Error Semántico", "El tipo de dato de la expresion no coincide con el tipo de dato del array" )
                        s.addError(err)
                        return
                else:
                    #error semantico
                    s = SingletonErrores.getInstance()
                    err = Error(self.linea, self.columna, "Error Semántico", "El indice " + str(index) + " no existe en el array" )
                    s.addError(err)
                    return
    
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

    def genArbol(self) -> Nodo:
        print("+**********************+++++++++++++++++++++++++++++++*********************")
        nodo = Nodo("ASIGNACION ARRAY")

        nodo.agregarHijo(Nodo(str(self.id)))
        acc = Nodo("ACCESO")
        nodo.agregarHijo(acc)
        for a in self.accesos:
            acc.agregarHijo(Nodo("["))
            acc.agregarHijo(a.genArbol())
            acc.agregarHijo(Nodo("]"))
        nodo.agregarHijo(Nodo("="))
        nodo.agregarHijo(self.expresion.genArbol())
        return nodo