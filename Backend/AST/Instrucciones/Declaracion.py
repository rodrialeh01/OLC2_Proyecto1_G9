from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Nodo import Nodo
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.generador import Generador
from AST.Simbolos.Simbolo import Simbolo
from AST.SingletonErrores import SingletonErrores


class Declaracion(Instruccion):
    def __init__(self, id, tipo, valor, fila, columna):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna

        self.find = True
        self.hide = -1

        super().__init__()
    
    def ejecutar(self, entorno, helper):

        print("Declaracion")
        identificador = self.id
        tipo = self.tipo
        print(tipo)
        existe = entorno.BuscarSimboloLocal(identificador)
        if not existe:
            existe = entorno.BuscarInterfaceLocal(identificador)
            if not existe:
                existe = entorno.BuscarInterfaceDeclaradaLocal(identificador)
        if existe:
            #error semantico
            s = SingletonErrores.getInstance()
            err = Error(self.fila, self.columna, "Error Semántico", "La variable " + identificador + " ya fue declarada anteriormente en el entorno actual")
            s.addError(err)
            helper.setConsola("[ERROR] La variable " + identificador + " ya fue declarada anteriormente en el entorno actual en la línea "+ str(self.fila) +" y columna " + str(self.columna))
            return
        
        if tipo != None:
            if self.tipo == TIPO_DATO.NULL:
                if self.valor != None:
                    val = self.valor.ejecutar(entorno, helper)
                    if val.tipo != TIPO_DATO.NULL:
                        #error semantico
                        s = SingletonErrores.getInstance()
                        err = Error(self.fila, self.columna, "Error Semántico", "La variable " + identificador + " es de tipo NULL, no puede asignarle un valor")
                        s.addError(err)
                        helper.setConsola("[ERROR] La variable " + identificador + " es de tipo NULL, no puede asignarle un valor en la línea "+ str(self.fila) +" y columna " + str(self.columna))
                        return
                    simb = Simbolo()
                    simb.nombre = identificador
                    simb.tipo = TIPO_DATO.NULL
                    simb.valor = None
                    simb.linea = self.fila
                    simb.columna = self.columna
                    simb.entorno = entorno
                    entorno.AgregarSimbolo(identificador, simb)
                    return
                else:
                    simb = Simbolo()
                    simb.nombre = identificador
                    simb.tipo = TIPO_DATO.NULL
                    simb.valor = None
                    simb.linea = self.fila
                    simb.columna = self.columna
                    simb.entorno = entorno
                    entorno.AgregarSimbolo(identificador, simb)
                    return

            if self.valor != None:
                valorG = self.valor.ejecutar(entorno, helper)
                if valorG.tipo == tipo:
                    simb = Simbolo()
                    simb.nombre = identificador
                    simb.tipo = tipo
                    simb.valor = valorG.valor
                    simb.linea = self.fila
                    simb.columna = self.columna
                    simb.entorno = entorno
                    entorno.AgregarSimbolo(identificador, simb)
                else:
                    s = SingletonErrores.getInstance()
                    err = Error(self.fila, self.columna, "Error Semántico", "No se ha podido declarar ya que los tipos no son iguales")
                    s.addError(err)
                    helper.setConsola("[ERROR] La variable " + identificador + " no se ha podido declarar ya que los tipos no coinciden en: "+ str(self.fila) +" y columna " + str(self.columna))
                    return
            else:
                simb = Simbolo()
                simb.nombre = identificador
                simb.tipo = tipo
                if self.tipo == TIPO_DATO.NUMERO:
                    simb.valor = 0
                elif self.tipo == TIPO_DATO.CADENA:
                    simb.valor = ""
                elif self.tipo == TIPO_DATO.BOOLEANO:
                    simb.valor = True
                else:
                    simb.valor = None
                simb.linea = self.fila
                simb.columna = self.columna
                simb.entorno = entorno

                entorno.AgregarSimbolo(identificador, simb)
        else:
            if self.valor != None:
                valorG = self.valor.ejecutar(entorno, helper)
                simb = Simbolo()
                simb.nombre = identificador
                simb.tipo = valorG.tipo
                simb.valor = valorG.valor
                simb.linea = self.fila
                simb.columna = self.columna
                simb.entorno = entorno

                entorno.AgregarSimbolo(identificador, simb)
            else:
                simb = Simbolo()
                simb.nombre = identificador
                simb.tipo = TIPO_DATO.ANY
                simb.valor = None
                simb.linea = self.fila
                simb.columna = self.columna
                simb.entorno = entorno

                entorno.AgregarSimbolo(identificador, simb)

    def genArbol(self) -> Nodo:
        nodo = Nodo("Declaracion")
        nodo_id = Nodo(str(self.id))
        if self.tipo != None:
            nodo_id.agregarHijo(Nodo(obtTipoDato(self.tipo)))
        if self.valor != None:
            nodo_id.agregarHijo(self.valor.genArbol())
        nodo.agregarHijo(nodo_id)
        return nodo
    
    def genC3D(self, entorno, helper):
        gen = Generador()
        generador = gen.getInstance()

        generador.addComment("Declaracion de variable")
        s_C3D = None
        val = None

        if self.tipo != None:
            val = self.valor.genC3D(entorno, helper)
        else:
            val = self.valor.genC3D(entorno, helper)
            self.tipo = val.tipo

        if self.tipo != None:
            if val != None:
                if self.tipo == val.tipo:
                    inHeap = val.tipo == TIPO_DATO.CADENA #or val.tipo == TIPO_DATO.INTERFACE or TIPO_DATO.ARRAY
                    s_C3D = entorno.setEntorno(self.id, val.tipo, inHeap, self.find)
            else:
                generador.addComment("Error: el tipo de dato no coincide al declarado")
                
            
        else:
            pass
        
        posicionTemp = s_C3D.posicion
        if not s_C3D.globalVar:
            posicionTemp = generador.addTemp()
            generador.addExpresion(posicionTemp, "P", s_C3D.posicion, "+")
        
        if self.tipo == TIPO_DATO.BOOLEANO:
            tempLbl = generador.newLabel()
            generador.putLabel(val.trueLabel)
            generador.setStack(posicionTemp, '1')
            
            generador.addGoto(tempLbl)
            
            generador.putLabel(val.falseLabel)
            generador.setStack(posicionTemp, '0')

            generador.putLabel(tempLbl)

        if self.tipo != TIPO_DATO.BOOLEANO:
            generador.setStack(posicionTemp, val.valor)
        else:
            if val.valor == True:
                generador.setStack(posicionTemp, '1')
            else:
                generador.setStack(posicionTemp, '0')
        generador.addComment("Fin declaracion de variable")