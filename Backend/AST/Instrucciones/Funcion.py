from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Instrucciones.Transferencia.Return import Return
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores


class Funcion(Simbolo, Instruccion):
    def __init__(self, nombre, params, listaInstrucciones, linea, columna, tipo) -> None:
        super().__init__()
        super().crearFuncion(nombre, params, listaInstrucciones, linea, columna, tipo)
        ##print("Creando funcion")
        self.nombre = nombre
        self.params = params
        self.listaInstrucciones = listaInstrucciones
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def declaracionesParams(self, entorno, exp, entornoPadre, helper):
        ##print("EXP: ", exp)
        if self.params is None and exp is None:
            return True
        
        if self.params is None and exp is not None:
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "La cantidad de argumentos no coincide con la cantidad de parametros")
            s.addError(err)
            helper.setConsola("[ERROR] La cantidad de argumentos no coincide con la cantidad de parametros en la línea "+ str(self.linea) +" y columna " + str(self.columna))
            return False


        paramsDecl = self.params
        if len(paramsDecl) != len(exp):
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "La cantidad de argumentos no coincide con la cantidad de parametros")
            s.addError(err)
            helper.setConsola("[ERROR] La cantidad de argumentos no coincide con la cantidad de parametros en la línea "+ str(self.linea) +" y columna " + str(self.columna))
            ##print("Error semántico, la cantidad de argumentos no coincide con la cantidad de parametros")
            return False
        
        ##print("-------------------------", str(self.params))
        contador = 0
        ##print(paramsDecl)
        for param in paramsDecl:
            param.utilizado = exp[contador].ejecutar(entornoPadre, helper)
            param.ejecutar(entorno, helper)
            contador += 1

        return True
        
    def ejecutar(self, entorno, helper):
        tempHelper = helper.getFuncion()
        helper.setFuncion("Funcion")
        
        for instruccion in self.listaInstrucciones:

            #instruccion.ejecutar(entorno, helper)
            if instruccion is None:
                continue
            accion = instruccion.ejecutar(entorno, helper)

            if accion is not None:
                if isinstance(accion, Return) or isinstance(accion, Retorno):
                    if isinstance(accion.valor, int) or isinstance(accion.valor, float):
                        accion.tipo = TIPO_DATO.NUMERO
                    elif isinstance(accion.valor, str):
                        accion.tipo = TIPO_DATO.CADENA
                    elif isinstance(accion.valor, bool):
                        accion.tipo = TIPO_DATO.BOOLEANO
                    #verificar que el tipo de dato que se retorna sea el mismo que el de la funcion
                    if accion.tipo is not TIPO_DATO.NULL or accion.tipo is not TIPO_DATO.ERROR:
                        helper.setFuncion(tempHelper)
                        if self.tipo is not None:
                            if isinstance(self.tipo, TIPO_DATO):
                                if self.tipo is not accion.tipo:
                                    s = SingletonErrores.getInstance()
                                    err = Error(self.linea, self.columna, "Error Semántico", "El tipo de dato de retorno no coincide con el de la funcion")
                                    s.addError(err)
                                    helper.setConsola("[ERROR] El tipo de dato de retorno no coincide con el de la funcion en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                                    ##print("Error semantico, tipo de dato de retorno no coincide con el de la funcion")
                                    return
                            else:
                                #busca si existe el objeto al cual se esta referenciando
                                existe_interface = entorno.ExisteInterface(self.tipo)
                                ##print(existe_interface)
                                if existe_interface is None:
                                    s = SingletonErrores.getInstance()
                                    err = Error(self.linea, self.columna, "Error Semántico", "El tipo de dato ",self.tipo," de la funcion ",self.nombre," no existe")
                                    s.addError(err)
                                    helper.setConsola("[ERROR] El tipo de dato ", self.tipo," de la funcion ", self.nombre," no existe en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                                    ##print("Error semantico, tipo de dato de retorno no coincide con el de la funcion")
                                    return
                                

                                #busca si coincide el objeto a retornar con el tipo de objeto de la funcion
                                list_params = accion.valor.paramDeclarados
                                referencia = entorno.ObtenerInterface(self.tipo)

                                lista_parametros_objeto = referencia.params
                                lista_ya_Declarada = []
                                verificacion = True
                                #recorremos la lista de parametros del objeto
                                for i in range(0, len(lista_parametros_objeto)):
                                    #placa : "P-1234" <- exp = Retorno("P-1234", TIPO_DATO.CADENA)
                                    if verificacion:
                                        verificacion = False
                                        for j in range(0, len(list_params)):
                                            if lista_parametros_objeto[i].id in list_params[j]:
                                                verificacion = True
                                                exp = list_params[j][lista_parametros_objeto[i].id]
                                                if lista_parametros_objeto[i].tipo != exp.tipo:
                                                    #error semantico
                                                    s = SingletonErrores.getInstance()
                                                    err = Error(self.linea, self.columna, "Error Semántico", "El tipo de dato para el parametro " + lista_parametros_objeto[i].id + " no coincide" )
                                                    s.addError(err)
                                                    helper.setConsola("[ERROR] El tipo de dato para el parametro " + lista_parametros_objeto[i].id + " no coincide en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                                                    return
                                                j = len(list_params)
                                    else:
                                        break
                                if verificacion == False:
                                    #error semantico
                                    s = SingletonErrores.getInstance()
                                    err = Error(self.linea, self.columna, "Error Semántico", "El tipo de dato que va a retornar no coincide con el tipo de objeto " + self.tipo + " que es de la funcion" )
                                    s.addError(err)
                                    helper.setConsola("[ERROR] El tipo de dato que va a retornar no coincide con el tipo de objeto " + self.tipo + " que es de la funcion no coincide en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                                    return
                        
                        helper.setTs(entorno)
                        return Retorno(accion.valor, accion.tipo)
                    else:

                        helper.setFuncion(tempHelper)
                        s = SingletonErrores.getInstance()
                        err = Error(self.linea, self.columna, "Error Semántico", "El tipo de dato de retorno no coincide con el de la funcion")
                        s.addError(err)
                        #helper.setConsola("[ERROR] El tipo de dato de retorno no coincide con el de la funcion en la línea "+ str(self.linea) +" y columna " + str(self.columna))
                        helper.setConsola("[ERROR] REVISAR POR QUÉ SE GENERA ESTE ERROR EN LA FUNCIÓN")
                        return Return(None, TIPO_DATO.ERROR)
        helper.setTs(entorno)
        helper.setFuncion(tempHelper)            
        
    def genArbol(self) -> Nodo:
        nodo = Nodo("FUNCIÓN")
        nodo.agregarHijo(Nodo(str(self.nombre)))
        nodo2 = Nodo("Parametros")
        if self.params is not None:
            for param in self.params:
                nodo2.agregarHijo(param.genArbol())
            nodo.agregarHijo(nodo2)
        nodo3 = Nodo("Instrucciones")
        for instruccion in self.listaInstrucciones:
            nodo3.agregarHijo(instruccion.genArbol())
        nodo.agregarHijo(nodo3)
        return nodo
    