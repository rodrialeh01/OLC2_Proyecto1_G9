from AST.Error import Error
from AST.Instrucciones.Funcion import Funcion
from AST.Instrucciones.Interface import Interface
from AST.Simbolos.Entorno import Entorno
from AST.Simbolos.helper import Helper
from AST.SingletonErrores import SingletonErrores as Sing
from flask import Flask, jsonify, request
from flask_cors import CORS
from AST.Nodo import Nodo
from AST.Instrucciones.Declaracion import Declaracion
from AST.Instrucciones.DeclaracionArray import DeclaracionArray
from gramatica import gramatica2

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
    if parseado is not None:
        for i in parseado:
            if i is not None:
                try:
                    if isinstance(i, Funcion):
                        verif = entornoGlobal.ExisteFuncion(i.nombre)

                        if not verif:
                            entornoGlobal.AgregarFuncion(i.nombre, i)
                        
                except Exception as e:
                    if isinstance(e, Error):
                        singletonErr.addError(e)
                        print(e)

        for i in parseado:
            if i is not None:
                try:
                    if isinstance(i, Interface) or isinstance(i, Declaracion) or isinstance(i, DeclaracionArray) :
                        i.ejecutar(entornoGlobal,helpe)
                        
                except Exception as e:
                    if isinstance(e, Error):
                        singletonErr.addError(e)
                        print(e)

        for i in parseado:
            if i is not None:
                try:
                    if not isinstance(i, Funcion) and not isinstance(i, Interface) and not isinstance(i, Declaracion) and not isinstance(i, DeclaracionArray):
                        i.ejecutar(entornoGlobal,helpe)
                        
                except Exception as e:
                    if isinstance(e, Error):
                        singletonErr.addError(e)
                        print(e)
    
        for i in parseado:
            if i is not None:
                try:
                    nodo.agregarHijo(i.genArbol())
                except Exception as e:
                    print(e)
    
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
    
    entornoTemp += helpe.getTs() + "\n</table>"

    print(entornoTemp)
    return jsonify({"texto": entornoTemp})

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