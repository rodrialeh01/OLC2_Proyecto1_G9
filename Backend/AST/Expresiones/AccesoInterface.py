from AST.Abstract.Expresion import Expresion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO
from AST.Simbolos.Retorno import Retorno
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores


class AccesoInterface(Expresion):
    def __init__(self, id_interface,ids_param, linea, columna):
        self.id_interface = id_interface
        self.ids_param = ids_param
        self.linea = linea
        self.columna = columna
        super().__init__()
        
    def ejecutar(self, entorno, helper):
        existe = entorno.ExisteInterfaceDeclarada(self.id_interface)
        if not existe:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.linea, self.columna, "Error Semántico", "No se encontró la variable " + str(self.id_interface))
            helper.setConsola("[ERROR]: No se encontró la variable " + str(self.id_interface) + " en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
            s.addError(err)
            return Retorno(None, TIPO_DATO.ERROR)
        objeto = entorno.ObtenerInterfaceDeclarada(self.id_interface)
        if len(self.ids_param) == 1:
            for p in objeto.paramDeclarados:
                for accs in self.ids_param:
                    if accs in p:
                        if not isinstance(p[accs], list):
                            return p[accs]
                        else:
                            # Se crea un simbolo temporal que no se guarde para que retorne la interfaz
                            sim = Simbolo()
                            sim.crearStructDeclarado(p,p[accs],'',self.linea,self.columna)
                            return Retorno(sim, TIPO_DATO.INTERFACE)
        elif len(self.ids_param) > 1:
            acceso_a_retornar = self.obtenerAccesos(self.ids_param, objeto, entorno, helper)
            return acceso_a_retornar
                
        #error semantico
        s = SingletonErrores.getInstance()
        err = Error(self.linea, self.columna, "Error Semántico", "La variable " + str(self.id_interface) + " no posee el atributo" + str(self.ids_param) )
        helper.setConsola("[ERROR]: La variable " + str(self.id_interface) + " no posee el atributo " + str(self.ids_param) + " en la linea: " + str(self.linea) + " y columna: " + str(self.columna))
        s.addError(err)
        return Retorno(None, TIPO_DATO.ERROR)
    
    def obtenerAccesos(self, lista,objeto, entorno, helper):
        print('$$$$$$$$$$$$$$$$$$$$$$$$')
        print(objeto.objeto)
        print(lista)
        print(objeto.paramDeclarados)
        print('$$$$$$$$$$$$$$$$$$$$$$$$')
        tipo_objeto = entorno.ObtenerInterface(objeto.objeto)
        for p in objeto.paramDeclarados:
            for accs in lista:
                for t in tipo_objeto.params:
                    print('////////////////////////')
                    print(accs)
                    print(t.id)
                    print('////////////////////////')
                    print(accs == t.id)
                    if accs == t.id:
                        dic = self.obtenerDic(objeto.paramDeclarados, accs)
                        if len(lista) == 1:
                            print("aaaaaa")
                            print(accs)
                            print(objeto.paramDeclarados)
                            print('========================')
                            print(dic[accs])
                            print('========================')
                            if not isinstance(dic[accs], list):
                                print("!!!!!!!!!!!!!!!!!!!")
                                print(dic[accs])
                                return dic[accs]
                            else:
                                # Se crea un simbolo temporal que no se guarde para que retorne la interfaz
                                sim = Simbolo()
                                sim.crearStructDeclarado(p,dic[accs],'',self.linea,self.columna)
                                return Retorno(sim, TIPO_DATO.INTERFACE)
                        else:
                            sim_temp = Simbolo()
                            sim_temp.crearStructDeclarado(accs,dic[accs],t.tipo,self.linea,self.columna)
                            return self.obtenerAccesos(lista[1:],sim_temp,entorno,helper)

    def obtenerDic(self, lista, id):
        print('3ntr3')
        for l in lista:
            print(l)
            if id in l:
                print('ziii')
                return l

    def genC3D(self, entorno, helper):
        pass

    def genArbol(self) -> Nodo:
        nodo = Nodo("ACCESO INTERFACE")
        nodo.agregarHijo(Nodo(str(self.id_interface)))
        return nodo
