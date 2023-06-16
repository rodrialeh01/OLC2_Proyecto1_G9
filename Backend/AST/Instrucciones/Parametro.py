from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores


class Parametro(Instruccion):
    def __init__(self, id, tipo, valor, fila, columna, esRef):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna

        self.esRef = esRef 
        self.utilizado = None 
        self.entorno = None 
        self.valorRef = None 

    def ejecutar(self, entorno, helper):
        #print("**********************PARAMETRO")
        #print(self.tipo)
        #print(self.utilizado.tipo)
        #print(self.id)
        if self.valor != None or self.utilizado != None:
            retorno = Retorno()
            if self.valor != None: 
                retorno = self.valor.ejecutar(entorno, helper)
            else:
                retorno.valor = self.utilizado.valor
                retorno.tipo = self.utilizado.tipo


            if self.tipo != retorno.tipo:
                if retorno.tipo != TIPO_DATO.INTERFACE:
                    s = SingletonErrores.getInstance()
                    err = Error(self.fila, self.columna, "Error Semántico", "El tipo de dato no coincide con el tipo de dato del parametro")
                    s.addError(err)
                    helper.setConsola("[ERROR] El tipo de dato no coincide con el tipo de dato del parametro en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                    return
                
                existe_tipo = entorno.ExisteInterface(self.tipo)
                if not existe_tipo:
                    s = SingletonErrores.getInstance()
                    err = Error(self.fila, self.columna, "Error Semántico", "El tipo de dato no coincide con el tipo de dato del parametro")
                    s.addError(err)
                    helper.setConsola("[ERROR] El tipo de dato no coincide con el tipo de dato del parametro en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                    return
                
                existencia_id = entorno.BuscarSimboloLocal(self.id)
                tipo_obj = entorno.ObtenerInterface(self.tipo)
                #print("EXISTENCIA ID", existencia_id)
                if existencia_id is False:
                    #print("INTERFAXXXX")
                    simbolo = self.utilizado.valor
                    #print(simbolo.listaParams)
                    verificacion = True
                    lista_parametros_objeto = tipo_obj.listaParametros
                    listaParams = simbolo.listaParams
                    lista_ya_Declarada = []
                    #recorremos la lista de parametros del objeto
                    for i in range(0, len(lista_parametros_objeto)):
                        #placa : "P-1234" <- exp = Retorno("P-1234", TIPO_DATO.CADENA)
                        if verificacion:
                            verificacion = False
                            for j in range(0, len(listaParams)):
                                if lista_parametros_objeto[i].id == listaParams[j].id:
                                    verificacion = True
                                    exp = listaParams[j].expresion.ejecutar(entorno, helper)
                                    if lista_parametros_objeto[i].tipo != exp.tipo and lista_parametros_objeto[i].tipo != TIPO_DATO.ANY:
                                        #error semantico
                                        s = SingletonErrores.getInstance()
                                        err = Error(self.fila, self.columna, "Error Semántico", "El tipo de dato para el parametro " + lista_parametros_objeto[i].id + " no coincide" )
                                        s.addError(err)
                                        helper.setConsola("[ERROR] El tipo de dato para el parametro " + lista_parametros_objeto[i].id + " no coincide en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                                        return
                                    
                                    lista_ya_Declarada.append({
                                        lista_parametros_objeto[i].id : exp
                                    })

                                    j = len(listaParams)
                        else:
                            break
                    simbolo.crearStructDeclarado(self.id, lista_ya_Declarada,self.tipo, self.fila, self.columna)
                    entorno.AgregarInterfaceDeclarada(self.id, simbolo)
                    #print("Me creee :D con el id: ", self.id)
                    return
                else:
                    s = SingletonErrores.getInstance()
                    err = Error(self.fila, self.columna, "Error Semántico", "El parametro " + self.id + " ya fue declarado anteriormente en el entorno actual")
                    s.addError(err)
                    helper.setConsola("[ERROR] El parametro " + self.id + " ya fue declarado anteriormente en el entorno actual en la línea "+ str(self.fila) +" y columna " + str(self.columna))

                    #ERROR
                    return

            ##print("SIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIUUUUUUUUUUUUU")
            existencia = entorno.BuscarSimboloLocal(self.id)
            #print(existencia)
            if existencia is False:
                simbolo = Simbolo()
                simbolo.nombre = self.id
                simbolo.tipo = self.tipo
                simbolo.valor = retorno.valor
                simbolo.linea = self.fila
                simbolo.columna = self.columna
                simbolo.entorno = entorno

                entorno.AgregarSimbolo(self.id, simbolo)
            else:
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "El parametro " + self.id + " ya fue declarado anteriormente en el entorno actual")
                s.addError(err)
                helper.setConsola("[ERROR] El parametro " + self.id + " ya fue declarado anteriormente en el entorno actual en la línea "+ str(self.fila) +" y columna " + str(self.columna))

                #ERROR
                return
        else:
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "El parametro" + self.id +" no tiene un valor asignado")
            s.addError(err)
            helper.setConsola("[ERROR] El parametro" + self.id +" no tiene un valor asignado en la línea "+ str(self.fila) +" y columna " + str(self.columna))
            return

    def genArbol(self) -> Nodo:
        nodo = Nodo("Parametro")
        nodo.agregarHijo(Nodo(str(self.id)))
        if self.tipo != None:
            nodo.agregarHijo(Nodo(str(self.tipo)))
        if self.valor != None:
            nodo.agregarHijo(self.valor.genArbol())

            
        return nodo



