from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
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

    def ejecutar(self, entorno, helper):

        existe_interface = entorno.ExisteInterface(self.id_interface)

        if not existe_interface:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La interface " + self.id_interface + " no existe" )
            s.addError(err)
            helper.setConsola("[ERROR] La interface " + self.id_interface + " no existe en la línea "+ str(self.fila) +" y columna " + str(self.columna))
            return
    
        existe_nombre = entorno.ExisteSimbolo(self.nombreDeclarado)
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

        verificacion = True
        #recorremos la lista de parametros del objeto
        for i in range(0, len(lista_parametros_objeto)):
            #placa : "P-1234" <- exp = Retorno("P-1234", TIPO_DATO.CADENA)
            if verificacion:
                verificacion = False
                for j in range(0, len(self.listaParams)):
                    if lista_parametros_objeto[i].id == self.listaParams[j].id:
                        verificacion = True
                        exp = self.listaParams[j].expresion.ejecutar(entorno, helper)
                        if lista_parametros_objeto[i].tipo != exp.tipo:
                            #error semantico
                            s = SingletonErrores.getInstance()
                            err = Error(self.fila, self.columna, "Error Semántico", "El tipo de dato para el parametro " + lista_parametros_objeto[i].id + " no coincide" )
                            s.addError(err)
                            helper.setConsola("[ERROR] El tipo de dato para el parametro " + lista_parametros_objeto[i].id + " no coincide en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                            return
                        
                        lista_ya_Declarada.append({
                            lista_parametros_objeto[i].id : exp
                        })

                        j = len(self.listaParams)
            else:
                break
            

        #creamos el simbolo
        self.crearStructDeclarado(self.nombreDeclarado, lista_ya_Declarada, self.linea, self.columna)
        entorno.AgregarInterfaceDeclarada(self.nombreDeclarado, self)
    
    def genArbol(self) -> Nodo:
        nodo = Nodo("INSTANCIA")
        nodo.agregarHijo(Nodo(str(self.nombreDeclarado)))
        nodo.agregarHijo(Nodo(str(self.id_interface)))
        params = Nodo("PARAMETROS INTERFACE")
        if self.listaParams != None:
            for param in self.listaParams:
                params.agregarHijo(param.genArbol())
        nodo.agregarHijo(params)
        return nodo