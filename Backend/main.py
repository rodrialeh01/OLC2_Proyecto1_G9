import json

from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.helper import Helper
from flask import Flask, jsonify, request
from flask_cors import CORS
from gramatica import gramatica
from AST.SingletonErrores import SingletonErrores as Sing
from AST.Error import Error
app = Flask(__name__)
cors = CORS(app)

@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    texto = request.json["texto"]
    print(texto)

    #utilizando singleton para errores:
    singletonErr = Sing.getInstance()

    parseado = gramatica.parse(texto)
    retorno_consola = ""
    entornoGlobal = Entorno(retorno_consola,None)
    helpe = Helper()
    if parseado is not None:
        for i in parseado:
            if i is not None:
                try:
                    i.ejecutar(entornoGlobal,helpe)
                except Exception as e:
                    if isinstance(e, Error):
                        singletonErr.addError(e)
                        print(e)
    
    print(singletonErr.getErrores())


    return jsonify({"message": helpe.getConsola()})

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)