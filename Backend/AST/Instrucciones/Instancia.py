from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Expresiones.Llamada import Llamada
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores


class Instancia(Instruccion, Simbolo):
    #nombreDeclarado, ID_Struct, listaParams, linea, columna
    def __init__(self, nombreDeclarado, id_interface, listaParams, fila, columna):
        self.nombreDeclarado = nombreDeclarado
        self.id_interface = id_interface
        self.listaParams = listaParams
        self.fila = fila
        self.columna = columna
        super().__init__()

    def ejecutar(self, entorno, helper):
        print("ENTRO A CREAR INSTANCIA")
        print("SI ES INSTANCIA COMO ES?: ", self.listaParams)
        existe_interface = entorno.ExisteInterface(self.id_interface)

        if not existe_interface:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La interface " + self.id_interface + " no existe" )
            s.addError(err)
            helper.setConsola("[ERROR] La interface " + self.id_interface + " no existe en la línea "+ str(self.fila) +" y columna " + str(self.columna))
            return
    
        existe_nombre = entorno.BuscarSimboloLocal(self.nombreDeclarado)
        if not existe_nombre:
            existe_nombre = entorno.BuscarInterfaceLocal(self.nombreDeclarado)
            if not existe_nombre:
                existe_nombre = entorno.BuscarInterfaceDeclaradaLocal(self.nombreDeclarado)
        if existe_nombre:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La variable " + self.nombreDeclarado + " ya fue declarada anteriormente en el entorno actual" )
            s.addError(err)
            helper.setConsola("[ERROR] La variable " + self.nombreDeclarado + " ya fue declarada anteriormente en el entorno actual en la línea "+ str(self.fila) +" y columna " + str(self.columna))
            return

        #obtenemos el objeto al cual se esta referenciando
        objeto = entorno.ObtenerInterface(self.id_interface)
        #obtenemos la lista de parametros del objeto
        # nombre : expresion          nombre : tipo
        if isinstance(self.listaParams, list):
            print("ES UNA LISTAAAAA")
            lista_parametros_objeto = objeto.listaParametros
            #comparamos la lista de parametros del objeto con la lista de parametros que nos mandaron
            if self.listaParams == None:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "La cantidad de parametros para la interface no coincide" )
                s.addError(err)
                helper.setConsola("[ERROR] La cantidad de parametros para la interface no coincide en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                return

            if len(lista_parametros_objeto) != len(self.listaParams):
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "La cantidad de parametros para la interface no coincide" )
                helper.setConsola("[ERROR] La cantidad de parametros para la interface no coincide en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                s.addError(err)
                return
            
            lista_ya_Declarada = []
            print('EL SELF.LISTA PARAMS')
            print(self.listaParams[0].expresion)
            verificacion = True
            #recorremos la lista de parametros del objeto
            for i in range(0, len(lista_parametros_objeto)):
                #placa : "P-1234" <- exp = Retorno("P-1234", TIPO_DATO.CADENA)
                if verificacion:
                    verificacion = False
                    for j in range(0, len(self.listaParams)):
                        if lista_parametros_objeto[i].id == self.listaParams[j].id:
                            verificacion = True
                            if not isinstance(self.listaParams[j].expresion, list):
                                print('ITERACIONNNNNNNNNNNNN', self.listaParams[j].expresion)
                                exp = self.listaParams[j].expresion.ejecutar(entorno, helper)
                                print("EXP INTERFACE: ", exp.valor)
                                print(lista_parametros_objeto[i].tipo, exp.tipo)
                                if lista_parametros_objeto[i].tipo != exp.tipo and lista_parametros_objeto[i].tipo != TIPO_DATO.ANY:
                                    #error semantico
                                    s = SingletonErrores.getInstance()
                                    err = Error(self.fila, self.columna, "Error Semántico", "El tipo de dato para el parametro " + lista_parametros_objeto[i].id + " no coincide" )
                                    s.addError(err)
                                    helper.setConsola("[ERROR] El tipo de dato para el parametro " + lista_parametros_objeto[i].id + " no coincide en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                                    return
                                print('no es 3er0rrrrrrrrrrrrrrr')
                                lista_ya_Declarada.append({
                                    lista_parametros_objeto[i].id : exp
                                })
                                print(lista_ya_Declarada)
                            else:
                                struct_interno = self.listaParams[j].expresion
                                declarado = self.declarar_sub_interface(struct_interno, lista_parametros_objeto[i].tipo, entorno, helper)
                                if declarado is not None:
                                    lista_ya_Declarada.append({
                                        lista_parametros_objeto[i].id : declarado
                                    })
                            j = len(self.listaParams)
                else:
                    break
            #creamos el simbolo
            print("COMO DEBE DE SER: ", lista_ya_Declarada)
            self.crearStructDeclarado(self.nombreDeclarado, lista_ya_Declarada,self.id_interface, self.fila, self.columna)
            entorno.AgregarInterfaceDeclarada(self.nombreDeclarado, self)
            print('YA TE CREEEEEEEE ^-^')
        elif isinstance(self.listaParams, Llamada):
            existe_funcion = entorno.ExisteFuncion(self.listaParams.id)
            if not existe_funcion:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "La funcion " +self.listaParams + " no existe")
                s.addError(err)
                helper.setConsola("[ERROR] La funcion " +self.listaParams + " no existe en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                return
            
            return_func = self.listaParams.ejecutar(entorno, helper)
            print('.-.-.-.-.-.-')
            print(return_func.valor)
            print('&&&&&&&&&&&')
            if not isinstance(return_func.valor, Instancia):
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "La funcion " +self.listaParams + " no existe")
                s.addError(err)
                helper.setConsola("[ERROR] La funcion " +self.listaParams + " no existe en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                return
            
            if return_func.tipo != TIPO_DATO.INTERFACE:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "La funcion " +self.listaParams + " no retorna una interface")
                s.addError(err)
                helper.setConsola("[ERROR] La funcion " +self.listaParams + " no retorna una interface en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                return
            
            objeto_retornado = return_func.valor
            print("PERO ES: ",objeto_retornado.listaParams)
            list_sim = []



            for o in objeto_retornado.listaParams:
                print(o.expresion)

                exp_asig = o.expresion.ejecutar(entorno, helper)
                print(exp_asig)
                print('SE ME MURIO?:', exp_asig)


                list_sim.append({
                    o.id : exp_asig
                })
            print('LISTA SIM: ', list_sim)
            if self.id_interface != objeto_retornado.id_interface:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "El retorno de la funcion " +self.listaParams + " no es de tipo \"" + self.id_interface + "\"")
                s.addError(err)
                helper.setConsola("[ERROR] El retorno de la funcion " +self.listaParams + " no es de tipo \"" + self.id_interface + "\" en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                return
            self.crearStructDeclarado(self.nombreDeclarado, list_sim, self.id_interface, self.fila, self.columna)
            print('YA TE CREEEEEEEE \-^-^-/')
            print(self.nombreDeclarado)
            entorno.AgregarInterfaceDeclarada(self.nombreDeclarado, self)
            print('YA TE CREEEEEEEE -^-^-')

        elif isinstance(self.listaParams, str):
            existe_variable = entorno.ExisteInterfaceDeclarada(self.listaParams)
            if not existe_variable:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "La variable " +self.listaParams + " no existe")
                s.addError(err)
                helper.setConsola("[ERROR] La variable " +self.listaParams + " no existe en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                return
            print("OBTIENE UNA VARIABLE", existe_variable)
            contenido_variable = entorno.ObtenerInterfaceDeclarada(self.listaParams)
            if self.id_interface != contenido_variable.objeto:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "La variable a la cual quiere asignar a " +self.nombreDeclarado + " no es del tipo" + self.id_interface + " sino de tipo " + contenido_variable.objeto )
                s.addError(err)
                helper.setConsola("[ERROR] La variable a la cual quiere asignar a " +self.nombreDeclarado + " no es del tipo \"" + self.id_interface + "\" sino de tipo \"" + contenido_variable.objeto + "\" en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                return
            #creamos el simbolo
            self.crearStructDeclarado(self.nombreDeclarado, contenido_variable.paramDeclarados, self.id_interface, self.fila, self.columna)
            entorno.AgregarInterfaceDeclarada(self.nombreDeclarado, self)
        else:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La interfaz no se puede crear si no es con una llamada, variable o {atributos:expresion...}" )
            s.addError(err)
            helper.setConsola("[ERROR] La interfaz no se puede crear si no es con una llamada, variable o {atributos:expresion...} en la línea "+ str(self.fila) +" y columna " + str(self.columna))
            return

    
    def declarar_sub_interface(self, lista_params_objeto,tipo, entorno, helper):
        sub_interface = entorno.ObtenerInterface(tipo)
        lista_parametros_objeto = sub_interface.listaParametros
        lista_ya_Declarada = []
        verificacion = True
        #recorremos la lista de parametros del objeto
        for i in range(0, len(lista_parametros_objeto)):
            if verificacion:
                verificacion = False
                for j in range(0, len(lista_params_objeto)):
                    if lista_parametros_objeto[i].id == lista_params_objeto[j].id:
                        verificacion = True
                        if not isinstance(lista_params_objeto[j].expresion, list):
                            exp = lista_params_objeto[j].expresion.ejecutar(entorno, helper)
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
                        else:
                            struct = lista_params_objeto[j].expresion[0]
                            declarado = self.declarar_sub_interface(struct, lista_parametros_objeto[i].tipo, entorno, helper)
                            if declarado is not None:
                                lista_ya_Declarada.append({
                                    lista_parametros_objeto[i].id : declarado
                                })
                        j = len(lista_params_objeto)
        return lista_ya_Declarada


    def genArbol(self) -> Nodo:
        nodo = Nodo("INSTANCIA")
        return nodo
    
    def genC3D(self, entorno, helper):
        pass