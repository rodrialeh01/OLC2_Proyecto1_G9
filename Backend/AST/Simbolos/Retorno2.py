class Retorno2:
    def __init__(self, valor, tipo, isTemp, auxType = "", length=0, referencia = ''):
        self.valor = valor
        self.tipo = tipo
        self.isTemp = isTemp
        self.auxType = auxType
        self.length = length
        self.referencia = referencia
        self.trueLabel = ''
        self.falseLabel = ''
        self.arr = []
        self.verifArraydec = False
        self.test = ''