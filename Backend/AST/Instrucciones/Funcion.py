from AST.Abstract.Instruccion import Instruccion
from AST.Instrucciones.Transferencia.Return import Return
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Simbolo import Simbolo


class Funcion(Simbolo, Instruccion):
    def __init__(self, nombre, params, listaInstrucciones, linea, columna, tipo) -> None:
        super().__init__()
        print("VOY A CREAR LA FUNCIÓN: ")
        print('---------------------')
        super().crearFuncion(nombre, params, listaInstrucciones, linea, columna, tipo)
        print("Creando funcion")
        self.nombre = nombre
        self.params = params
        self.listaInstrucciones = listaInstrucciones
        self.tipo = tipo

    def declaracionesParams(self, entorno, exp, entornoPadre, helper):
        print("EXP: ", exp)
        if self.params is None and exp is None:
            print("No hay parametros")
            return True
        
        paramsDecl = self.params
        if len(paramsDecl) != len(exp):
            print("Error semántico, la cantidad de argumentos no coincide con la cantidad de parametros")
            return False
        
        print("-------------------------", str(self.params))
        contador = 0
        print(paramsDecl)
        for param in paramsDecl:
            print("parametro: " + param.id)
            print(param.esRef)
            if param.esRef is True:
                param.valRef = exp[contador]
                param.entorno = entornoPadre

            param.utilizado = exp[contador].ejecutar(entorno, helper)
            param.ejecutar(entorno, helper)

            #funcion("hola", a);

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
            print(accion is not None)
            if accion is not None:
                if isinstance(instruccion, Return) or isinstance(instruccion, Retorno):
                    #verificar que el tipo de dato que se retorna sea el mismo que el de la funcion
                    if accion.tipo is not TIPO_DATO.ANY or accion.tipo is not TIPO_DATO.NULL or accion.tipo is not TIPO_DATO.ERROR:
                        helper.setFuncion(tempHelper)
                        print("Tipo de la función: ", self.tipo)
                        if self.tipo is not accion.tipo:
                            print("Error semantico, tipo de dato de retorno no coincide con el de la funcion")
                            return
                        
                        #si es el mismo tipo de dato, se retorna el valor
                        return Retorno(accion.valor, accion.tipo)
                        
                    else:
                        helper.setFuncion(tempHelper)
                        #si es de tipo any, null o error, es un proceso diferente
                        return Return(None, TIPO_DATO.NULL)
                    
        
    def genArbol(self) -> Nodo:
        nodo = Nodo("Funcion")
        nodo.agregarHijo(Nodo(str(self.nombre)))
        nodo2 = Nodo("Parametros")
        for param in self.params:
            nodo2.agregarHijo(param.genArbol())
        nodo.agregarHijo(nodo2)
        nodo3 = Nodo("Instrucciones")
        for instruccion in self.listaInstrucciones:
            nodo3.agregarHijo(instruccion.genArbol())
        nodo.agregarHijo(nodo3)
        return nodo
    