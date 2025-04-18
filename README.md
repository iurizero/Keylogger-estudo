
# Keylogger simples para estudo
Este é um projeto de uma página de login fake do Facebook a fim de estudos, desenvolvido com HTML, CSS, JavaScript e Python (Flask).

## Descrição

A página de login permite que os usuários insiram um email ou telefone e uma senha. Quando o botão "Entrar" é clicado, os dados são enviados para um servidor local usando uma requisição `fetch`. O servidor, desenvolvido com Flask, registra os dados em um arquivo JSON.

## Tecnologias Utilizadas

- HTML
- CSS
- JavaScript
- Python (Flask)

## Estrutura do Projeto

- `index.html`: Contém a estrutura HTML da página.
- `style.css`: Contém os estilos CSS para a página.
- `script.js`: Contém o código JavaScript para manipulação dos inputs e envio dos dados.
- `app.py`: Contém o código Python para o servidor Flask que registra os dados.

## Como Executar o Projeto

1. Clone este repositório.
2. Certifique-se de ter o Python e o Flask instalados em sua máquina. Você pode fazer isso executando o seguinte comando no terminal:
    ```pip install flask```
3. Execute o servidor Flask com o comando:
    ```python app.py```
4. Abra o arquivo `index.html` em seu navegador.
5. Certifique-se de que o servidor local está rodando na porta 5000 para receber os dados enviados pelo formulário.
6. Agora é só inserir um usuário e senha pra testes e ele sera salvo no arquivo captura.json (Clicando você verá os dados inseridos)