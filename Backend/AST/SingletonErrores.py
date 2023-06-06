class SingletonErrores:
    instancia = None
    ListaErrores = []

    def __private__(self):
        pass

    @staticmethod
    def getInstance():
        if SingletonErrores.instancia == None:
            SingletonErrores.instancia = SingletonErrores()
        return SingletonErrores.instancia
    
    def addError(self, error):
        self.ListaErrores.append(error)

    def getErrores(self):
        codigo_html = ""
        codigo_html += '''
        <table align="center" class="table table-striped "> \n
        <thead><tr> <th colspan="6">TABLA DE ERRORES</th> </tr></thead>\n
        <tr class="table-dark"><th >No.</th ><th>Tipo de Error</th><th>Descripción</th><th>Linea</th><th>Columna</th><th>Fecha y Hora</th></tr>\n
        '''
        contador = 1
        for i in self.ListaErrores:
            codigo_html += "<tr>"
            codigo_html += "<th scope=\"row\">" + str(contador) + "</th>\n"
            codigo_html += "<td>" + i.tipo + "</td>\n"
            codigo_html += "<td>" + i.desc + "</td>\n"
            codigo_html += "<td>" + str(i.fila) + "</td>\n"
            codigo_html += "<td>" + str(i.column) + "</td>\n"
            codigo_html += "<td>" + str(i.fechaHora) + "</td>\n"
            codigo_html += "</tr>"
            contador += 1

        codigo_html += "\n</table>\n"
        return codigo_html
    
    def reinicioErrores(self):
        self.ListaErrores = []