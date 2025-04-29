# ShadowKey Estudo

Este é um projeto de ESTUDO que simula páginas de login de redes sociais para fins educacionais. O projeto demonstra como criar interfaces web realistas e como implementar um sistema de coleta de dados básico.

## 🚀 Funcionalidades

- Páginas de login simuladas para:
  - Facebook
  - Instagram
  - LinkedIn
  - Twitter (X)
- Interface visual semelhante às plataformas originais
- Animações e transições realistas
- Armazenamento de dados em arquivos JSON

## 📋 Pré-requisitos

- Python 3.x
- Flask
- Flask-CORS

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/keylogger-estudo.git
cd keylogger-estudo
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🎮 Como Usar

1. Inicie o servidor:
```bash
python server.py
```

2. Acesse as páginas de login:
- Facebook: `http://localhost:5000/`
- Instagram: `http://localhost:5000/instagram`
- LinkedIn: `http://localhost:5000/linkedin`
- Twitter: `http://localhost:5000/twitter`

## 📁 Estrutura do Projeto

```
keylogger-estudo/
├── data/                  # Pasta para armazenar os dados capturados
│   ├── captura_facebook.json
│   ├── captura_instagram.json
│   ├── captura_linkedin.json
│   └── captura_twitter.json
├── static/                # Arquivos estáticos (CSS, JS, imagens)
│   ├── style.css
│   ├── script.js
│   └── images/
├── templates/             # Templates HTML
│   ├── index.html
│   ├── instagram.html
│   ├── linkedin.html
│   └── twitter.html
├── server.py             # Servidor Flask
└── requirements.txt      # Dependências do projeto
```

## 📝 Formato dos Dados

Os dados são armazenados em arquivos JSON com o seguinte formato:
```json
{
    "timestamp": "DD/MM/YYYY HH:MM:SS",
    "rede_social": "nome_da_rede",
    "email": "email@exemplo.com",
    "senha": "senha123"
}
```

## ⚠️ Aviso Legal

Este projeto é apenas para fins educacionais. O uso deste software para atividades maliciosas é estritamente proibido. O desenvolvedor não se responsabiliza pelo uso indevido deste código.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

- Nome: [Iuri Costa]
- GitHub: [@seu-usuario](https://github.com/iurizero)

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.