from AST.Abstract.Instruccion import Instruccion
from AST.Error import Error
from AST.Simbolos.Enums import TIPO_DATO, obtTipoDato
from AST.Simbolos.Retorno import Retorno
from AST.SingletonErrores import SingletonErrores


class Push(Instruccion):
    def __init__(self, id, expresion, linea, columna) :
        self.id = id
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, entorno, helper):
        existe = entorno.ExisteSimbolo(self.id)
        if existe:
            val = entorno.ObtenerSimbolo(self.id)
            val2 = self.expresion.ejecutar(entorno, helper)
            
            # ninguno inserta null y unicamente el que inserta arrays son los de tipo array_any/array
            if val.tipo == TIPO_DATO.NUMERO or val.tipo == TIPO_DATO.CADENA or val.tipo == TIPO_DATO.BOOLEANO or val.tipo == TIPO_DATO.NULL:
                s = SingletonErrores.getInstance()
                s.addError(Error(self.linea, self.columna, "Semantico", "No es posible hacer push a un tipo de variable que no es array"))
                helper.setConsola("[ERROR] Un tipo de dato que no es array no posee la funcion push en linea: "+str(self.linea)+ " y columna: "+str(self.columna))
                return
            elif val.tipo == TIPO_DATO.ARRAY:
                val.valor.append(val2)
                entorno.ActualizarSimbolo(self.id, val)
            elif val.tipo == TIPO_DATO.ARRAY_NUMBER:
                if val2.tipo == TIPO_DATO.NUMERO:
                    val.valor.append(val2.valor)
                    entorno.ActualizarSimbolo(self.id, val)
                else:
                    s = SingletonErrores.getInstance()
                    s.addError(Error(self.linea, self.columna, "Semantico", "No es posible hacer push de tipo de dato "+obtTipoDato(val2.tipo)+ " a un array de tipo number"))
                    helper.setConsola("[ERROR] No es posible hacer push de tipo de dato "+obtTipoDato(val2.tipo)+ " a un array de tipo number en la línea "+str(self.linea)+ " y columna: "+str(self.columna))
                    return
            elif val.tipo == TIPO_DATO.ARRAY_STRING:
                if val2.tipo == TIPO_DATO.CADENA:
                    val.valor.append(val2.valor)
                    entorno.ActualizarSimbolo(self.id, val)
                else:
                    s = SingletonErrores.getInstance()
                    s.addError(Error(self.linea, self.columna, "Semantico", "No es posible hacer push de tipo de dato "+obtTipoDato(val2.tipo)+ " a un array de tipo string"))
                    helper.setConsola("[ERROR] No es posible hacer push de tipo de dato "+obtTipoDato(val2.tipo)+ " a un array de tipo string en la línea "+str(self.linea)+ " y columna: "+str(self.columna))
                    return
            elif val.tipo == TIPO_DATO.ARRAY_BOOLEAN:
                if val2.tipo == TIPO_DATO.BOOLEANO:
                    val.valor.append(val2.valor)
                    entorno.ActualizarSimbolo(self.id, val)
                else:
                    s = SingletonErrores.getInstance()
                    s.addError(Error(self.linea, self.columna, "Semantico", "No es posible hacer push de tipo de dato "+obtTipoDato(val2.tipo)+ " a un array de tipo boolean"))
                    helper.setConsola("[ERROR] No es posible hacer push de tipo de dato "+obtTipoDato(val2.tipo)+ " a un array de tipo boolean en la línea "+str(self.linea)+ " y columna: "+str(self.columna))
                    return
            elif val.tipo == TIPO_DATO.ARRAY_NULL:
                if val2.tipo == TIPO_DATO.NULL:
                    val.valor.append(val2.valor)
                    entorno.ActualizarSimbolo(self.id, val)
                else:
                    s = SingletonErrores.getInstance()
                    s.addError(Error(self.linea, self.columna, "Semantico", "No es posible hacer push de tipo de dato "+obtTipoDato(val2.tipo)+ " a un array de tipo null"))
                    helper.setConsola("[ERROR] No es posible hacer push de tipo de dato "+obtTipoDato(val2.tipo)+ " a un array de tipo null en la línea "+str(self.linea)+ " y columna: "+str(self.columna))
                    return

            elif val.tipo == TIPO_DATO.ARRAY_INTERFACE:
                if val2.tipo == TIPO_DATO.INTERFACE:
                    
                    pass
                else:
                    s = SingletonErrores.getInstance()
                    s.addError(Error(self.linea, self.columna, "Semantico", "No es posible hacer push de tipo de dato "+obtTipoDato(val2.tipo)+ " a un array de tipo interface"))
                    helper.setConsola("[ERROR] No es posible hacer push de tipo de dato "+obtTipoDato(val2.tipo)+ " a un array de tipo interface en la línea "+str(self.linea)+ " y columna: "+str(self.columna))
                    return

    def genArbol(self):
        pass