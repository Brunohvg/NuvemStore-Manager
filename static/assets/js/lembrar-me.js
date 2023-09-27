// Quando o usuário submete o formulário de login
document.querySelector('#login-form').addEventListener('submit', function (event) {
    // Previne a submissão padrão do formulário
    event.preventDefault();

    // Obtém o nome de usuário e a senha dos campos do formulário
    let username = document.querySelector('#username').value;
    let password = document.querySelector('#password').value;

    // Verifica se a caixa de seleção "Lembrar-me" está marcada
    if (document.querySelector('#remember-me').checked) {
        // Se estiver marcada, armazena o nome de usuário no armazenamento local
        localStorage.setItem('username', username);
    } else {
        // Se não estiver marcada, remove o nome de usuário do armazenamento local
        localStorage.removeItem('username');
    }

    // Aqui você pode adicionar o código para autenticar o usuário...
});

// Quando a página é carregada
window.addEventListener('DOMContentLoaded', (event) => {
    // Verifica se há um nome de usuário no armazenamento local
    let rememberedUsername = localStorage.getItem('username');

    if (rememberedUsername) {
        // Se houver, preenche o campo do nome de usuário com ele
        document.querySelector('#username').value = rememberedUsername;

        // Marca a caixa de seleção "Lembrar-me"
        document.querySelector('#remember-me').checked = true;
    }
});