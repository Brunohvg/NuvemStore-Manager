function formatField(inputElement, format) {
    inputElement.addEventListener("input", function () {
        let value = this.value.replace(/\D/g, ''); // Remove todos os caracteres não numéricos
        let formattedValue = '';

        for (let i = 0; i < format.length && value.length > 0; i++) {
            if (format[i] === '#') {
                formattedValue += value[0];
                value = value.slice(1);
            } else {
                formattedValue += format[i];
            }
        }

        this.value = formattedValue;
    });
}

// JavaScript
document.addEventListener("DOMContentLoaded", function () {
    // Obtenha todos os elementos de menu
    var menuItems = document.querySelectorAll(".nav-item");

    // Adicione um ouvinte de evento de clique a cada item de menu
    menuItems.forEach(function (menuItem) {
        menuItem.addEventListener("click", function (event) {
            // Evite que o link siga o URL
            event.preventDefault();

            // Remova a classe "active" de todos os itens de menu
            menuItems.forEach(function (item) {
                item.classList.remove("active");
            });

            // Adicione a classe "active" apenas ao elemento de menu clicado
            menuItem.classList.add("active");
        });
    });
});

// Usando a função formatField para formatar o campo "cep"
formatField(document.getElementById("cep"), "#####-####");

// Usando a função formatField para formatar o campo "id_cep"
formatField(document.querySelector("#id_cep"), "#####-####");

// Usando a função formatField para formatar o campo "id_telefone"
formatField(document.querySelector("#id_telefone"), "(##) #####-####");

// JavaScript
document.addEventListener("DOMContentLoaded", function () {
    // Obtenha todos os elementos de menu
    var menuItems = document.querySelectorAll(".nav-item");

    // Adicione um ouvinte de evento de clique a cada item de menu
    menuItems.forEach(function (menuItem) {
        menuItem.addEventListener("click", function (event) {
            // Evite que o link siga o URL
            event.preventDefault();

            // Remova a classe "active" de todos os itens de menu
            menuItems.forEach(function (item) {
                item.classList.remove("active");
            });

            // Adicione a classe "active" apenas ao elemento de menu clicado
            menuItem.classList.add("active");
        });
    });
});