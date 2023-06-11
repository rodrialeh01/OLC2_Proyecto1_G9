from AST.Abstract.Instruccion import Instruccion
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.Simbolo import Simbolo


class Instancia(Instruccion, Simbolo):
    #nombreDeclarado, ID_Struct, listaParams, linea, columna
    def __init__(self, nombreDeclarado, id_interface, listaParams, linea, columna):
        self.nombreDeclarado = nombreDeclarado
        self.id_interface = id_interface
        self.listaParams = listaParams
        self.linea = linea
        self.columna = columna

    def ejecutar(self, entorno, helper):

        existe_interface = entorno.ExisteInterface(self.id_interface)

        if not existe_interface:
            #error semantico
            #print("Error semantico: No existe la interface: " + self.id_interface)
            return
    
        existe_nombre = entorno.ExisteSimbolo(self.nombreDeclarado)
        if existe_nombre:
            #error semantico
            #print("Error semantico: Ya existe el simbolo: " + self.nombreDeclarado)
            return

        '''
            entorno nos retorne el struct
            agarramos la lista de parametros del struct y la comparamos con la lista de parametros que nos mandaron
        '''
        #obtenemos el objeto al cual se esta referenciando
        objeto = entorno.ObtenerInterface(self.id_interface)
        #obtenemos la lista de parametros del objeto
        # nombre : expresion          nombre : tipo
        lista_parametros_objeto = objeto.listaParametros
        #comparamos la lista de parametros del objeto con la lista de parametros que nos mandaron
        if self.listaParams == None:
            #error semantico
            return

        if len(lista_parametros_objeto) != len(self.listaParams):
            #error semantico
            #print("Error semantico: La cantidad de parametros no coincide")
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
                            #print("Error semantico: El tipo de parametro no coincide")
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
                print("+99999999999999999999999999999", param)
                params.agregarHijo(param.genArbol())
        nodo.agregarHijo(params)
        return nodo