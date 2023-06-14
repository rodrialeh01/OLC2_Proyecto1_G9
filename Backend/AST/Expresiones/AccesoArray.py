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
        print("ejecutar?")
        print(self.accesos)
        #buscar el id en el entorno
        existe = entorno.ExisteSimbolo(self.id)
        print(existe)
        if not existe:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La variable " + self.id + " no existe en el entorno actual" )
            s.addError(err)
            Retorno(None, None)
        
        simbolo = entorno.ObtenerSimbolo(self.id)
        
        listaAccesos = []
        #verificar que sea un array
        
        for a in self.accesos:
            listaAccesos.append(a.ejecutar(entorno, helper).valor)
        print('listaAccesos: ', listaAccesos)
        xd = self.accesar(listaAccesos, simbolo, entorno, helper)
        print('Te voy a enviar desde el acceso: ', xd)
        return xd

    def accesar(self, pila, lista, entorno, helper):
        print('LISTA ESSSSSS:', lista)
        if len(pila) == 0:
            return lista
        else:
            #{0,3,2}
            index = pila.pop(0)
            try:
                valor = lista.valor[index]
                print("VALOR: ", valor)
                print("LENPILA", len(pila))
                print(isinstance(valor, Retorno))
            except:
                #error semantico
                s = SingletonErrores.getInstance()
                err = Error(self.fila, self.columna, "Error Semántico", "El indice al que se intenta acceder no existe en el array")
                s.addError(err)
                return Retorno(None, None)
            if len(pila) == 0 and isinstance(valor, Retorno)==False:
                print("-------------------------------si?")
                return Retorno(valor, TIPO_DATO.CADENA)
            elif valor.tipo == TIPO_DATO.ARRAY :
                return self.accesar(pila, valor, entorno, helper)
            elif valor.tipo == TIPO_DATO.CADENA and len(pila) > 0 and len(valor.valor)> 1:
                print("+++++++++++++++++++++++++++++++si?")
                return self.accesar(pila, valor, entorno, helper)
            else:
                if len(pila) == 0:
                    print('acceso tiene de la lista[index]:')
                    print(lista.valor[index])
                    return lista.valor[index]
                else:
                    #error semantico
                    s = SingletonErrores.getInstance()
                    err = Error(self.fila, self.columna, "Error Semántico", "No se puede acceder al valor que se intenta acceder al array")
                    s.addError(err)
                    return Retorno(None, None)

    def genArbol(self) -> Nodo:
        nodo = Nodo("ACCESO ARRAY")
        nodo.agregarHijo(Nodo(str(self.id)))
        listaAcc = []
        for a in self.accesos:
            listaAcc.append(a.genArbol())
        for a in listaAcc:
            nodo.agregarHijo(Nodo("["))
            nodo.agregarHijo(a)
            nodo.agregarHijo(Nodo("]"))
        return nodo
