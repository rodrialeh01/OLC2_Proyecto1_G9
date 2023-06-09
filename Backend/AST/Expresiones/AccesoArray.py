from AST.Abstract.Expresion import Expresion
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

        xd = self.accesar(listaAccesos, simbolo.valor, entorno, helper)
        print('------------')
        print(xd.valor)
        return xd

    def accesar(self, pila, lista, entorno, helper):
        if len(pila) == 0:
            print("se vacio la pila")
            print(lista)
            return lista
        else:
            #{0,3,2}
            index = pila.pop(0)
            try:
                valor = lista[index]
                print(valor.tipo)
            except:
                #error semantico
                return None
            if valor.tipo == TIPO_DATO.ARRAY :
                print("si")
                return self.accesar(pila, valor.valor, entorno, helper)
            else:
                if len(pila) == 0:
                    return lista[index]
                else:
                    #error semantico
                    return None

#lista = [[1, 2, 3], [-9,-7]]
#lista[0] = [1, 2, 3]
