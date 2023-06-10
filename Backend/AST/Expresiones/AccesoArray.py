from AST.Abstract.Expresion import Expresion
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO


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
            return None
        
        simbolo = entorno.ObtenerSimbolo(self.id)
        
        listaAccesos = []
        #verificar que sea un array
        
        for a in self.accesos:
            listaAccesos.append(a.ejecutar(entorno, helper).valor)

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
            except:
                #error semantico
                return None
            if valor.tipo == TIPO_DATO.ARRAY :
                return self.accesar(pila, valor, entorno, helper)
            else:
                if len(pila) == 0:
                    print('acceso tiene de la lista[index]:')
                    print(lista.valor[index])
                    return lista.valor[index]
                else:
                    #error semantico
                    return None

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
