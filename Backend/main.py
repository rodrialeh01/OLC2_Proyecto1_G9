from AST.Error import Error
from AST.Instrucciones.Funcion import Funcion
from AST.Instrucciones.Interface import Interface
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.helper import Helper
from AST.SingletonErrores import SingletonErrores as Sing
from flask import Flask, jsonify, request
from flask_cors import CORS
from gramatica import gramatica2

app = Flask(__name__)
cors = CORS(app)

global entornoGlobal
entornoGlobal = Entorno(None)
entornoGlobal.setActual("Global")

@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    global entornoTemp
    texto = request.json["texto"]
    print(texto)

    #utilizando singleton para errores:
    singletonErr = Sing.getInstance()
    singletonErr.reinicioErrores()
    parseado = gramatica2.parse(texto)

    entornoGlobal = Entorno(None)
    entornoGlobal.setActual("Global")
    helpe = Helper()
    if parseado is not None:
        for i in parseado:
            if i is not None:
                try:
                    if isinstance(i, Funcion):

                        print(i.nombre)
                        verif = entornoGlobal.ExisteFuncion(i.nombre)

                        if not verif:

                            entornoGlobal.AgregarFuncion(i.nombre, i)
                    else:       
                        i.ejecutar(entornoGlobal,helpe)
                        
                except Exception as e:
                    if isinstance(e, Error):
                        singletonErr.addError(e)
                        print(e)
    
    #print(singletonErr.getErrores())
    entornoTemp = entornoGlobal.getSimbolos()
    return jsonify({"message": helpe.getConsola()})

@app.route('/errores', methods=['GET'])
def errores():
    singletonErr = Sing.getInstance()
    return jsonify({"texto": singletonErr.getErrores()})

@app.route('/Ts', methods=['GET'])
def ts():
    # print(tablaS)
    return jsonify({"texto": entornoTemp})

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)