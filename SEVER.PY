from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Licencias
licencias = {
    "ABC123": {
        "expira": "2026-06-30",
        "estado": "active"
    }
}

@app.route('/validar', methods=['GET'])
def validar():

    licencia = request.args.get('licencia')

    if licencia not in licencias:
        return jsonify({
            "status": "invalid"
        })

    datos = licencias[licencia]

    fecha_expira = datetime.strptime(
        datos["expira"],
        "%Y-%m-%d"
    )

    if datetime.now() > fecha_expira:
        return jsonify({
            "status": "expired"
        })

    return jsonify({
        "status": "active",
        "expires": datos["expira"]
    })

if __name__ == '__main__':
    app.run(port=5000)