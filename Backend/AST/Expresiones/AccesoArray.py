from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class AccesoArray(Expresion):
    def __init__(self, id, accesos, linea, columna):
        self.id = id
        self.accesos = accesos
        self.linea = linea
        self.columna = columna


    def ejecutar(self, entorno, helper):

        #buscar el id en el entorno
        existe = entorno.ExisteSimbolo(self.id)
        if not existe:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La variable " + self.id + " no existe en el entorno actual" )
            s.addError(err)
            helper.setConsola("[ERROR]: La variable " + self.id + " no existe en el entorno actual " + " en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
            Retorno(None, TIPO_DATO.ERROR)
        
        simbolo = entorno.ObtenerSimbolo(self.id)
        
        listaAccesos = []
        #verificar que sea un array
        for a in self.accesos:
            listaAccesos.append(a.ejecutar(entorno, helper).valor)
        xd = self.accesar(listaAccesos, simbolo, entorno, helper)
        return xd

    def accesar(self, pila, lista, entorno, helper):
        if len(pila) == 0:
            return lista
        else:
            index = pila.pop(0)
            try:
                valor = lista.valor[index]
                #print(isinstance(valor, Retorno))
            except:
                #error semantico
                #print("ERROR SOTE")
                s = SingletonErrores.getInstance()
                err = Error(self.linea, self.columna, "Error Semántico", "El indice al que se intenta acceder no existe en el array")
                s.addError(err)
                helper.setConsola("[ERROR]: El indice al que se intenta acceder no existe en el array en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
                return Retorno(None, TIPO_DATO.ERROR)
            if len(pila) == 0 and isinstance(valor, Retorno)==False:
                return Retorno(valor, TIPO_DATO.CADENA)
            elif valor.tipo == TIPO_DATO.ARRAY :
                return self.accesar(pila, valor, entorno, helper)
            elif valor.tipo == TIPO_DATO.CADENA and len(pila) > 0 and len(valor.valor)> 1:
                return self.accesar(pila, valor, entorno, helper)
            else:
                if len(pila) == 0:
                    #print(lista.valor[index])
                    return lista.valor[index]
                else:
                    #error semantico
                    s = SingletonErrores.getInstance()
                    err = Error(self.linea, self.columna, "Error Semántico", "No se puede acceder al valor que se intenta acceder al array")
                    s.addError(err)
                    #print("esto es un ERRRRRRRRROR")
                    helper.setConsola("[ERROR]: No se puede acceder al valor que se intenta acceder al array en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
                    return Retorno(None, TIPO_DATO.ERROR)

    def genArbol(self) -> Nodo:
        nodo = Nodo("ACCESO ARRAY")
        nodo.agregarHijo(Nodo(str(self.id)))
        listaAcc = []
        for a in self.accesos:
            listaAcc.append(a.genArbol())
        for a in listaAcc:
            nodo.agregarHijo(a)
        return nodo
