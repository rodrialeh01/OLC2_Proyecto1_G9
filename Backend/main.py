import json

from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.helper import Helper
from flask import Flask, jsonify, request
from flask_cors import CORS
from gramatica import gramatica

app = Flask(__name__)
cors = CORS(app)

@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    texto = request.json["texto"]
    print(texto)
    parseado = gramatica.parse(texto)
    retorno_consola = ""
    entornoGlobal = Entorno(retorno_consola,None)
    helpe = Helper()
    for i in parseado:
        i.ejecutar(entornoGlobal,helpe)

    return jsonify({"message": helpe.getConsola()})

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)