from AST.Abstract.Instruccion import Instruccion
from AST.Simbolos.Simbolo import Simbolo
from AST.Instrucciones.Transferencia.Return import Return
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Enums import TIPO_DATO


class Funcion(Simbolo, Instruccion):
    def __init__(self, nombre, params, listaInstrucciones, linea, columna) -> None:
        super().__init__()
        super().crearFuncion(nombre, params, listaInstrucciones, linea, columna)
        print("Creando funcion")

    def declaracionesParams(self, entorno, exp, entornoPadre, helper):
        '''
        revisa que si se declararon los parametros de la funcion, la función al ser llamada obtenga 
        los valores de los parametros que se le pasaron (verifica cantidad y tipo)
        '''
        paramsDecl = self.params
        if len(paramsDecl) != len(exp):
            return False
        
        contador = 0
        print(paramsDecl)
        for param in paramsDecl:
            print("parametro: " + param.id)
            print(param.esRef)
            if param.esRef is True:
                param.valRef = exp[contador]
                param.entorno = entornoPadre

            print("QUIERO REVISAR")
            param.utilizado = exp[contador].ejecutar(entorno, helper)
            print(">>>>>> ", param.utilizado)
            param.ejecutar(entorno, helper)

            contador += 1

        return True
        
    def ejecutar(self, entorno, helper):
        for instruccion in self.listaInstrucciones:
            #instruccion.ejecutar(entorno, helper)
            if instruccion is None:
                continue

            accion = instruccion.ejecutar(entorno, helper)
            if accion is not None:
                if isinstance(accion, Return) or isinstance(accion, Retorno):
                    #verificar que el tipo de dato que se retorna sea el mismo que el de la funcion
                    if accion.tipo is not TIPO_DATO.ANY or accion.tipo is not TIPO_DATO.NULL or accion.tipo is not TIPO_DATO.ERROR:
                        if self.tipo is not accion.tipo:
                            print("Error semantico, tipo de dato de retorno no coincide con el de la funcion")
                            return
                        
                        #si es el mismo tipo de dato, se retorna el valor
                        return Retorno(accion.valor, accion.tipo)
                        
                    else:
                        #si es de tipo any, null o error, es un proceso diferente
                        #Return(Null, TIPO_DATO.NULL)
                        pass
                        


                    print("Ayúdame dios")