from AST.Error import Error
from AST.Instrucciones.Declaracion import Declaracion
from AST.Instrucciones.DeclaracionArray import DeclaracionArray
from AST.Instrucciones.Funcion import Funcion
from AST.Instrucciones.Interface import Interface
from AST.Nodo import Nodo
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.helper import Helper
from AST.SingletonErrores import SingletonErrores as Sing
from flask import Flask, jsonify, request
from flask_cors import CORS
from gramatica import gramatica2

# importando los errores que se agregaron a la gramatica2:


app = Flask(__name__)
cors = CORS(app)

nodo = Nodo("INICIO")
entornoTemp = ""
helpe = Helper()
@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    global entornoTemp
    global nodo
    global helpe
    nodo = Nodo("INICIO")
    texto = request.json["texto"]
    print(texto)

    #utilizando singleton para errores:
    singletonErr = Sing.getInstance()
    singletonErr.reinicioErrores()
    parseado = gramatica2.parse(texto)
    entornoGlobal = Entorno(None)
    entornoGlobal.setActual("Global")
    helpe = Helper()
    helpe.Ts = ""

    for err in gramatica2.errores:
        if isinstance(err, Error):
            helpe.setConsola("[ERROR] "+err.desc )


    if parseado is not None:
        for i in parseado:
            if i is not None:
                try:
                    if isinstance(i, Funcion):
                        verif = entornoGlobal.ExisteFuncion(i.nombre)

                        if not verif:
                            entornoGlobal.AgregarFuncion(i.nombre, i)
                    else:
                        i.ejecutar(entornoGlobal, helpe)         
                except Exception as e:
                    if isinstance(e, Error):
                        singletonErr.addError(e)
                        print(e)

        # for i in parseado:
        #     if i is not None:
        #         try:
        #             if isinstance(i, Interface) or isinstance(i, Declaracion) or isinstance(i, DeclaracionArray) :
        #                 i.ejecutar(entornoGlobal,helpe)
                        
        #         except Exception as e:
        #             if isinstance(e, Error):
        #                 singletonErr.addError(e)
        #                 print(e)

        # for i in parseado:
        #     if i is not None:
        #         try:
        #             if not isinstance(i, Funcion) and not isinstance(i, Interface) and not isinstance(i, Declaracion) and not isinstance(i, DeclaracionArray):
        #                 i.ejecutar(entornoGlobal,helpe)
                        
        #         except Exception as e:
        #             if isinstance(e, Error):
        #                 singletonErr.addError(e)
        #                 print(e)
    
        # for i in parseado:
        #     if i is not None:
        #         try:
        #             nodo.agregarHijo(i.genArbol())
        #         except Exception as e:
        #             print(e)

    #print(singletonErr.getErrores())
    entornoTemp = ""
    entornoTemp = entornoGlobal.getSimbolos()
    return jsonify({"message": helpe.getConsola()})

@app.route('/errores', methods=['GET'])
def errores():
    singletonErr = Sing.getInstance()
    return jsonify({"texto": singletonErr.getErrores()})

@app.route('/Ts', methods=['GET'])
def ts():
    global entornoTemp
    global helpe
    codigo_html = '''
        <table align="center" class="table table-striped "> \n
        <thead><tr> <th colspan="5">TABLA DE SÍMBOLOS</th> </tr></thead>\n
        <h6> NOTA: FALTA CAMBIAR LOS TIPOS DE ALGUNAS COSAS (EJ: TIPO_DATO.NUMBER -> NUMBER) </h6>\n
        <h6> NOTA: FALTA AGREGAR SÍMBOLOS DE LAS FUNCIONES </h6>\n
        <tr class="table-dark"><th>Nombre</th><th>Tipo</th><th>Ámbito</th><th>Fila</th><th>Columna</th></tr>\n
        '''
    codigo_html += entornoTemp + helpe.getTs() + "\n</table>"
    print(codigo_html)
    return jsonify({"texto": codigo_html})

@app.route('/Arbol', methods=['GET'])
def arbol():
    global nodo
    textoG = "digraph G {"
    tree = nodo.instArbol()
    textoG += tree
    textoG += "}"

    return jsonify({"texto": textoG})

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)