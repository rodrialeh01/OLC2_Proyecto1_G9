from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Expresiones.Identificador import Identificador
from AST.Expresiones.Primitivo import Primitivo
from AST.Instrucciones.Instancia import Instancia
from AST.Instrucciones.Transferencia.Return import Return
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.generador import Generador
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores


class Funcion(Simbolo, Instruccion):
    def __init__(self, nombre, params, listaInstrucciones, linea, columna, tipo) -> None:
        super().__init__()
        super().crearFuncion(nombre, params, listaInstrucciones, linea, columna, tipo)
        print("Creando funcion " + nombre)
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
            print("PARAMETRO: ", exp[contador])
            param.utilizado = exp[contador].ejecutar(entornoPadre, helper)
            param.ejecutar(entorno, helper)
            contador += 1

        return True
        
    def ejecutar(self, entorno, helper):
        tempHelper = helper.getFuncion()
        helper.setFuncion("Funcion")
        print("EEEEEEEEEEEEEEEEEEEEEEEEEEL TIPOOOOOOOOOOOOOOOOOOOOOOOOOOOOO:")
        print(self.tipo)
        for instruccion in self.listaInstrucciones:

            #instruccion.ejecutar(entorno, helper)
            if instruccion is None:
                continue
            accion = instruccion.ejecutar(entorno, helper)
            print("ACCION: ", accion)
            if accion is not None:
                if isinstance(accion, Return) or isinstance(accion, Retorno):
                    if (isinstance(accion.valor, int) or isinstance(accion.valor, float)) and not isinstance(accion.valor, bool):
                        accion.tipo = TIPO_DATO.NUMERO
                    elif isinstance(accion.valor, str):
                        accion.tipo = TIPO_DATO.CADENA
                    elif isinstance(accion.valor, bool):
                        print("le asigno acá que si es booleano")
                        accion.tipo = TIPO_DATO.BOOLEANO
                    #verificar que el tipo de dato que se retorna sea el mismo que el de la funcion
                    if accion.tipo is not TIPO_DATO.NULL or accion.tipo is not TIPO_DATO.ERROR:
                        helper.setFuncion(tempHelper)
                        if self.tipo is not None:
                            if isinstance(self.tipo, TIPO_DATO):
                                print("TIPO DE DATO DE LA FUNCION: ", self.tipo)
                                print("TIPO DE DATO DEL RETURN: ", accion.tipo)
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
                                print("LISTA DE PARAMETROS DEL OBJETO: ", lista_parametros_objeto)
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
                                print('RETORNO ACCION: ', accion.valor)
                                for a in range(len(accion.valor.listaParams)):
                                    if isinstance(accion.valor.listaParams[a].expresion, Identificador):
                                        ret = accion.valor.listaParams[a].expresion.ejecutar(entorno, helper)
                                        accion.valor.listaParams[a].expresion = Primitivo(ret.tipo, ret.valor, self.linea,self.columna)
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

    def genC3D(self, entorno, helper):
        #print("Generando C3D de funcion")
        gen = Generador()
        generador = gen.getInstance()
        generador.addComment("Inicio de la funcion " + self.nombre)

        
        entorno.AgregarFuncion(self.nombre, self)
        entornoLocal = Entorno(entorno)

        labelRetorno = generador.newLabel()
        entornoLocal.returnLabel = labelRetorno
        entornoLocal.size = 1
        #print("------------------------")
        #print(self.nombre)

        if self.params is not None:
            for p in self.params:
                entornoLocal.setEntorno(p.id,p.tipo ,(p.tipo == TIPO_DATO.CADENA or p.tipo == TIPO_DATO.INTERFACE or p.tipo == TIPO_DATO.ARRAY))
        
        generador.addBeginFunc(self.nombre)
        for i in self.listaInstrucciones:
            accion = i.genC3D(entornoLocal, helper)
            #print('accion',accion)
            #print('i',i)
            if isinstance(i, Return):
                print('retorno')
                print(i)
                if entornoLocal.returnLabel != '':
                    if accion.trueLabel == '':
                        generador.addComment("Retorno de la funcion ")
                        generador.setStack('P', accion.valor)
                        generador.addGoto(labelRetorno)
                        generador.addComment("Fin del retorno")
                    else:
                        generador.addComment("Retorno de la funcion ")
                        generador.putLabel(accion.trueLabel)
                        generador.setStack('P', '1')
                        generador.addGoto(entornoLocal.returnLabel)
                        generador.putLabel(entornoLocal.falseLabel)
                        generador.setStack('P', '0')
                        generador.addGoto(entornoLocal.returnLabel)
                        generador.addComment("Fin del retorno")

        generador.addGoto(labelRetorno)
        generador.putLabel(labelRetorno)
        generador.addComment("Fin de la funcion " + self.nombre)
        generador.addEndFunc()
        
        return
        
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
    