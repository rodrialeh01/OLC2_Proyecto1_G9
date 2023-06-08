import json

from AST.Error import Error
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.helper import Helper
from AST.SingletonErrores import SingletonErrores as Sing
from flask import Flask, jsonify, request
from flask_cors import CORS
from AST.Instrucciones.Funcion import Funcion
from gramatica import gramatica2

app = Flask(__name__)
cors = CORS(app)

@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    texto = request.json["texto"]
    print(texto)

    #utilizando singleton para errores:
    singletonErr = Sing.getInstance()
    singletonErr.reinicioErrores()
    parseado = gramatica2.parse(texto)

    entornoGlobal = Entorno(None)
    helpe = Helper()
    if parseado is not None:
        for i in parseado:
            if i is not None:
                try:
                    if isinstance(i, Funcion):
                        print("Estoy en una funcion")
                        print(i.nombre)
                        verif = entornoGlobal.ExisteFuncion(i.nombre)
                        print("soy verif" + str(verif))
                        if not verif:
                            print("Agregando funcion")
                            entornoGlobal.AgregarFuncion(i.nombre, i)
                    else:       
                        i.ejecutar(entornoGlobal,helpe)
                        print("Estoy en una instruccion")
                except Exception as e:
                    if isinstance(e, Error):
                        singletonErr.addError(e)
                        print(e)
    
    #print(singletonErr.getErrores())

    return jsonify({"message": helpe.getConsola()})

@app.route('/errores', methods=['GET'])
def errores():
    singletonErr = Sing.getInstance()
    return jsonify({"texto": singletonErr.getErrores()})


if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)