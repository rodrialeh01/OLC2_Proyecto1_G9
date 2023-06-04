import json

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    texto = request.json["texto"]
    print(texto)
    return jsonify({"message": "Success"})

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)