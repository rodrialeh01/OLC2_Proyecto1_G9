from AST.Abstract.Instruccion import Instruccion


class AsignarInterface(Instruccion):
    def __init__(self, id_interface,id_param,expresion, linea, columna):
        self.id_interface = id_interface
        self.id_param = id_param
        self.expresion = expresion
        self.linea = linea
        self.columna = columna


    def ejecutar(self, entorno, helper):
        print("hola?")
        existe = entorno.ExisteInterfaceDeclarada(self.id_interface)
        if not existe:
            return
        objeto = entorno.ObtenerInterfaceDeclarada(self.id_interface)
        print("----------------AsignarInterface-------------------")
        print(self.id_param)
        print(objeto.paramDeclarados)

        print(self.id_param in objeto.paramDeclarados)
        for p in objeto.paramDeclarados:
            if self.id_param in p:
                if p[self.id_param].tipo != self.expresion.tipo:
                    pass
                    return
                p[self.id_param].valor = self.expresion.ejecutar(entorno,helper).valor
                entorno.ActualizarInterfaceDeclarada(self.id_interface, objeto)
                return
                
        #error semantico
